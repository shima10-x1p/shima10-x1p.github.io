#### Postflight
* 変更内容: `content/images` を静的配信対象に追加し、記事サムネイル解決フィルターを `pelicanconf.py` に実装。`index.html` と `article.html` でサムネイル表示を追加し、CSSで一覧/記事上部/本文画像のリサイズ表示を調整。サンプル画像配置とサンプル記事本文画像を追加。
* 変更理由: 記事ごとの画像管理を `content/images/YYYY/MM/<slug>/` で統一し、一覧と記事詳細で同一ルールのサムネイル表示を実現するため。
* 影響範囲: `index.html` と記事詳細ページ上部に画像が表示される。サムネイル未設定記事は一覧で既存プレースホルダー継続、記事詳細は非表示。公開URL構造と `SITEURL` は変更なし。
* 変更ファイル一覧:
  * `pelicanconf.py`
  * `themes/shima-island/templates/index.html`
  * `themes/shima-island/templates/article.html`
  * `themes/shima-island/static/css/main.css`
  * `content/articles/2026/02/homepage-renewal-bootstrap.md`
  * `content/images/2026/02/homepage-renewal-bootstrap/thumbnail.gif`
  * `docs/agent/logs/pre-flight/20260208_185141_article-image-support.md`
  * `docs/agent/logs/post-flight/20260208_185334_article-image-support.md`
* 実行したコマンドと結果:
  * `uv run ruff check .` : 成功（All checks passed）
  * `uv run pelican content -o output -s pelicanconf.py` : 成功（1記事を処理）
  * `find output/images -maxdepth 5 -type f | sort` : `output/images/2026/02/homepage-renewal-bootstrap/thumbnail.gif` を確認
  * `rg -n "post-thumbnail-image|article-thumbnail|thumbnail.gif" output/index.html output/articles/2026/02/homepage-renewal-bootstrap/index.html` : 一覧と記事詳細でサムネイル参照を確認
* 確認方法:
  * `uv run pelican --listen` でローカル起動
  * `/` の記事一覧でサムネイル表示を確認
  * `/articles/2026/02/homepage-renewal-bootstrap/` で記事上部サムネイルと本文画像の表示崩れがないことを確認
* 残タスク: 実運用画像（実寸・最適化済み）の差し替え。必要なら `Thumbnail:` 明示指定パターンの記事も追加して運用ルールを検証。
