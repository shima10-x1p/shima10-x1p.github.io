#### Preflight
* 目的: Gemini で更新された `docs/agents/reference/テーマサンプル/index.html` のレイアウト変更（記事カードの構造・レスポンシブ挙動）を `themes/shima-island` のテーマへ反映する。
* 変更範囲: `themes/shima-island/templates/index.html` と `themes/shima-island/static/css/main.css`、作業ログ。公開URLや依存関係は変更しない。
* 前提: 既存のテーマ方針（Pico CSS、オレンジ基調、プロフィール設定の外出し）は維持する。`base.html` と `article.html` は必要時のみ最小変更。
* 手順:
  1. 参照 `index.html` の差分（記事カードの横並び化、post-contentラッパー、ボタン/タイトル寸法）を抽出する。
  2. `templates/index.html` を Pelican 変数を維持したまま新構造へ更新する。
  3. `static/css/main.css` に対応スタイルを追加・調整する。
  4. `ruff` と Pelican ビルドで描画エラーがないことを確認する。
  5. Postflight を記録する。
* 検証コマンド:
  * `uv run ruff check .`
  * `uv run pelican content -o output -s pelicanconf.py`
  * `uv run pelican content -o output -s publishconf.py`
* 相談が必要な点: Ask 条件に該当する変更（依存追加/削除、SITEURL変更、大規模構造変更）は実施しない。
