#### Preflight
* 目的: GitHub Pages で公開中の個人ホームページを、Python + Pelican による静的生成へ段階的に移行するための最小で安全な土台を整える。
* 変更範囲: 既存の Pelican 設定・コンテンツ最小構成・README/ドキュメント・GitHub Actions 設定の確認と必要最小限の修正。`output/` は変更しない。既存の運用方針（Actions デプロイ、CNAME）は維持する。
* 前提: 公開URLは `https://www.shima10-x1p.net`、`CNAME` は `www.shima10-x1p.net`、言語は `ja`、タイムゾーンは `Asia/Tokyo`。依存追加・削除や `SITEURL` 変更は原則行わない。
* 手順:
  1. リポジトリ現状（Pelican 構成、Pages デプロイ方式、既存資産）を確認して要点を整理する。
  2. 最小構成として不足しているコンテンツまたはテーマ要素のみを追加する。
  3. ローカルプレビュー/ビルドコマンドが通るように調整する。
  4. `ruff` と Pelican ビルドを実行して成功を確認する。
  5. Postflight を作成し、変更理由・影響範囲・再現手順を記録する。
* 検証コマンド:
  * `uv run ruff check .`
  * `uv run pelican content -o output -s pelicanconf.py`
  * `uv run pelican content -o output -s publishconf.py`
* 相談が必要な点: 依存追加/削除や `SITEURL` 変更が必要になった場合は、理由と影響範囲を提示して事前確認する。
