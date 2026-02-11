#### Preflight
* 目的: 記事ページ（`homepage-renewal-bootstrap`）で発生しているレイアウト崩れの原因を特定し、`themes/shima-island/templates/article.html` のスタイルを最小修正して崩れを防ぐ。
* 変更範囲: `themes/shima-island/templates/article.html` とログファイルのみ。`content/` の記事本文や公開URL/SITEURL設定は変更しない。
* 前提: SITEURL や公開URL構造（`/articles/YYYY/MM/article-slug/`）は現状維持。言語・タイムゾーン設定には触れない。
* 手順: （1）テンプレートと問題ページ出力を確認（2）崩れの主因（画像/コードブロック/横幅）を特定（3）テンプレートCSSを最小修正（4）ビルド実行（5）結果確認とPostflight作成。
* 検証コマンド: `uv run pelican content -o output -s publishconf.py`, `uv run ruff check .`
* 相談が必要な点: 依存関係追加・SITEURL変更・大規模構成変更は行わない前提のため現時点なし。
