#### Preflight
* 目的: 記事ごとに `content/images/YYYY/MM/<slug>/` で画像を管理できるようにし、`index.html` と `article.html` にサムネイル表示機能を追加する。
* 変更範囲: `pelicanconf.py`、`themes/shima-island/templates/`、`themes/shima-island/static/css/`、`content/articles/`、`content/images/`、`docs/agent/logs/post-flight/`。触らない範囲は GitHub Actions 設定、公開 URL 設定、依存関係定義。
* 前提: `SITEURL` は変更しない。公開 URL 構造は既存の `articles/YYYY/MM/slug/` を維持する。言語は `ja`、タイムゾーンは `Asia/Tokyo` のまま。
* 手順: 1) `STATIC_PATHS` に `images` を追加 2) サムネイル解決フィルターを実装 3) `index.html` と `article.html` にサムネイル表示を追加 4) CSS で一覧/記事上部/本文画像の表示を調整 5) サンプル画像と記事サンプルを追加し lint/build を実行。
* 検証コマンド: `uv run ruff check .`、`uv run pelican content -o output -s pelicanconf.py`、必要に応じて `rg`/`sed` で生成結果確認。
* 相談が必要な点: なし（依存追加なし、SITEURL変更なし、大規模構造変更なし）。
