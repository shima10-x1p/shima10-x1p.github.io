#### Postflight
* 変更内容: 記事本文のレイアウト崩れ対策として、グリッド子要素の `min-width: 0` と、コードブロック（`pre` / `.highlight`）の横スクロール制御を追加。併せて本文画像を `display: block` に調整。
* 変更理由: 長いコード行がある記事で、グリッド項目の最小幅と `pre` のオーバーフロー未制御により横方向へ押し広げが発生しうるため。
* 影響範囲: 記事ページ全体の本文表示。コードスニペットは横スクロールで表示され、画像は本文幅内に収まりやすくなる。URL構造・リンク・SITEURL設定の変更なし。
* 変更ファイル一覧:
  * `themes/shima-island/static/css/main.css`
  * `docs/agent/logs/pre-flight/20260212_000513_article-layout-fix.md`
  * `docs/agent/logs/post-flight/20260212_000653_article-layout-fix.md`
* 実行したコマンドと結果:
  * `uv run pelican content -o output -s publishconf.py` : 成功（2 articles を処理）
  * `uv run ruff check .` : 成功（All checks passed）
* 確認方法:
  * `uv run pelican --listen` でローカル起動し、`/articles/2026/02/github-copilot-workflow/` と `/articles/2026/02/homepage-renewal-bootstrap/` を開いて本文の横崩れがないことを確認。
* 残タスク: 必要なら長い1行コードを含む記事で追加の表示確認を実施。
