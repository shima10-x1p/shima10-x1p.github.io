Title: GitHub Copilot の カスタムエージェントの整理
Date: 2026-02-11 23:43
Slug: github-copilot-workflow
Category: GitHub Copilot
Summary: GitHub Copilot の カスタムエージェントを今更使ってみたので...

GitHub Copilot の カスタムエージェントを今更使ってみたので整理。

## ざっくり整理
![今の段階で考えた流れ](/images/2026/02/github-copilot-workflow/copilot-flow.drawio.png)

ざっくりこんな流れで、それぞれ用のカスタムエージェントを作っていい気がする。
(これはまだ整理中)

---

## YAMLフロントマター
カスタムエージェントの YAML フロントマターは以下のような感じ。
handoffs で他のエージェントに渡すことができる。
```yaml
name: Python Implement
description: 承認済みPlanまたはタスク分割に沿ってPython実装を行い、検証して報告する
argument-hint: 承認済みの Plan（または docs/agent/tasks/index.md などの参照）＋受け入れ条件＋検証手順（コマンド/手動確認）
target: vscode
user-invokable: true
disable-model-invocation: false
tools: ['agent', 'read', 'search', 'edit', 'execute', 'execute/getTerminalOutput', 'execute/testFailure', 'web', 'vscode/askQuestions', 'todo']
agents: []
handoffs:
  - label: 計画に戻る
    agent: Plan
    prompt: 実装中に見つかった点を踏まえてPlanを更新してください
    send: true

  - label: タスク分割に戻る
    agent: Task Breakdown
    prompt: 実装中に見つかった点を踏まえてタスク分割を更新してください
    send: true

  - label: 作業報告をdocsに書き出す
    agent: agent
    prompt: createDirectory docs/agent/walk-through. createFile 作業報告をフロントマターなしのMarkdownとして次に作成してください。`docs/agent/walk-through/walk-through-${camelCaseName}.md`
    send: true
    showContinueOn: false
```

![handoff先の選択肢](/images/2026/02/github-copilot-workflow/select-button.png)
こんな感じで、複数定義すればその分選択肢が出てくる。
