# Project Guidelines

## 目的
Python + Pelican で GitHub Pages 上に静的サイトを公開するリポジトリ。

## 技術スタック
- Python 3.14、Pelican 4.11.0.post0
- テーマ: `themes/shima-island-coral/`（Pico CSS ベース）
- パッケージ管理: uv
- デプロイ: GitHub Actions (`.github/workflows/pelican.yml`) — `main` ブランチへの push で自動デプロイ

## ビルド・開発コマンド
```bash
uv run pelican           # サイト生成
uv run pelican --listen  # ローカルプレビューサーバー起動
uv run ruff check .      # コード品質チェック
uv run ruff format .     # コード自動整形
```

## コンテンツ規約
- 記事は `content/articles/YYYY/MM/{slug}.md` に配置
- URL 構造: `https://www.shima10-x1p.net/articles/YYYY/MM/{slug}/`
- フロントマター必須項目: `Title`, `Date`, `Category`, `Slug`
- 静的ファイル: `content/images/YYYY/MM/{slug}/` に配置

## 構成の概要
```
content/articles/YYYY/MM/   # 記事 Markdown
themes/shima-island-coral/  # アクティブテーマ（Jinja2 + Pico CSS）
pelicanconf.py              # 開発用設定
publishconf.py              # 本番用設定（SITEURL を上書き）
.github/workflows/pelican.yml  # CI/CD パイプライン
```

## コーディング規約
- 言語設定: Python コード・コメントは日本語
- チャット・応答は日本語
- シンプルさ優先: YAGNI / KISS / DRY
- テーマテンプレートは最低限のみ（不要なテンプレートを増やさない）

## 境界
**Always（必ず行う）**
- 変更後にビルドし (`uv run pelican`)、成功・失敗を報告する
- 触ったファイル一覧を最後に列挙する

**Ask（事前に確認）**
- 依存関係の追加・削除
- `SITEURL` など公開 URL を含む設定変更
- ディレクトリ構造の大規模変更・テーマの全面入れ替え

**Never（禁止）**
- シークレット・トークンをコミットしない
- `output/` を手編集しない（生成物）
- 意図不明な大改造を独断で進めない

## 完了条件
- `uv run pelican` でビルド成功
- ローカルプレビューで正常表示
- 変更が目的に対して過剰でない

---

## ボトルメール機能

スクラップ風の「短い投稿をスレッド形式で連ねる」機能。

### 関連ファイル

| ファイル | 役割 |
|----------|------|
| `plugins/bottles.py` | カスタムジェネレータープラグイン本体 |
| `themes/shima-island-coral/templates/bottles.html` | 一覧ページテンプレート |
| `themes/shima-island-coral/templates/bottle.html` | スレッドページテンプレート |
| `themes/shima-island-coral/static/css/style.css` | ボトルメール用 CSS（`.bottle-*` クラス） |

### コンテンツ構造

```
content/bottles/{slug}/
    meta.md      # スレッド全体のメタ情報
    001.md       # 個別投稿（時系列順）
    002.md
    ...
```

**meta.md フロントマター（必須: Title, Date, Slug / 任意: Tags）**

```markdown
Title: スレッドのタイトル
Date: 2026-04-12
Tags: tag1, tag2
Slug: my-thread
```

**個別投稿フロントマター（必須: Date / 任意: Tags）**

```markdown
Date: 2026-04-12 14:30
Tags: tag1
```

### URL 構造

| ページ | URL |
|--------|-----|
| 一覧 | `/bottles/` |
| スレッド | `/bottles/{slug}/` |

### プラグイン実装の注意点

- `MarkdownReader.read(path)` を直接呼ぶこと（`Readers.read_file()` は `Page` オブジェクトを返すため不可）
- `metadata` の `date` は Pelican が `datetime` オブジェクトとして返す場合があるため `_parse_date` で型チェックが必要
- コードブロックの二重枠防止: `.bottle-post-body .highlight pre { border: none; }` を CSS に設定済み
