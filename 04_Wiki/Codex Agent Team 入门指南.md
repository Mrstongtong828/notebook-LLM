---
title: Codex Agent Team 入门指南
aliases:
  - Codex 多 Agent 编程
  - Agent Team 编程范例
tags:
  - codex
  - agent-team
  - ai-programming
  - subagents
created: 2026-06-09
source: C:\Users\tong'tong\Documents\Codex\2026-06-09\agent-team-3-56-3pm-06\outputs\agent-team-codex-guide.md
---

# Codex Agent Team 入门指南

## 这类视频在讲什么

你贴的几条抖音内容，核心都在讲同一件事：不要让一个 AI 从头到尾单线程写代码，而是让主代理像项目负责人一样拆任务，再把独立任务交给多个子代理并行处理。

常见分工是：

- 主代理：理解目标、拆任务、控制写入范围、合并结果、最终验收。
- 研究/架构代理：读代码、查资料、提出方案。
- 前端/后端/数据库/安全/AI 代理：各自负责清晰边界内的实现。
- 测试/审查代理：写测试、跑验证、找风险。

关键不是“代理越多越好”，而是每个代理都要有明确边界，最好不要同时改同一个文件。

## 已安装内容

本工作区已安装项目级 agent 配置：

```text
.codex/agents/
  agent-organizer.toml
  task-distributor.toml
  frontend-developer.toml
  backend-developer.toml
  ui-designer.toml
  test-automator.toml
  code-reviewer.toml
  documentation-engineer.toml
```

来源备份在：

```text
work/awesome-codex-subagents/
```

这套配置来自 GitHub 项目 `VoltAgent/awesome-codex-subagents`。我只挑了入门常用的 8 个角色，避免一次装 130+ 个角色造成选择噪声。

## 最小范例：密码强度评分器

这次演示做了一个很小的 Python 功能：

```python
password_strength.score_password(password: str) -> dict
```

返回：

```python
{"score": int, "label": str, "reasons": list[str]}
```

团队分工：

- 测试工程师子代理：只写 `tests/test_password_strength.py`，不写生产代码。
- 主代理：先确认测试失败，再实现 `password_strength.py`。
- 代码审查子代理：只读实现和测试，找 bug、边界风险、测试缺口。

运行验证：

```powershell
python -m unittest tests.test_password_strength
```

## 你可以直接复制的 Agent Team 提示词

### 通用版

```text
请用 agent team 模式完成这个需求。

主代理职责：
1. 先拆任务，判断哪些任务可以并行，哪些必须自己做。
2. 给每个子代理明确角色、目标、文件范围和输出格式。
3. 子代理之间不要改同一个文件。
4. 子代理完成后，主代理负责审查、整合、运行测试和最终汇报。

需求：
【在这里写你的需求】

建议分工：
- explorer：读代码/查现状/找入口，不改文件。
- worker A：负责后端或核心逻辑，限定文件范围。
- worker B：负责前端或 UI，限定文件范围。
- worker C：负责测试，限定测试文件范围。
- reviewer：最终只读审查，列出阻塞问题和建议。

验收：
- 跑相关测试。
- 汇报每个子代理做了什么。
- 汇报修改文件和剩余风险。
```

### 小项目开发版

```text
请用多 agent 并行开发一个小功能：【功能名称】。

请先让一个 organizer/explorer 帮我拆任务，输出：
- 哪些工作本地做
- 哪些工作交给子代理
- 每个子代理的写入范围
- 等待和合并顺序

然后再启动 worker：
- 测试代理先写测试，不写生产代码。
- 实现代理只改核心代码。
- 文档代理只改 README 或 docs。
- 审查代理最后只读审查。

要求：
- 每个 worker 都要知道自己不是独自在代码库里，不要回退别人改动。
- 并行任务必须文件范围不重叠。
- 主代理最后运行测试并给我中文总结。
```

## 什么时候适合用 Agent Team

适合：

- 一个需求包含前端、后端、测试、文档等多个独立部分。
- 需要同时调研竞品、读代码、写实现、写测试。
- 大项目里需要多个专家从不同角度审查。

不适合：

- 改一行配置。
- 任务强依赖前一步结果，无法并行。
- 多个代理都必须编辑同一个文件，容易冲突。

## 最重要的规则

1. 先拆任务，再开代理。
2. 每个代理只做一个清晰任务。
3. 写入范围要分开。
4. 主代理不要重复子代理的工作。
5. 最后必须验收：读汇报、看改动、跑测试。
