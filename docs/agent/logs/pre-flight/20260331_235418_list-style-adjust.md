#### Preflight
* 目的: 記事一覧をカード感なし・影なし・細い区切り線中心のリスト表示へ寄せ、不要な宣伝文句を削除する。
* 変更範囲: `themes/shima-island/templates/index.html`, `themes/shima-island/static/css/main.css`, `docs/agent/logs/`。`base.html` や設定ファイルは原則変更しない。
* 前提: Pico.css は継続利用。URL構造と既存機能（記事リンク、メタ情報表示）は維持。
* 手順: 1) index から Welcome/紹介見出し除去 2) 一覧の見出しと行構造をリスト寄りへ調整 3) CSSを枠/カード/装飾なしに再調整 4) ruff/build 検証 5) postflight 記録。
* 検証コマンド: `uv run ruff check .` / `uv run pelican content -o output -s publishconf.py`
* 相談が必要な点: 依存追加・SITEURL変更・大規模構造変更は実施しない。
