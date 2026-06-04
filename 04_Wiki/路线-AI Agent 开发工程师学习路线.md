---
created: 2026-06-04
tags: [学习路线, AI, Agent, LangChain, RAG, Python]
status: 🚧 进行中
---

# 🧭 AI Agent 开发工程师 — 从小白到面试

## 目标岗位画像

> **Python · LangChain · RAG · 全栈开发 · LLM 应用开发**
> 核心：基于大语言模型的 AI Agent 开发，包括工具链（如 LangChain）和检索增强生成（RAG）

---

## 📊 你的起点

| 已有基础 | 说明 |
|---------|------|
| ✅ **C 语言基础** | 物联网254 课程学过循环、数组、函数 |
| ✅ **网页基础** | 网页设计课程 |
| ✅ **Agent 实践认知** | ima 知识库已有 8 篇 Agent 笔记（多智能体协同、主提示词设计等） |
| ✅ **AI 工具使用** | Claude Code、Cursor 等 |
| ❌ **待补** | Python 全栈、LangChain、RAG、部署工程化 |

---

## 🗺️ 四阶段路线总览

```
底层机制 ──→ LangChain+RAG ──→ Agent工程 ──→ 项目+面试
  2周           2-3周            2-3周           2-3周
```

| 阶段 | 时间 | 核心产出 |
|:----|:----:|:---------|
| 🏗️ **阶段一：底层机制** | 第 1-2 周 | Python 全栈基础 + 手写 minimal Agent |
| 🔗 **阶段二：LangChain + RAG** | 第 3-5 周 | 企业级 RAG 系统 + FastAPI 服务 |
| 🤖 **阶段三：Agent 工程化** | 第 6-8 周 | Agent + MCP + LangGraph + 可观测性 |
| 🚀 **阶段四：项目 + 面试** | 第 9-11 周 | 2 个完整项目 + 简历 + 八股文 |

---

## 🏗️ 阶段一：底层机制（第 1-2 周）

> **目标**：不依赖框架，从头理解 Agent 和 LLM 的工作方式

### 第 1 周：Python 全栈补强

| 天 | 内容 | 资源 |
|:-:|------|------|
| 1-2 | Python 异步编程 `async/await`、`asyncio` | [官方文档](https://docs.python.org/3/library/asyncio.html) |
| 3 | FastAPI 路由、Pydantic 校验、异步接口 | [FastAPI 教程](https://fastapi.tiangolo.com/zh/) |
| 4-5 | 装饰器、面向对象、类型注解进阶 | [Python 教程](https://docs.python.org/3/tutorial/) |
| 6-7 | **产出：** 用 FastAPI 搭建一个「Hello World」API + 一个简单的文件上传解析接口 | — |

### 第 2 周：LLM API + 手写 minimal Agent

| 天 | 内容 | 资源 |
|:-:|------|------|
| 1 | LLM API 调用（OpenAI / Claude），理解 Prompt、Temperature 等参数 | 各模型官方文档 |
| 2 | **Prompt Caching**（2026 必考！）— KV Cache 原理、TTL、成本影响 | [Anthropic Prompt Caching](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching) |
| 3 | ReAct 循环原理：Thought → Action → Observation | [ReAct 论文](https://arxiv.org/abs/2210.03629) |
| 4 | **手写 50 行 minimal Agent**：直接调 API，自己拼 messages 数组，实现 Calculator + Web Search 两个工具 | 🔥 **关键产出** |
| 5 | Context Window 四大坑：Lost in the Middle / Context Rot / 死循环 / 早停 | [Anthropic 文档](https://docs.anthropic.com/en/docs/build-with-claude/context-windows) |
| 6-7 | **整合产出：** FastAPI + 手写 Agent 搭建一个简单的问答 API | — |

> 💡 **学习资源推荐**
> - [牛客网 2026 Agent 学习路线文章](https://www.nowcoder.com/discuss/879367411529506816) — 必读！底层视角一流
> - [ai-agents-from-zero](https://github.com/didilili/ai-agents-from-zero) — 2026 最系统的中文 Agent 教程
> - [Datawhale easy-langent](https://github.com/datawhalechina/easy-langent) — 适合小白入门

---

## 🔗 阶段二：LangChain + RAG（第 3-5 周）

> **目标**：掌握 LangChain 框架 + 搭建生产级 RAG 系统

### 第 3 周：LangChain 核心

| 天 | 内容 | 资源 |
|:-:|------|------|
| 1 | LangChain 六大核心模块：Model I/O、Retrieval、Chains、Memory、Agents、Callbacks | [LangChain 官方文档](https://python.langchain.com/docs) |
| 2 | **LCEL（LangChain Expression Language）** — `管道操作符` 链式组合 | [LCEL 教程](https://python.langchain.com/docs/how_to/#lcel) |
| 3 | Document Loaders + Text Splitters（PDF/MD 加载、分块策略） | [langchain-from-zero](https://github.com/it-worker-tango/langchain-from-zero) — 21 章中文教程 |
| 4 | Embeddings + Vector Stores（Chroma/FAISS 本地快速上手） | — |
| 5 | **手撕 Naive RAG**：30 分钟从零搭建文档问答系统 | 🔥 **关键产出** |
| 6-7 | **整合产出：** LangChain + Chroma + FastAPI 构建"迷你知识库问答 API" | — |

### 第 4 周：高级 RAG + 向量数据库

| 天 | 内容 | 资源 |
|:-:|------|------|
| 1 | **Advanced RAG 技术栈**：Query Transformation、HyDE、Multi-Query | [LlamaIndex](https://docs.llamaindex.ai) |
| 2 | **混合检索**：BM25（稀疏）+ Dense（稠密）Hybrid Search | [Milvus 混合检索](https://milvus.io/docs/hybrid_search.md) |
| 3 | **Reranker 重排序**：BGE-Rerank / Cohere Rerank 提升精度 | — |
| 4 | **RAG 评估**：RAGAS / TruLens 自动化评估管线 | [RAGAS](https://docs.ragas.io) |
| 5 | **生产级向量数据库**：Milvus 部署 + 索引优化 | [Milvus 文档](https://milvus.io/docs) |
| 6-7 | **完善产出：** 升级到 Hybrid Search + Reranker + Milvus 的知识库问答系统 | — |

### 第 5 周：全栈接合

| 天 | 内容 | 资源 |
|:-:|------|------|
| 1-2 | FastAPI 完整 API 设计（路由、鉴权、错误处理、API 文档） | [FastAPI 进阶](https://fastapi.tiangolo.com/advanced/) |
| 3 | **简单前端**：Streamlit / Gradio 快速搭建演示界面 | [Streamlit](https://streamlit.io) |
| 4 | Docker + Docker Compose 容器化部署 | [Docker 教程](https://docs.docker.com/get-started/) |
| 5 | 异步处理 + 缓存策略（Redis 缓存 LLM 响应） | — |
| 6-7 | **全栈产出：** Docker 化部署的 RAG 问答系统，前端可交互 | 🏆 **里程碑产出** |

> 💡 **学习资源推荐**
> - [LangChain 21 章中文教程](https://github.com/it-worker-tango/langchain-from-zero) — 视频+代码，适合系统学习
> - [ai-agents-from-zero 第04章](https://github.com/didilili/ai-agents-from-zero) — 企业级 RAG 实战
> - 吴恩达 [LangChain for LLM Application Development](https://www.deeplearning.ai/short-courses/) 短课

---

## 🤖 阶段三：Agent 工程化（第 6-8 周）

> **目标**：掌握 Agent 核心框架 + MCP + 可观测性

### 第 6 周：Agent + Tool Calling

| 天 | 内容 | 资源 |
|:-:|------|------|
| 1-2 | **Function Calling 原理**：Tool Schema 定义、参数绑定、错误处理 | [OpenAI Function Calling](https://platform.openai.com/docs/guides/function-calling) |
| 3 | **自定义 Tool 开发**：将 API、数据库查询、计算器封装为 Agent 工具 | — |
| 4 | **LangChain Agent**：ReAct Agent、Multi-Tool 编排 | [LangChain Agent 文档](https://python.langchain.com/docs/how_to/#agents) |
| 5 | **MCP 协议（2026 必学）**：Model Context Protocol 工作原理、与 Function Calling 对比 | [MCP 官方文档](https://modelcontextprotocol.io/) |
| 6 | **动手写 MCP Server**：实现一个自定义 MCP Server（如 Notion/文件系统） | 🔥 **简历亮点** |
| 7 | **整合产出：** 一个拥有 5+ 工具的 Agent 服务 | — |

### 第 7 周：LangGraph + Multi-Agent + 可观测性

| 天 | 内容 | 资源 |
|:-:|------|------|
| 1-2 | **LangGraph 核心**：State / Node / Edge、图状工作流 | [LangGraph 文档](https://langchain-ai.github.io/langgraph/) |
| 3 | **条件分支 + 循环**：人类审核节点、反思-修正循环 | — |
| 4 | **Memory 分层**：短期（Sliding Window + Summary）、长期（向量库）、系统级（RAG） | [Mem0](https://mem0.ai) / [Zep](https://www.zep.ai) |
| 5 | **可观测性**：LangSmith 链路追踪、Prometheus 指标、Grafana 可视化 | [LangSmith](https://smith.langchain.com) |
| 6-7 | **整合产出：** LangGraph + LangSmith 构建的可观测 Agent 工作流 | — |

### 第 8 周：性能优化 + 生产化

| 天 | 内容 |
|:-:|------|
| 1 | **Prompt Caching 深度实战**：Cache Breakpoints、TTL 策略、成本建模 |
| 2 | **Token 优化**：上下文压缩、主动剪枝、分级缓存 |
| 3 | **并发控制**：Rate Limiting、Batching、异步流式输出 |
| 4 | **容错设计**：重试机制、熔断器、降级策略 |
| 5-6 | **Docker 部署 + CI/CD**：自动化测试、镜像构建、部署脚本 |
| 7 | **系统产出：** 完整的、可部署的 Agent 生产系统 | 🏆 **里程碑产出** |

> 💡 **学习资源推荐**
> - [ai-agents-from-zero 第03章](https://github.com/didilili/ai-agents-from-zero) — LangChain/LangGraph/MCP
> - [easy-langent](https://github.com/datawhalechina/easy-langent) — Datawhale 5 周系统教程
> - [AgentGuide 学习路线](https://github.com/adongwanai/AgentGuide) — 8 周完整计划

---

## 🚀 阶段四：项目实战 + 面试准备（第 9-11 周）

> **目标**：2 个能写进简历的完整项目 + 面试硬实力

### 项目方向选择

#### 🔥 推荐项目一：企业级智能客服 RAG 系统

| 维度 | 内容 |
|:----|:------|
| **业务场景** | 某场景的智能问答系统，自动回答 80% 重复性用户问题 |
| **技术栈** | FastAPI + LangChain + Milvus + Redis + Docker |
| **核心功能** | 混合检索（BM25+向量）、Reranker 重排序、缓存优化、对话记忆 |
| **量化指标** | 准确率 > 85%、P99 延迟 < 500ms、QPS > 100 |

#### 🔥 推荐项目二：自动化 Agent 系统

| 维度 | 内容 |
|:----|:------|
| **业务场景** | 自动化任务处理 Agent（数据分析 / 代码生成 / 报告撰写） |
| **技术栈** | LangGraph + MCP + LangSmith + FastAPI |
| **核心功能** | 多工具编排、反思-修正循环、MCP Server、人机审核 |
| **量化指标** | 自动化率 > 80%、成功率 > 95%、效率提升 > 3x |

### 第 9-10 周：项目开发

```
第9周：项目一（需求分析 → 架构设计 → 核心开发 → 优化部署）
第10周：项目二（需求分析 → Agent 设计 → 工具开发 → 工作流实现）
```

### 第 11 周：面试冲刺

| 天 | 内容 | 资源 |
|:-:|------|------|
| 1-2 | **简历撰写**（开发岗 STAR 格式） | [ai-agent-interview-guide 简历模板](https://github.com/bcefghj/ai-agent-interview-guide) |
| 3-4 | **八股文突击**（9 大模块 200+ 题） | 同上仓库 01-面试八股文/ |
| 5 | **系统设计题**：高并发 RAG、Agent 自动化系统、Multi-Agent 协作 | — |
| 6 | **项目面试稿**：STAR 法则准备、追问应对 | — |
| 7 | **模拟面试**：1v1 Mock | — |

> 📘 **面试必刷资源**
> - [ai-agent-interview-guide](https://github.com/bcefghj/ai-agent-interview-guide) — 200+ 八股文 + STAR 模板 + 简历模板
> - [AgentGuide 面试题库](https://github.com/adongwanai/AgentGuide/tree/main/docs) — 系统设计题

---

## 🛠️ 推荐技术栈汇总

```
┌─────────────────────────────────────────────┐
│               学习技术栈                      │
├─────────────────────────────────────────────┤
│  Language:     Python 3.11+                  │
│  API框架:      FastAPI + Pydantic            │
│  Agent框架:    LangChain + LangGraph         │
│  向量数据库:    Milvus / Chroma / FAISS       │
│  MCP协议:      MCP SDK + 自定义 Server       │
│  可观测性:      LangSmith + Prometheus        │
│  容器化:        Docker + Docker Compose       │
│  缓存:          Redis                         │
│  前端:          Streamlit / Gradio (演示用)   │
│  部署:          腾讯云 / 阿里云 / AutoDL      │
└─────────────────────────────────────────────┘
```

---

## 📚 资源清单（一键直达）

### 🆓 免费开源教程
| 资源 | 说明 | 推荐指数 |
|:-----|:-----|:--------:|
| [ai-agents-from-zero](https://github.com/didilili/ai-agents-from-zero) | 2026 最系统中文 Agent 实战教程 | ⭐⭐⭐⭐⭐ |
| [langchain-from-zero](https://github.com/it-worker-tango/langchain-from-zero) | 21 章 LangChain 中文教程（视频+代码） | ⭐⭐⭐⭐⭐ |
| [easy-langent](https://github.com/datawhalechina/easy-langent) | Datawhale：LangChain+LangGraph 5 周教程 | ⭐⭐⭐⭐ |
| [AgentGuide](https://github.com/adongwanai/AgentGuide) | 8 周 Agent 开发路线图 | ⭐⭐⭐⭐ |

### 📖 面试资源
| 资源 | 说明 | 推荐指数 |
|:-----|:-----|:--------:|
| [ai-agent-interview-guide](https://github.com/bcefghj/ai-agent-interview-guide) | 200+ 八股文 + STAR 模板 + 简历 | ⭐⭐⭐⭐⭐ |
| [牛客网 Agent 学习路线帖](https://www.nowcoder.com/discuss/879367411529506816) | 2026 最新视角 | ⭐⭐⭐⭐⭐ |

### 🎓 官方文档
| 资源 | 说明 |
|:-----|:-----|
| [LangChain 官方文档](https://python.langchain.com/docs) | 权威参考 |
| [LangGraph 文档](https://langchain-ai.github.io/langgraph/) | 状态机工作流 |
| [MCP 官方文档](https://modelcontextprotocol.io/) | 2026 Agent 通信标准 |
| [Anthropic Prompt Caching](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching) | 2026 必考知识点 |

---

## 📈 每日打卡追踪

### 周次进度
- [ ] **阶段一**：第 1-2 周 —— Python 全栈 + 手写 Agent
- [ ] **阶段二**：第 3-5 周 —— LangChain + RAG
- [ ] **阶段三**：第 6-8 周 —— Agent 工程化
- [ ] **阶段四**：第 9-11 周 —— 项目 + 面试

### 关键里程碑
- [ ] 🏁 **M1**：手写 50 行 minimal Agent（不依赖框架）
- [ ] 🏁 **M2**：搭建一个完整的 RAG API 服务（Docker 部署）
- [ ] 🏁 **M3**：完成 LangGraph Agent 工作流 + LangSmith 监控
- [ ] 🏁 **M4**：2 个完整项目上线 + 简历定稿
- [ ] 🏁 **M5**：模拟面试通过（八股文 + 系统设计）

---

> **关联笔记：**
> - [[30.areas/ima-知识库/03-AI与技术/主智能体提示词]] — 你已有的 Agent 提示词设计
> - [[30.areas/ima-知识库/03-AI与技术/笔记-非最新仅参考-多智能体协同-长时工作设计]] — 多 Agent 协同经验
> - [[30.areas/ima-知识库/03-AI与技术/Hermes Agent 进阶：三大隐藏技能]] — Hermes Agent 实战
> - [[HOME/知识库驾驶舱]] — 回到总驾驶舱
