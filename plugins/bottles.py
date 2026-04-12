"""ボトルメール — スクラップ風スレッド形式投稿プラグイン。

content/bottles/{slug}/ 配下の meta.md + 連番 .md を読み込み、
一覧ページ (bottles.html) とスレッドページ (bottle.html) を生成する。

ディレクトリ構造::

    content/bottles/{slug}/
        meta.md      ← スレッド全体のメタ情報 (Title, Date, Tags, Slug)
        001.md       ← 個別投稿（Date 必須、Tags 任意）
        002.md
        ...

生成テンプレート:
    - ``bottles.html`` : 一覧ページ → output/bottles/index.html
    - ``bottle.html``  : スレッド → output/bottles/{slug}/index.html

Pelican の ``get_generators`` シグナルで ``BottlesGenerator`` を登録する。
"""

from __future__ import annotations

import logging
from datetime import datetime
from operator import attrgetter
from pathlib import Path
from typing import Any

from pelican import signals
from pelican.generators import Generator
from pelican.readers import MarkdownReader

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# データクラス
# ---------------------------------------------------------------------------
class BottlePost:
    """スレッド内の個別投稿を表すデータクラス。

    Attributes:
        date: 投稿日時。
        content: Markdown → HTML 変換済みの本文。
        tags: 投稿固有のタグ一覧。
    """

    def __init__(self, date: datetime, content: str, tags: list[str], image: str | None = None) -> None:
        self.date = date
        self.content = content
        self.tags = tags
        self.image = image  # 添付画像のサイトルート相対パス（例: images/bottles/slug/001.jpg）


class Bottle:
    """1 つのスレッド（meta.md + 個別投稿群）を表すデータクラス。

    Attributes:
        title: スレッドのタイトル（meta.md の Title）。
        slug: URL に使用するスラッグ。
        date: スレッド作成日（meta.md の Date）。
        tags: スレッド全体のタグ。
        posts: 個別投稿のリスト（時系列順）。
        url: スレッドの相対 URL パス。
        save_as: 出力先の相対ファイルパス。
    """

    def __init__(
        self,
        title: str,
        slug: str,
        date: datetime,
        tags: list[str],
        posts: list[BottlePost],
    ) -> None:
        self.title = title
        self.slug = slug
        self.date = date
        self.tags = tags
        self.posts = posts
        self.url = f"bottles/{slug}/"
        self.save_as = f"bottles/{slug}/index.html"

    @property
    def post_count(self) -> int:
        """スレッド内の投稿数を返す。

        Returns:
            int: 投稿数。
        """
        return len(self.posts)

    @property
    def last_updated(self) -> datetime:
        """スレッド内の最終更新日時を返す。

        投稿がある場合は最新投稿の日時、なければスレッド作成日を返す。

        Returns:
            datetime: 最終更新日時。
        """
        if self.posts:
            return max(p.date for p in self.posts)
        return self.date


# ---------------------------------------------------------------------------
# ジェネレーター
# ---------------------------------------------------------------------------
class BottlesGenerator(Generator):
    """content/bottles/ を走査してボトルメールページを生成するジェネレーター。

    Pelican の ``Generator`` を継承し、``generate_context`` でコンテンツを
    読み込み、``generate_output`` でテンプレートを使って HTML を書き出す。
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.bottles: list[Bottle] = []

    # -- 読み込みフェーズ ---------------------------------------------------

    def generate_context(self) -> None:
        """content/bottles/ 配下のスレッドを読み込みコンテキストに追加する。

        1. content/bottles/ のサブフォルダを走査
        2. 各フォルダ内の meta.md + 連番 .md を読み込み Bottle を構築
        3. 作成日の降順でソートし self.context["bottles"] に格納
        """
        bottles_path = Path(self.path) / "bottles"
        if not bottles_path.is_dir():
            logger.warning("bottles: %s が見つかりません", bottles_path)
            return

        reader = MarkdownReader(self.settings)

        # サブフォルダをアルファベット順に走査
        for thread_dir in sorted(bottles_path.iterdir()):
            if not thread_dir.is_dir():
                continue

            meta_file = thread_dir / "meta.md"
            if not meta_file.exists():
                logger.warning("bottles: %s に meta.md がありません", thread_dir)
                continue

            bottle = self._read_thread(thread_dir, meta_file, reader)
            if bottle:
                self.bottles.append(bottle)

        # 作成日の降順でソート（新しいスレッドが先頭）
        self.bottles.sort(key=attrgetter("date"), reverse=True)

        # テンプレートからアクセスできるようコンテキストに登録
        self._update_context(("bottles",))
        self.context["bottles"] = self.bottles

    def _read_thread(
        self,
        thread_dir: Path,
        meta_file: Path,
        reader: MarkdownReader,
    ) -> Bottle | None:
        """スレッドフォルダ 1 つ分を読み込み Bottle を構築する。

        Args:
            thread_dir: スレッドフォルダのパス。
            meta_file: meta.md のパス。
            reader: Markdown リーダー。

        Returns:
            Bottle | None: 読み込み成功時は Bottle、Date 不正時は None。
        """
        # meta.md からスレッド全体のメタ情報を取得
        _content, meta = self._read_md(meta_file, reader)

        title = meta.get("title", thread_dir.name)
        slug = meta.get("slug", thread_dir.name)
        date = self._parse_date(meta.get("date", ""))
        tags = self._parse_tags(meta.get("tags", ""))

        if date is None:
            logger.warning("bottles: %s の Date が不正です", meta_file)
            return None

        # 個別投稿を読み込み（meta.md 以外の .md をファイル名順 = 時系列順）
        posts: list[BottlePost] = []
        post_files = sorted(f for f in thread_dir.glob("*.md") if f.name != "meta.md")
        for post_file in post_files:
            post = self._read_post(post_file, reader)
            if post:
                posts.append(post)

        return Bottle(
            title=title,
            slug=slug,
            date=date,
            tags=tags,
            posts=posts,
        )

    def _read_post(self, path: Path, reader: MarkdownReader) -> BottlePost | None:
        """個別投稿ファイル (001.md 等) を読み込み BottlePost を構築する。

        Args:
            path: 投稿 Markdown ファイルのパス。
            reader: Markdown リーダー。

        Returns:
            BottlePost | None: 読み込み成功時は BottlePost、Date 不正時は None。
        """
        content, meta = self._read_md(path, reader)

        date = self._parse_date(meta.get("date", ""))
        if date is None:
            logger.warning("bottles: %s の Date が不正です", path)
            return None

        tags = self._parse_tags(meta.get("tags", ""))
        image_raw = meta.get("image", None)
        image = str(image_raw).strip() if image_raw else None
        return BottlePost(date=date, content=content, tags=tags, image=image)

    @staticmethod
    def _read_md(path: Path, reader: MarkdownReader) -> tuple[str, dict[str, Any]]:
        """Markdown ファイルを Pelican の MarkdownReader で読み込む。

        MarkdownReader.read() は (content, metadata) のタプルを返す。
        metadata の値には SafeMarkup (HTMLSafe 文字列) が含まれるため、
        ``.string`` 属性があればプレーン文字列に変換する。

        Args:
            path: 読み込み対象の Markdown ファイルパス。
            reader: Pelican の MarkdownReader インスタンス。

        Returns:
            tuple[str, dict[str, Any]]:
                HTML 変換済み本文と、キーを正規化したメタデータ辞書。
        """
        content, metadata = reader.read(str(path))

        # metadata の値を SafeMarkup → プレーン値に正規化
        meta: dict[str, Any] = {}
        for key, val in metadata.items():
            if hasattr(val, "string"):
                # SafeMarkup オブジェクトからプレーン文字列を取得
                meta[key] = val.string
            else:
                meta[key] = val
        return content, meta

    @staticmethod
    def _parse_date(value: Any) -> datetime | None:
        """日付文字列または datetime オブジェクトを datetime に変換する。

        Pelican の MarkdownReader が Date メタデータを datetime として
        返す場合があるため、まず isinstance でチェックする。
        文字列の場合は ``%Y-%m-%d %H:%M`` → ``%Y-%m-%d`` の順にパースを試みる。

        Args:
            value: Date メタデータの値（datetime / str / None）。

        Returns:
            datetime | None: パース成功時は datetime、失敗時は None。
        """
        if isinstance(value, datetime):
            return value
        if not value:
            return None
        for fmt in ("%Y-%m-%d %H:%M", "%Y-%m-%d"):
            try:
                return datetime.strptime(str(value).strip(), fmt)
            except ValueError:
                continue
        return None

    @staticmethod
    def _parse_tags(value: Any) -> list[str]:
        """タグメタデータをプレーンな文字列リストに変換する。

        入力はカンマ区切り文字列・リスト・タプルのいずれかを受け付ける。
        空白のみの要素は除外する。

        Args:
            value: Tags メタデータの値。

        Returns:
            list[str]: タグ文字列のリスト。
        """
        if not value:
            return []
        if isinstance(value, (list, tuple)):
            return [str(t).strip() for t in value if str(t).strip()]
        return [t.strip() for t in str(value).split(",") if t.strip()]

    # -- 出力フェーズ -------------------------------------------------------

    def generate_output(self, writer: Any) -> None:
        """一覧ページとスレッドページの HTML を出力する。

        Args:
            writer: Pelican の Writer インスタンス。
        """
        # 一覧ページ: output/bottles/index.html
        writer.write_file(
            name="bottles/index.html",
            template=self.get_template("bottles"),
            context=self.context,
            relative_urls=self.settings["RELATIVE_URLS"],
            bottles=self.bottles,
        )

        # 各スレッドページ: output/bottles/{slug}/index.html
        for bottle in self.bottles:
            writer.write_file(
                name=bottle.save_as,
                template=self.get_template("bottle"),
                context=self.context,
                relative_urls=self.settings["RELATIVE_URLS"],
                bottle=bottle,
            )


# ---------------------------------------------------------------------------
# Pelican 登録
# ---------------------------------------------------------------------------
def get_generators(pelican_object: Any) -> type[BottlesGenerator]:
    """get_generators シグナルのコールバック。

    Pelican のジェネレーター一覧に BottlesGenerator を追加する。

    Args:
        pelican_object: Pelican インスタンス（未使用だがシグナル仕様で必要）。

    Returns:
        type[BottlesGenerator]: ジェネレータークラス。
    """
    return BottlesGenerator


def register() -> None:
    """プラグイン登録エントリーポイント。

    Pelican のプラグインシステムが呼び出す。
    ``get_generators`` シグナルにコールバックを接続する。
    """
    signals.get_generators.connect(get_generators)
