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
