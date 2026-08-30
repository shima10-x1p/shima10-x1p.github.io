# Personal site

Pelican、Markdown、Jinja2で作る小さな個人サイトです。生成先の `output/` はGit管理せず、GitHub ActionsからGitHub Pagesへ公開します。

## 初期設定

次の仮情報を自分の内容へ差し替えてください。

- `pelicanconf.py` 冒頭の名前、コピーライト年、紹介文、所在地、プロフィール画像、興味タグ、外部リンク
- `content/pages/about.md` のプロフィール本文
- `publishconf.py` と `content/extra/CNAME` の公開URL・カスタムドメイン
- `content/articles/` のサンプル記事（不要なら削除）

Aboutページのタグは `pelicanconf.py` の `ABOUT_INTERESTS` へ追加・削除・並べ替えを行うと反映されます。プロフィール画像は同じファイルの `PROFILE_AVATAR_URL` で変更できます。

カスタムドメインを使わない場合は `content/extra/CNAME` を削除し、`pelicanconf.py` の `EXTRA_PATH_METADATA` から対応する設定を外してください。`publishconf.py` の `SITEURL` には実際のGitHub Pages URLを指定します。

## 記事を追加する

`content/articles/` にMarkdownファイルを追加します。

```markdown
Title: 記事タイトル
Slug: article-slug
Date: 2026-08-30 09:00
Summary: 記事の短い説明。

ここから本文です。
```

言語名付きコードフェンス（例：<code>```python</code>）は、言語名、シンタックスハイライト、行番号付きで表示されます。

## ローカル確認

```sh
uv sync --locked
uv run pelican content -s pelicanconf.py --autoreload --listen
```

ブラウザで <http://localhost:8000/> を開きます。

## ビルド

```sh
uv run pelican content -s pelicanconf.py
```

公開用URLを埋め込む場合は、次を実行します。

```sh
uv run pelican content -s publishconf.py
```

## 公開

GitHubのリポジトリ設定で Pages の Source を **GitHub Actions** に設定し、`main` ブランチへpushします。`.github/workflows/pages.yml` がロック済み依存関係でビルドし、`output/` をGitHub Pagesへデプロイします。
