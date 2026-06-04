---
created: 2026-06-04
source: https://github.com/abi/screenshot-to-code
type: GitHub 项目沉淀
tags:
  - AI工具
  - 前端开发
  - 截图转代码
  - 低代码
  - 多模态
---

# screenshot-to-code 截图转代码工具

## 链接

- GitHub: https://github.com/abi/screenshot-to-code
- 本地项目路径: `C:\Users\tong'tong\Documents\Codex\2026-06-03\ps-c-users-tong-tong-codegraph\work\screenshot-to-code`
- 本地访问地址: http://localhost:5173
- 后端地址: http://localhost:7001

## 它可以用来干什么

`screenshot-to-code` 是一个把截图、设计稿、Figma 页面、文字描述或已有网页转换成前端代码的开源项目。它的核心价值是：把“我看到的界面”快速变成“可以运行、可以继续改的前端原型”。

它适合做这些事：

- 把 App / 小程序 / Web 页面截图转成 HTML、Tailwind、React、Vue、Bootstrap、Ionic 等代码。
- 快速复刻一个参考界面，用来做原型、竞品分析、课程作业或设计验证。
- 把 UI 设计图变成第一版前端骨架，之后再人工精修交互、状态和业务逻辑。
- 用文字描述或 URL 作为输入，让 AI 生成一个可预览的页面。
- 对“页面长什么样”先快速落地，再让 Codex / Claude Code 继续做工程化改造。

一句话判断：它不是完整产品生成器，而是“视觉到前端原型”的加速器。

## 输入与输出

支持的输入方式：

- 上传截图
- 输入 URL
- 输入文本描述
- 导入已有代码

支持的输出栈：

- HTML + Tailwind
- HTML + CSS
- React + Tailwind
- Vue + Tailwind
- Bootstrap
- Ionic + Tailwind
- SVG

## 我的本地配置

当前本地使用 Docker 运行：

```powershell
cd "C:\Users\tong'tong\Documents\Codex\2026-06-03\ps-c-users-tong-tong-codegraph\work\screenshot-to-code"
docker compose up -d
```

停止：

```powershell
docker compose down
```

重新构建：

```powershell
docker compose up -d --build backend frontend
```

本地做过的适配：

- 后端 Dockerfile 的 Poetry 安装源改成清华 PyPI 镜像，用来解决容器内访问 PyPI SSL 失败的问题。
- 前端移除了 `vite-plugin-checker`，避免 TypeScript 类型错误遮罩盖住页面。
- 加入了 `deepseek-v4-pro` 到前端模型下拉和后端模型列表。
- 给 DeepSeek 单独接了 OpenAI 兼容的 `/chat/completions` 调用路径，因为原项目 OpenAI 分支默认使用 Responses API。
- `.env` 已配置 DeepSeek OpenAI-compatible API，不在笔记里记录密钥。

## API key 与模型

项目原生支持：

- OpenAI
- Anthropic Claude
- Google Gemini

也可以接入 OpenAI 兼容服务：

```env
OPENAI_API_KEY=你的第三方平台 key
OPENAI_BASE_URL=https://你的服务商地址
```

当前我配置的是 DeepSeek V4 Pro：

```env
OPENAI_BASE_URL=https://api.deepseek.com
```

注意：API key 不应该写进知识库。之前临时测试用的 key 应该后续轮换。

## 适合我的使用场景

### 1. 小程序 / App 原型复刻

看到一个优秀页面，可以截图上传，让它生成 React / HTML / Tailwind 初稿。适合用于：

- 校园服务小程序界面参考
- 打印、预约、表单、列表、卡片页等 UI 快速搭建
- 比赛 demo 的视觉原型

### 2. 设计学习与拆解

可以把优秀页面变成代码，再反向学习：

- 布局层级
- spacing / padding / gap
- 字体大小和颜色
- 卡片、按钮、表单的组件组织方式

### 3. Codex 工作流的前置工具

它负责“从视觉生成第一版代码”，Codex 负责后续：

- 修复样式和响应式问题
- 抽组件
- 接真实数据
- 加交互状态
- 工程化整理

一个理想流程：

1. 用 screenshot-to-code 生成页面初稿。
2. 把生成代码放进真实项目。
3. 让 Codex 按现有项目风格重构。
4. 手工做最后的视觉和交互校准。

### 4. 快速验证产品想法

当还不确定一个页面是否值得做时，可以先用截图/文字描述生成低成本 demo。适合在需求早期判断：

- 页面结构是否合理
- 信息密度是否合适
- 交互入口是否清楚
- 这个想法是否值得继续开发

## 局限

- 生成结果通常只是“看起来像”，不一定有完整业务逻辑。
- 对复杂交互、动效、数据状态、权限流程理解有限。
- 生成代码可能不符合现有项目架构，需要二次整理。
- 如果使用 DeepSeek V4 Pro，它可能不支持图片输入；上传截图路径可能失败，文本或导入代码路径更稳。
- 原项目模型列表偏向 OpenAI / Claude / Gemini，接第三方模型时可能需要改代码。
- 前端原本存在 CodeMirror 依赖类型冲突，当前为了试用先关闭了浏览器错误遮罩。

## 和其他工具的关系

- 与 [[CodeGraph]] 不同：CodeGraph 用来理解已有代码库，screenshot-to-code 用来从视觉生成新代码。
- 与 Codex / Claude Code 不同：它更像“UI 初稿生成器”，不是通用编码 Agent。
- 与 Figma Dev Mode 不同：它不要求源文件结构完整，只要有截图也能试。
- 与 v0 类似：都可以生成前端界面，但 screenshot-to-code 更强调从截图/设计稿反推代码。

## 我的判断

这个项目值得保留在工具链里，但不要期待它一次生成生产级前端。它最适合当作“前端原型启动器”：

- 视觉明确、业务简单时，收益很高。
- 页面复杂、交互很多时，只适合作为参考初稿。
- 如果要做正式项目，后续必须经过人工/Codex 重构。

优先级：中高。适合在小程序、Web demo、比赛原型、课程项目中频繁试用。

## 下一步

- [ ] 用一个真实小程序截图测试 DeepSeek V4 Pro 是否支持图片输入。
- [ ] 如果图片输入失败，改用 Gemini / OpenAI / Claude 这类明确支持视觉的模型。
- [ ] 选一个生成结果较好的页面，沉淀一篇“截图转代码后如何工程化”的流程笔记。
- [ ] 评估是否把它加入自己的常用 AI 前端工具链。

