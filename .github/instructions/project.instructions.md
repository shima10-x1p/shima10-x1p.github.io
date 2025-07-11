---
applyTo: '**'
---
# GitHub Copilot Agent Instructions: 個人ホームページ初期構築

## 🎯 ゴール

* **React (Vite + TypeScript)**、**Tailwind CSS**、**shadcn/ui** を用いて“まっさら”なプロジェクトを作成する
* トップページに **ナビゲーションバー・メインコンテンツ・フッター** を配置し、メインにサンプルテキストとサンプルボタンを表示する

## 🗺️ 全体ワークフロー

1. **PLAN** – 具体的手順を Issue に下書きし、`approved` ラベルが付くまで待機
2. **BUILD** – 承認後に以下を実行（既存リポジトリ直下で作業）

   1. プロジェクト雛形を現在のディレクトリに生成

      ```bash
      npm create vite@latest . -- --template react-ts --force
      ```
   2. 依存パッケージをインストール

      ```bash
      pnpm add -D tailwindcss postcss autoprefixer @tailwindcss/vite
      pnpm add lucide-react clsx
      pnpm dlx shadcn@latest init
      ```
   3. Tailwind 設定 (`tailwind.config.ts`, `postcss.config.js`) と `src/index.css` を用意
   4. `vite.config.ts` を編集（デフォルト `base: "/"` で可）
   5. UI 実装

      * `src/components/navbar.tsx`：簡易ナビゲーションバー（サイト名とリンク）
      * `src/components/footer.tsx`：コピーライト表記のみ
      * `src/pages/home.tsx`：`<h1>` + サンプルテキスト + shadcn/ui `<Button>` を中央配置
      * `src/App.tsx` にて上記を配置
3. **REPORT** – 実施内容をまとめた Pull Request を作成し、レビュアーをタグ付け

## 🛡️ 制約

* `main` への強制 push を禁止
* **セマンティックコミットメッセージ** を使用（例: `feat: add navbar`）
* 機密情報はコミットしない

## 📦 成果物

* リポジトリ直下のソースコード
* `Initial site scaffold` というタイトルの Pull Request

## ✅ チェックリスト

* `pnpm dev` でローカルサーバが起動し、ページが表示される
* ナビゲーションバー・メイン・フッターがレイアウト崩れなく表示される
* shadcn/ui のボタンがクリック可能

---
