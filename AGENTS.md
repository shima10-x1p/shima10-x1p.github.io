# AGENTS.md

## 目的
このリポジトリは、Python + Pelican を使用して GitHub Pages 上で静的なウェブサイトを公開するためのものです。

## 技術スタック
* Python 3.14
* Pelican 4.11.0.post0
* GitHub Pages
* Markdown
* Jinja2 Template Engine
* Pico CSS (pico.css)

## コマンド
* パッケージ管理: uv
    uv --help, uv {command} --help などでヘルプを参照できる。
* 静的サイト生成: pelican
    uv run pelican --help でヘルプを参照できる。
* ローカルサーバー起動: pelican --listen
    uv run pelican --listen でローカルサーバーを起動できる。
* 品質チェック: ruff
    uv run ruff check . でコードの品質チェックを実行できる。
    uv run ruff format . でコードの自動整形を実行できる。

## ディレクトリ構成
repository_root/
├── content/                    # コンテンツ（Markdownファイルなど）
|   └── articles/               # 記事コンテンツ
|       └── 2026/               # 2026年の記事
|           └── 01              # 1月の記事
|               └── {記事}.md   # 記事ファイル
├── themes/                     # カスタムテーマ
|   └── shima-island/           # カスタムテーマのディレクトリ
├── CNAME                       # カスタムドメイン設定ファイル
├── main.py                     # Pelican設定ファイル
├── pelicanconf.py              # Pelican設定ファイル
├── publishconf.py              # 公開用Pelican設定ファイル
├── pyproject.toml              # パッケージ管理設定ファイル
├── uv.lock                     # パッケージ管理ロックファイル
└── AGENTS.md                   # このドキュメント

## プロジェクトの前提
* コンテンツ: Markdown 形式で作成され、`content/` ディレクトリに配置される。`content/articles/YYYY/MM` 以下に各年月ごとになるよう記事を整理する。
  * 公開するときのURL構造は `https://yourdomain.com/articles/YYYY/MM/article-slug/` となるようにする。
* テーマ: カスタムテーマは `themes/` ディレクトリに配置される。Pico CSS をベースにしたシンプルでレスポンシブなデザインを採用する。
* デプロイ: GitHub Actions を使用して、`main` ブランチへのプッシュ時に自動的にサイトをビルドし、GitHub Pages にデプロイする。
* ドメイン: カスタムドメインを使用する場合、`CNAME` ファイルにドメイン名を記載する。
* Pelican カスタムテーマ: `themes/shima-island/` に配置される。Pico CSS をベースにしたテーマを使用し、必要に応じてカスタマイズする。動作するために最低限のテンプレートのみを作成すること。(base.html, article.html, index.html など)

## 開発ルール
* コード品質: `ruff` を使用してコード品質をチェックする。コミット前に `uv run ruff check .` を実行し、問題があれば修正する。
* コミットメッセージ: 一貫性を保つため、コミットメッセージは簡潔かつ具体的に記述する。(例: "feat: 新しい記事の追加", "fix: レイアウトの修正", "docs: ドキュメントの更新" など)
* ブランチ戦略: `main` ブランチは常にデプロイ可能な状態を保つ。新機能や修正は別ブランチで行い、プルリクエストを通じて `main` にマージする。
* テスト: 主要な変更を加える場合は、ローカルでサイトをビルドし、動作確認を行うこと。
* コマンドや設定の追加は、必要最小限にする。増やしたらこの AGENTS.md も更新すること。

## GitHub Pages デプロイ
* デプロイは GitHub Actions を前提にします。
* 目安: `.github/workflows/pelican.yml` がサイト生成と Pages への公開を担当します。
* デプロイ方式を変える提案をする場合は、必ず理由と影響範囲を先に説明します。

## 境界
### Always: 常にやる
* 変更後にビルドを通し、成功したコマンドと結果を報告します。
* 触ったファイル一覧を最後に列挙します。

## Ask: 事前に確認する
* 依存関係の追加、削除
* 公開 URL や `SITEURL` を含む設定変更
* ディレクトリ構造の大規模変更、テーマの全面入れ替え

## Never: やらない
* シークレットやトークンをコミットしない
* 生成物 `output/` を手編集しない
* 意図が不明な大改造を独断で進めない

## 完了条件
* ローカルでプレビューできる
* ビルドが成功する
* 変更内容が説明可能で、差分が目的に対して過剰でない

## 参考
* README.md: 人向けの全体説明
* docs/: 詳細設計やメモがある場合はここ

---

## docsディレクトリについて
docsディレクトリは、このリポジトリに関する詳細な設計情報やメモを格納するための場所です。必要に応じて参照してください。

## docs/agents/reference
このサブディレクトリには、リポジトリの設計や運用に関する参考資料が含まれています。具体的な内容は以下の通りです。

* docs/agents/reference/テーマサンプル
  * 事前に Gemini と対話して練った、Pico CSS ベースのカスタムテーマのサンプル実装。
  * テーマの構造やスタイルの参考として利用できます。
  * このサンプルをベースにしたテーマを作成してください。

---

## 作業ログ（必須）
このリポジトリでは、Codex は作業の前後で必ずドキュメントを残します。
ログは差分と一緒にレビューできるよう、原則コミット対象です。

### ログの作り方（Always）
- 作業開始前に、次のファイルを新規作成する  
  - `docs/agent/logs/pre-flight/<yyyymmdd_HHMMSS>_<task-slug>.md`
- そのファイルに Preflight を書き終えるまで、コード変更をしない
- 作業完了後に、次のファイルへ Postflight を記載して作業完了とする  
  - `docs/agent/logs/post-flight/<yyyymmdd_HHMMSS>_<task-slug>.md`

※ task-slug は短い英数字でOKです（例: homepage-theme-refresh）

### Preflight に必ず書くこと（開始前）
`docs/agent/logs/pre-flight/<yyyymmdd_HHMMSS>_<task-slug>.md` に次のテンプレで記録する。

#### Preflight
* 目的: （何をどうしたいか）
* 変更範囲: （触るディレクトリと触らないディレクトリ）
* 前提: （SITEURL、公開URL、言語、タイムゾーンなど重要な仮定）
* 手順: （最大5ステップで）
* 検証コマンド: （この後に実行するコマンドを列挙）
* 相談が必要な点: （Ask 条件に触れそうならここに書く）

### Postflight に必ず書くこと（完了後）
`docs/agent/logs/post-flight/<yyyymmdd_HHMMSS>_<task-slug>.md` に次のテンプレで記録する。

#### Postflight
* 変更内容: （何を変えたかを短く）
* 変更理由: （なぜそれが必要か）
* 影響範囲: （ユーザーに見える差分、互換性、URL/リンクなど）
* 変更ファイル一覧: （パスを列挙）
* 実行したコマンドと結果: （成功/失敗、要点のみ。長いログは貼らない）
* 確認方法: （レビュー担当が再現できる手順）
* 残タスク: （必要なら）

## 主要コマンド（最初に参照する）
* 依存導入: <例: uv sync / pip install -r requirements.txt>
* ローカルプレビュー: <例: pelican -lr -s pelicanconf.py / make devserver>
* ビルド: <例: pelican content -o output -s publishconf.py>
* 品質チェック: <例: ruff check . && ruff format --check .>

## 境界（Ask）
次は実施前に必ず相談してから進める。
* 依存関係の追加・削除
* 公開URLや SITEURL、フィード設定に影響する変更
* ディレクトリ構造の大規模変更、テーマの全面入れ替え
