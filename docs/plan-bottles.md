# ボトルメール機能 実装プラン

## 概要

スクラップのような「短い投稿をスレッド形式で連ねる」機能を、
Pelican カスタムジェネレータープラグインで実現する。

名称: **ボトルメール**

---

## コンテンツ構造

```
content/bottles/{slug}/
  meta.md     ← スレッド全体のメタ情報
  001.md      ← 個別投稿（時系列順）
  002.md
  ...
```

### meta.md のフロントマター

```markdown
Title: Pelican Tips まとめ
Date: 2026-04-12
Tags: pelican, python
Slug: pelican-tips
```

- `Title`: スレッドのタイトル
- `Date`: スレッド作成日
- `Tags`: スレッド全体のタグ（任意）
- `Slug`: URL に使用（フォルダ名と一致させる）

### 個別投稿 (001.md, 002.md, ...) のフロントマター

```markdown
Date: 2026-04-12 14:30
Tags: pelican
```

- `Date`: 投稿日時（必須）
- `Tags`: 投稿固有のタグ（任意）
- 本文は通常の Markdown

---

## URL 構造

| ページ | URL |
|--------|-----|
| 一覧 | `/bottles/` |
| 個別スレッド | `/bottles/{slug}/` |

---

## 生成ファイル

| 出力パス | 内容 |
|----------|------|
| `output/bottles/index.html` | ボトルメール一覧 |
| `output/bottles/{slug}/index.html` | スレッドページ |

---

## プラグイン

**ファイル:** `plugins/bottles.py`

### 処理フロー

1. `content/bottles/` 配下のサブフォルダを走査
2. 各フォルダから `meta.md` を読み込み → スレッドメタ情報を取得
3. `*.md`（meta.md 以外）をファイル名順にソートして読み込み
4. Markdown → HTML 変換（Pelican の Reader を利用）
5. スレッドごとにコンテキストを組み立て
6. テンプレートでレンダリング → `output/` に書き出し

### Pelican 連携

- `pelican.generators.Generator` を継承したカスタムジェネレーターを定義
- `get_generators` シグナルで登録

---

## テンプレート

### bottles.html（一覧ページ）

```
themes/shima-island-coral/templates/bottles.html
```

- 全スレッドをカード形式で一覧表示
- 各カードにタイトル、作成日、投稿数、最終更新日を表示
- `/bottles/{slug}/` へのリンク

### bottle.html（スレッドページ）

```
themes/shima-island-coral/templates/bottle.html
```

- スレッドタイトル・メタ情報をヘッダーに表示
- 個別投稿を時系列で縦に並べる（タイムライン風）
- 各投稿に日時とタグを表示
- 記事ページとは異なるレイアウト（軽量・コンパクト）

---

## pelicanconf.py の変更

```python
# ボトルメール設定
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["bottles"]

# ナビゲーションに追加
MENUITEMS = (
    ("プロフィール", "/profile/"),
    ("ボトルメール", "/bottles/"),
)
```

---

## CSS

`themes/shima-island-coral/static/css/style.css` にボトルメール用のスタイルを追加。

- タイムライン風のレイアウト（左に線 + 丸ポイント）
- 一覧カードのスタイル
- 記事とは区別できるデザイン

---

## 実装ステップ（MVP）

1. **プラグイン作成** (`plugins/bottles.py`)
   - フォルダ走査・Markdown 読み込み・ページ生成ロジック
2. **テンプレート作成**
   - `bottles.html`（一覧）
   - `bottle.html`（スレッド）
3. **CSS 追加**
   - タイムライン風レイアウト
4. **設定更新** (`pelicanconf.py`)
   - プラグイン登録・ナビゲーション追加
5. **サンプルコンテンツ作成**
   - テスト用のボトルメール 1 件
6. **ビルド・動作確認**

---

## 将来の拡張（MVP 外）

- ボトルメール専用の Atom/RSS フィード
- 投稿数バッジ
- 最終更新日でのソート
- 検索対応
