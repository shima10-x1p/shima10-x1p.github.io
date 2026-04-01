#### Postflight
* 変更内容: 記事一覧の先頭プロモ文を削除し、`Latest Posts` 見出し + 日付付き縦リストへ調整。カード感/シャドウ/強い枠表現は使わず、細い区切り線中心にした。
* 変更理由: 実運用サイト向けに装飾を削減し、参考イメージに近い静かな一覧トーンへ寄せるため。
* 影響範囲: トップページの記事一覧の見た目が変更。記事リンク・メタ情報・タグ・抜粋・続きを読む導線は維持。URL構造変更なし。
* 変更ファイル一覧:
  - themes/shima-island/templates/index.html
  - themes/shima-island/static/css/main.css
  - docs/agent/logs/pre-flight/20260331_235418_list-style-adjust.md
  - docs/agent/logs/post-flight/20260331_235533_list-style-adjust.md
* 実行したコマンドと結果:
  - `uv run ruff check .` : 成功（All checks passed）
  - `uv run pelican content -o output -s publishconf.py` : 成功（2 articles processed）
* 確認方法:
  1) `uv run pelican --listen` でプレビュー
  2) トップページで先頭紹介文が無いことを確認
  3) 記事一覧が1カラム・細い区切り線・タイトル左/日付右のトーンになっていることを確認
* 残タスク: `Latest Posts` の文言を日本語化したい場合は `index.html` の見出し1行を変更する。
