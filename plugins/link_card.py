"""link_card — Markdown 単独行リンクを OGP カード HTML に変換するプラグイン。

Markdown の段落内に単独で書かれたリンク（行の先頭から末尾まで <a> 1つのみの
<p> 要素）を検出し、OGP 情報を取得してカード形式の HTML に変換する。

動作概要:
- `initialized` シグナルで MARKDOWN 設定に本拡張を注入する。
  → 記事・ボトルメールの MarkdownReader 両方に自動適用される。
- `LinkCardTreeProcessor` が変換後の ElementTree を走査し、単独行リンクを
  Python-Markdown の htmlStash 経由で raw HTML カードに置き換える。
- 内部 URL: OUTPUT_PATH 内の出力済み HTML を BeautifulSoup で解析。
  ※ フレッシュビルド初回は OUTPUT_PATH にファイルがないため fallback カード表示。
- 外部 URL: requests で HTTP GET し og:title / og:image を取得。
- 取得失敗時: URL + ドメインのみの fallback カードを表示し、ビルドは成功させる。
"""

from __future__ import annotations

import html
import logging
import re
from pathlib import Path
from typing import Any
from urllib.parse import urlparse
from xml.etree.ElementTree import Element  # noqa: S405 — 読み取り専用で使用

from markdown import Markdown
from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor
from pelican import signals

logger = logging.getLogger(__name__)

# ビルド内 OGP 取得結果のキャッシュ（URL → ogp dict）
_ogp_cache: dict[str, dict[str, str]] = {}

# Pelican の設定（initialized シグナルで注入）
_settings: dict[str, Any] = {}


# ---------------------------------------------------------------------------
# Pelican シグナルハンドラ
# ---------------------------------------------------------------------------


def _on_initialized(pelican: Any) -> None:
    """Pelican 初期化時に MARKDOWN 設定へ本拡張を注入する。

    Parameters:
        pelican: Pelican インスタンス。
    """
    global _settings  # noqa: PLW0603
    _settings = pelican.settings

    markdown_cfg = pelican.settings.setdefault("MARKDOWN", {})
    ext_configs = markdown_cfg.setdefault("extension_configs", {})
    # 既に登録されている場合はスキップ
    ext_configs.setdefault("link_card", {})

    extensions = markdown_cfg.setdefault("extensions", [])
    if "link_card" not in extensions:
        extensions.append("link_card")


def register() -> None:
    """Pelican のシグナルに本プラグインを登録する。"""
    signals.initialized.connect(_on_initialized)


# ---------------------------------------------------------------------------
# OGP 取得
# ---------------------------------------------------------------------------


def _fetch_ogp(url: str) -> dict[str, str]:
    """URL から OGP 情報を取得して辞書で返す。

    キャッシュがある場合はキャッシュを返す。取得に失敗した場合は
    タイトル・説明・画像が空の辞書を返し、呼び出し元が fallback カードを表示する。

    Parameters:
        url: 取得対象の URL。内部 URL（/ 始まり）と外部 URL の両方に対応。

    Returns:
        dict: ``title``, ``description``, ``image`` キーを持つ辞書。
    """
    if url in _ogp_cache:
        return _ogp_cache[url]

    result: dict[str, str] = {"title": "", "description": "", "image": ""}

    parsed = urlparse(url)
    is_internal = not parsed.scheme and not parsed.netloc  # 相対 URL

    if is_internal:
        result = _fetch_ogp_internal(url)
    else:
        result = _fetch_ogp_external(url)

    _ogp_cache[url] = result
    return result


def _fetch_ogp_internal(url: str) -> dict[str, str]:
    """内部 URL の OGP を OUTPUT_PATH の HTML から取得する。

    Parameters:
        url: サイトルート相対 URL（例: ``/articles/2026/04/slug/``）。

    Returns:
        dict: ``title``, ``description``, ``image`` キーを持つ辞書。
    """
    result: dict[str, str] = {"title": "", "description": "", "image": ""}

    output_path = _settings.get("OUTPUT_PATH", "output")
    # 末尾スラッシュの有無を吸収して index.html に解決
    path = url.lstrip("/").rstrip("/")
    candidate = Path(output_path) / path / "index.html"

    if not candidate.exists():
        logger.debug("link_card: 内部 URL の HTML が未生成: %s", candidate)
        return result

    try:
        from bs4 import BeautifulSoup  # noqa: PLC0415

        with candidate.open(encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")

        result["title"] = _og_meta(soup, "og:title") or _tag_text(soup, "title") or ""
        result["description"] = _og_meta(soup, "og:description") or ""
        result["image"] = _og_meta(soup, "og:image") or ""
    except Exception:  # noqa: BLE001
        logger.warning("link_card: 内部 URL の HTML 解析に失敗: %s", url)

    return result


def _fetch_ogp_external(url: str) -> dict[str, str]:
    """外部 URL の OGP を HTTP GET で取得する。

    Parameters:
        url: 取得対象の外部 URL。

    Returns:
        dict: ``title``, ``description``, ``image`` キーを持つ辞書。
    """
    result: dict[str, str] = {"title": "", "description": "", "image": ""}

    try:
        import requests  # noqa: PLC0415
        from bs4 import BeautifulSoup  # noqa: PLC0415

        headers = {"User-Agent": "Mozilla/5.0 (compatible; LinkCardBot/1.0)"}
        resp = requests.get(url, timeout=10, headers=headers)
        resp.raise_for_status()

        soup = BeautifulSoup(resp.text, "html.parser")
        result["title"] = _og_meta(soup, "og:title") or _tag_text(soup, "title") or ""
        result["description"] = _og_meta(soup, "og:description") or ""
        result["image"] = _og_meta(soup, "og:image") or ""
    except Exception:  # noqa: BLE001
        logger.warning("link_card: 外部 OGP 取得に失敗: %s", url)

    return result


def _og_meta(soup: Any, property_name: str) -> str:
    """BeautifulSoup の soup から OGP メタタグの content を取得する。

    Parameters:
        soup: BeautifulSoup インスタンス。
        property_name: ``og:title`` などの property 属性値。

    Returns:
        str: content の値。見つからなければ空文字。
    """
    tag = soup.find("meta", property=property_name)
    if tag and tag.get("content"):
        return str(tag["content"]).strip()
    return ""


def _tag_text(soup: Any, tag_name: str) -> str:
    """BeautifulSoup の soup からタグのテキストを取得する。

    Parameters:
        soup: BeautifulSoup インスタンス。
        tag_name: タグ名（例: ``"title"``）。

    Returns:
        str: タグのテキスト。見つからなければ空文字。
    """
    tag = soup.find(tag_name)
    if tag:
        return tag.get_text(strip=True)
    return ""


# ---------------------------------------------------------------------------
# カード HTML 生成
# ---------------------------------------------------------------------------


def _build_card_html(
    url: str,
    title: str,
    link_text: str,
) -> str:
    """OGP 情報からカード HTML を組み立てる。

    XSS 対策として html.escape で全値をエスケープする。
    タイトルが空の場合は fallback 表示（URL のみ）になる。

    Parameters:
        url: リンク先 URL。
        title: カードのタイトル文字列。
        link_text: Markdown で書かれたリンクテキスト。

    Returns:
        str: カード用 HTML 文字列。
    """
    parsed = urlparse(url)
    domain = html.escape(parsed.netloc or "")
    safe_url = html.escape(url, quote=True)
    safe_title = html.escape(title or link_text or url)

    return (
        f'<a href="{safe_url}" class="link-card" target="_blank" rel="noopener noreferrer">'
        f'  <span class="link-card__body">'
        f'    <span class="link-card__title">{safe_title}</span>'
        f'    <span class="link-card__domain">{domain}</span>'
        f"  </span>"
        f"</a>"
    )


# ---------------------------------------------------------------------------
# Python-Markdown 拡張
# ---------------------------------------------------------------------------

# htmlStash のプレースホルダーパターン（Python-Markdown 内部形式）
_PLACEHOLDER_RE = re.compile(r"wzxhzdk:\d+")


def _is_standalone_link(elem: Element) -> tuple[bool, str, str]:
    """<p> 要素が単独行リンクかどうか判定する。

    条件:
    - <p> の直接の子が <a> 1つだけ
    - <p> 自体のテキスト（<a> の前のテキスト）が空か空白のみ
    - <a> の tail テキスト（<a> の後のテキスト）が空か空白のみ

    Parameters:
        elem: 検査対象の Element。

    Returns:
        tuple: (is_standalone, href, link_text) の 3 要素タプル。
               単独行リンクでなければ (False, "", "") を返す。
    """
    children = list(elem)
    if len(children) != 1:
        return False, "", ""
    child = children[0]
    if child.tag != "a":
        return False, "", ""
    if elem.text and elem.text.strip():
        return False, "", ""
    if child.tail and child.tail.strip():
        return False, "", ""
    href = child.get("href", "")
    text = child.text or ""
    return bool(href), href, text


class LinkCardTreeProcessor(Treeprocessor):
    """ElementTree を走査し単独行リンクをカード HTML に置き換える。

    Python-Markdown の htmlStash を利用して raw HTML を安全に埋め込む。
    変換後の <p> は ``<p>プレースホルダー</p>`` となり、最終出力で
    Python-Markdown がプレースホルダーを raw HTML に展開する。
    """

    def run(self, root: Element) -> Element | None:
        """ElementTree のルートを受け取り変換を実施する。

        Parameters:
            root: Markdown 変換後の ElementTree ルート要素。

        Returns:
            Element | None: 変換後のルート要素（None でもよい）。
        """
        for elem in root.iter("p"):
            is_standalone, href, link_text = _is_standalone_link(elem)
            if not is_standalone:
                continue

            ogp = _fetch_ogp(href)
            card_html = _build_card_html(
                url=href,
                title=ogp.get("title", ""),
                link_text=link_text,
            )

            # htmlStash に格納してプレースホルダーを取得
            placeholder = self.md.htmlStash.store(card_html)

            # <p> の子を全て除去してプレースホルダーに置き換える
            for child in list(elem):
                elem.remove(child)
            elem.text = placeholder
        return None


class LinkCardExtension(Extension):
    """Markdown 拡張: 単独行リンクを OGP カードに変換する。"""

    def extendMarkdown(self, md: Markdown) -> None:  # noqa: N802
        """Treeprocessor を Markdown パイプラインに登録する。

        Parameters:
            md: Markdown インスタンス。
        """
        # 優先度 5（低め）で登録 — 他の treeprocessor 後に実行
        md.treeprocessors.register(LinkCardTreeProcessor(md), "link_card", 5)


def makeExtension(**kwargs: Any) -> LinkCardExtension:  # noqa: N802
    """Python-Markdown の拡張ファクトリー関数。

    Parameters:
        **kwargs: 拡張設定（現在は未使用）。

    Returns:
        LinkCardExtension: 拡張インスタンス。
    """
    return LinkCardExtension(**kwargs)
