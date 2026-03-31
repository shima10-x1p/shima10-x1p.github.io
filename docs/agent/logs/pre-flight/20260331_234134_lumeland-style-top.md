#### Preflight
* 目的: Pico.css を維持したまま、トップページ（記事一覧）を細い1カラム・静かな余白中心のブログデザインへ調整する。
* 変更範囲: `themes/shima-island/templates/base.html`, `themes/shima-island/templates/index.html`, `themes/shima-island/static/css/main.css`, `docs/agent/logs/`。触らない範囲は `content/` 配下の記事本文や Pelican 設定ファイル。
* 前提: SITEURL や公開URL構造は変更しない。言語・タイムゾーン設定は現状維持。Pico.css CDN 読み込みは維持。
* 手順: 1) 既存テンプレート構造確認 2) 変数上書き中心の CSS 設計 3) 必要最小限の HTML 調整（記事メタ順序対応） 4) ruff / pelican build で検証 5) postflight 記録。
* 検証コマンド: `uv run ruff check .` / `uv run pelican content -o output -s publishconf.py`
* 相談が必要な点: 依存追加・SITEURL変更・大規模構造変更は実施しないため該当なし。
