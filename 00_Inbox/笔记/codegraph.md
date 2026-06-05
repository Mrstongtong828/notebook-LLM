这是一个“给代码库建索引，让 AI/人快速理解代码结构”的工具。你已经装好了，本机版本是 `0.9.7`。

最常用流程是：

```powershell
cd C:\你的项目目录
codegraph init -i
codegraph status
```

然后就可以查代码结构：

```powershell
codegraph files
codegraph query "AuthService"
codegraph query "login" --kind function
codegraph callers "login"
codegraph callees "login"
codegraph impact "UserService"
codegraph context "我要修复登录失败的问题"
```

如果你改了代码，更新索引：

```powershell
codegraph sync
```

如果你想让 Codex / Cursor / Claude Code 这类 AI 助手直接调用它：

```powershell
codegraph install --target auto --location global -y
```

之后在支持 MCP 的助手里，它就能用 CodeGraph 查询项目符号、调用关系、影响范围等信息。这个工具的核心价值是：不用每次都让 AI 大范围 grep 文件，而是先查本地 `.codegraph` 索引，更省 token，也更快。官方介绍说它是 local-first，会用 tree-sitter 解析代码并把符号、关系、文件存在本地 SQLite 里，通过 CLI/MCP/TypeScript library 暴露出来：见 [CodeGraph docs](https://colbymchenry.github.io/codegraph/getting-started/introduction) 和 [GitHub README](https://github.com/colbymchenry/codegraph)。

另外你贴的帮助里 `Usage: codegrraph` 多了一个 `r`，看起来只是帮助文本拼写问题；实际命令仍然是：

```powershell
codegraph --help
```