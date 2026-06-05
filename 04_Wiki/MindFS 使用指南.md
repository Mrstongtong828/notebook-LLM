# MindFS 使用指南

## 一句话

MindFS 是一个本地 AI Agent 远程访问网关，可以在浏览器或手机上访问电脑里的项目文件、Agent 会话和命令执行结果。

## 当前部署

- 本机地址：`http://127.0.0.1:7331`
- 当前版本：`v0.3.1`
- 安装位置：`C:\Users\tong'tong\AppData\Local\Programs\mindfs\bin\mindfs.exe`
- 日志位置：`C:\Users\tong'tong\AppData\Roaming\mindfs\logs\mindfs.log`

## 常用命令

```powershell
mindfs -status
mindfs -stop
mindfs -restart
mindfs "C:\path\to\project"
```

如果新终端还找不到 `mindfs`，可以用完整路径：

```powershell
& "$env:LOCALAPPDATA\Programs\mindfs\bin\mindfs.exe" -status
```

## 启动一个项目

```powershell
mindfs "项目路径"
```

启动后打开：

```text
http://localhost:7331
```

MindFS 只有传入项目路径时，才会把该目录加入托管列表。

## 手机访问

### 同一 Wi-Fi

默认 `127.0.0.1` 只能电脑自己访问。手机要访问，需要改成局域网监听：

```powershell
mindfs -stop
mindfs -addr :7331 "项目路径"
```

然后在手机浏览器打开：

```text
http://电脑局域网IP:7331
```

例如：

```text
http://192.168.1.23:7331
```

### 远程访问

在 MindFS 页面左下角点击绑定，登录 relayer 后，可以通过远程节点从手机访问电脑上的 MindFS。

### 私有网络

如果使用 Tailscale、ZeroTier 等工具，手机可以直接访问电脑的私有网络 IP：

```text
http://私有网络IP:7331
```

## 安全建议

只在可信网络里使用普通 HTTP。需要手机远程访问或局域网长期使用时，建议开启 TLS 和端到端加密：

```powershell
mindfs -stop
mindfs -tls -e2ee -addr :7331 "项目路径"
```

首次访问会需要配对码。

## 适合用来做什么

- 在手机上查看电脑项目文件。
- 从浏览器继续 Codex、Claude Code、OpenCode 等 Agent 会话。
- 把命令执行结果、工具调用和上下文以更清晰的界面查看。
- 管理多个本地项目目录。

## 排查

- 页面打不开：先运行 `mindfs -status`。
- 端口冲突：换端口启动，例如 `mindfs -addr :9000 "项目路径"`。
- 手机打不开：确认电脑和手机在同一 Wi-Fi，且使用的是电脑局域网 IP，不是 `127.0.0.1`。
- Agent 不可用：确认对应 CLI 已安装并已登录。

## 更新记录

- 2026-06-05：根据本机部署情况整理第一版。
