

## 一句话定义

AI Agent 执行环境是让模型安全调用工具、访问系统、完成任务并留下可复盘记录的一整套运行边界。

## 我当前的理解

Agent 的能力不只由模型决定，还由它能进入哪些系统、能调用哪些工具、权限如何限制、失败如何回滚、人类如何确认、过程是否可追踪共同决定。

从 2026-06-02 的信息看，OpenAI Codex 进入 Amazon Bedrock、Microsoft 的 MagenticLite、Anthropic 的 Claude Code 沙箱实践、浏览器端 Pyodide 应用都指向同一件事：AI 正在从“回答问题”变成“在真实执行环境中做事”。执行环境越接近真实系统，安全边界和过程留痕越重要。

## 关键概念

- 工具权限：Agent 可以读写哪些文件、访问哪些 API、执行哪些命令。
- 沙箱隔离：用容器、虚拟机、系统沙箱或浏览器隔离风险操作。
- 人类确认：高风险动作执行前需要审批或确认。
- 过程留痕：记录提示词、工具调用、代码修改、测试结果和失败原因。
- 回滚能力：错误修改必须能定位、撤回或隔离。

## 可复用方法

- 评估 Agent 项目时，不只看 demo，还要看权限模型、日志、失败处理和人工确认。
- 给个人项目接入 AI 自动化时，先限定最小权限，再逐步放开工具。
- 对代码类 Agent，保留“需求、决策、修改、验证、回滚”的轨迹，便于复盘和解释贡献。
- 对浏览器或本地文件系统 Agent，优先选择有沙箱、人类审批和清晰日志的方案。

## 典型场景

- Codex/Claude Code 参与真实代码库开发。
- 浏览器 Agent 自动检索、填表、下载和整理资料。
- 本地知识库 Agent 读取 Obsidian 并写回 Wiki/项目页。
- 企业把 coding agent 接入云平台、CI/CD 和权限治理系统。

## 与我的项目的关系

- `Horizon 信息雷达`：需要把每日抓取、分析、失败降级和人工补检索做成可追踪流程。
- `校园服务小程序`：未来如加入 AI 助手，应优先考虑权限、隐私和用户确认，而不是直接自动操作。
- `个人作品集网站`：可以展示“AI 自动化工作流如何安全运行”的工程能力。

## 已确认事实

- 2026-06-02 日报记录了 OpenAI/Codex on AWS、MagenticLite、Claude Code 动态工作流、Pyodide ASGI 浏览器应用等相关信息。
- `microsoft/magentic-ui` 是跨浏览器和本地文件系统的实验性 Agent UI。
- `entireio/cli` 的方向是把 AI agent 会话和 Git 工作流绑定，形成可搜索的开发过程记录。
- 2026-06-04 日报新增判断：Agent 工程栈正在进入“资产治理”阶段，MCP server、浏览器自动化、本地文件访问都应纳入权限、日志和人工确认机制。
- 2026-06-05 日报新增判断：本地 Agent、AI 桌面应用和 MCP server 应被当作可注册、可审计、可限权的资产；Agent 记忆系统也需要来源、过期、检索和删除机制，不能只追求“记得更多”。
- 2026-06-07 日报新增判断：AI coding agent 的高风险面经常不是模型本身，而是它持有的 refresh token、API key、本地配置和第三方 UI/包管理器链路；因此 Agent 运行环境必须把凭证最小化、包来源校验、网络外连日志和异常撤销流程作为默认要求。
- 2026-06-08 日报新增判断：凭证治理是 Agent 执行环境的一部分，而不是独立杂项。API key、AppSecret、refresh token、订阅消息模板密钥等不应写入 Obsidian 普通笔记、截图、公开仓库或可同步 Markdown；应迁移到环境变量、系统凭据管理器、受控 secret manager 或至少本地未同步的 `.env`，并用 Gitleaks、TruffleHog、ggshield 等工具做提交前扫描。
- 2026-06-09 日报新增判断：Agent 执行环境还需要红队评测与失败模式回归测试。对 RAG、coding agent、浏览器 agent 和校园服务 AI 助手，应该用 promptfoo、garak、PyRIT 等工具测试提示注入、越权工具调用、敏感信息泄漏、不安全输出和异常恢复，而不是只验证“正常任务能跑通”。

## 待验证问题

- MagenticLite 的小模型 Agent 方案在本地环境中的实际可用性如何。
- `entireio/cli` 是否适合融入个人项目开发流程，还是只适合大型团队审计。
- Horizon pipeline 的 AI 分析阶段是否需要沙箱、任务队列或更细粒度的失败恢复。
- `memU`、`engram` 这类 Agent 记忆系统是否能补足 Obsidian 写回机制，还是会制造重复记忆和来源混乱。
- promptfoo、garak、PyRIT 哪个最适合作为个人 Agent/RAG 项目的第一套安全评测工具。

## 资料来源

- `每日蒸馏·/2026-06-02.md`
- `Horizon/data/summaries/horizon-2026-05-31-zh.md`
- https://openai.com/index/openai-frontier-models-and-codex-are-now-available-on-aws/
- https://www.microsoft.com/en-us/research/blog/magenticlite-magenticbrain-fara1-5-an-agentic-experience-optimized-for-small-models/
- https://www.anthropic.com/news/claude-opus-4-8
- https://github.com/microsoft/magentic-ui
- https://github.com/entireio/cli
- https://github.com/promptfoo/promptfoo
- https://github.com/NVIDIA/garak
- https://github.com/microsoft/PyRIT

## 更新记录

- 2026-06-02：由每日蒸馏写回，建立初版共识。
- 2026-06-04：补充 Microsoft Build 2026 安全治理与 Anthropic 自动化攻击案例带来的判断：Agent 能力越接近真实系统，越需要默认最小权限、过程留痕和高风险动作确认。
- 2026-06-05：补充本地 Agent 治理与长期记忆判断：本地运行、MCP、桌面应用、文件访问和记忆库都应纳入权限、日志、来源和可删除机制。
- 2026-06-07：补充 Agent 凭证与工具链攻击面判断：第三方 Codex/Claude/OpenClaw 类 UI、npm 包和本地 token 文件需要纳入安全检查，不能只关注模型能力。
- 2026-06-08：补充凭证治理判断：个人 Agent 工作流也需要 secret 扫描、密钥轮换和占位符记录，不能把真实 API key 当作普通知识材料保存。
- 2026-06-09：补充 Agent 红队评测判断：执行环境不仅要有权限、凭证和日志，还要有面向提示注入、越权调用、敏感信息泄漏和失败恢复的安全回归测试。
