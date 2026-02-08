#### Preflight
* 目的: テーマ切替ボタンの視認性改善、ヘッダー高さの縮小、CSSの外部ファイル化、プロフィール情報の設定値外出しを行い、テーマ運用をしやすくする。
* 変更範囲: `themes/shima-island/templates/`、`themes/shima-island/static/css/`、`pelicanconf.py`、作業ログ。公開URLや依存関係は変更しない。
* 前提: 既存の Pelican URL構造・GitHub Pages デプロイ設定・SITEURL は維持する。テーマデザイン方向（オレンジ基調）は維持する。
* 手順:
  1. `main.css` を新規作成し、テンプレート内スタイルを移管する。
  2. `base.html` のヘッダー・テーマ切替ボタン・サイドバー表示をクラス駆動に置き換える。
  3. `index.html` / `article.html` のインラインスタイルを削減しクラス化する。
  4. `pelicanconf.py` にプロフィール設定値を追加し、テンプレートから参照する。
  5. `ruff` と Pelican ビルドで検証し、Postflight を記録する。
* 検証コマンド:
  * `uv run ruff check .`
  * `uv run pelican content -o output -s pelicanconf.py`
  * `uv run pelican content -o output -s publishconf.py`
* 相談が必要な点: Ask 条件に該当する変更（依存追加/削除、公開URLやSITEURL変更、大規模構造変更）は実施しない。
