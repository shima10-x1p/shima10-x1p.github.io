#### Preflight
* 目的: `docs/agents/reference/テーマサンプル` を基に、Pelican 用カスタムテーマ `themes/shima-island` の `base.html` / `index.html` / `article.html` を実運用可能な Jinja テンプレートとして整備する。
* 変更範囲: `themes/shima-island/templates/` と作業ログのみ。Pelican の公開URL設定や依存関係は変更しない。
* 前提: 公開URLは既存設定（`https://www.shima10-x1p.net`）を維持。テーマは Pico CSS ベース。既存記事URL設計（`/articles/YYYY/MM/slug/`）は維持。
* 手順:
  1. 参照サンプルの見た目と構造を抽出し、共通部を `base.html` に集約する。
  2. `index.html` を記事一覧ループ対応に置き換える。
  3. `article.html` を記事詳細表示用に置き換える。
  4. ローカルビルドでテンプレートの描画確認を行う。
  5. Postflight を記録する。
* 検証コマンド:
  * `uv run ruff check .`
  * `uv run pelican content -o output -s pelicanconf.py`
  * `uv run pelican content -o output -s publishconf.py`
* 相談が必要な点: Ask 条件（依存追加/削除、SITEURL・公開URL変更、大規模構造変更）に該当する変更は予定しない。
