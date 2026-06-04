## 一句话

这是一份放在本机 `E:\代理\zz_v2rayN-With-Core-SelfContained` 的 v2rayN 自带内核版代理工具包，用来在 Windows 上临时或日常开启本地代理。

## 资源位置

- 主目录：`E:\代理\zz_v2rayN-With-Core-SelfContained`
- 启动程序：`E:\代理\zz_v2rayN-With-Core-SelfContained\v2rayN.exe`
- 配置目录：`E:\代理\zz_v2rayN-With-Core-SelfContained\guiConfigs`
- 日志目录：`E:\代理\zz_v2rayN-With-Core-SelfContained\guiLogs`
- 临时目录：`E:\代理\zz_v2rayN-With-Core-SelfContained\guiTemps`

## 当前确认信息

- 程序：v2rayN
- 文件版本：`6.23`
- 资源规模：约 `53` 个文件，合计约 `462 MB`
- 本地 SOCKS 代理：`127.0.0.1:10808`
- 本地 HTTP 代理：`127.0.0.1:10809`
- 当前界面语言：`zh-Hans`
- 当前系统代理模式：配置中 `sysProxyType = 0`，需要打开 v2rayN 后确认是否已启用系统代理。
- TUN 模式：配置中 `enableTun = false`
- 自动启动：配置中 `autoRun = false`
- GUI 日志：配置中 `enableLog = true`

## 目录里有什么

- `bin\Xray`：Xray 内核与 `geoip.dat`、`geosite.dat`
- `bin\v2fly` / `bin\v2fly_v5`：v2ray/v2fly 相关内核
- `bin\clash` / `bin\clash_meta`：Clash / Clash Meta 内核
- `bin\sing_box`：sing-box 内核
- `bin\SagerNet`、`bin\hysteria`、`bin\naiveproxy`、`bin\tuic`：其他协议或内核组件
- `guiConfigs\guiNConfig.json`：v2rayN GUI 设置
- `guiConfigs\config.json`：当前生成的运行配置
- `guiConfigs\guiNDB.db`：v2rayN 节点/分组等本地数据库
- `guiLogs\YYYY-MM-DD.txt`：按日期保存的日志

## 使用方式

1. 打开 `E:\代理\zz_v2rayN-With-Core-SelfContained\v2rayN.exe`
2. 在 v2rayN 里选择可用节点。
3. 如果要让浏览器、命令行或其他软件走代理，确认系统代理已开启，或手动配置：
   - HTTP：`127.0.0.1:10809`
   - SOCKS：`127.0.0.1:10808`
4. 不用了就退出 v2rayN，或在软件里关闭系统代理，避免后续网络异常。

## 备份与恢复

优先备份这些文件：

- `guiConfigs\guiNConfig.json`
- `guiConfigs\guiNDB.db`
- `guiConfigs\guiNConfig.json.*.bak`
- `guiConfigs\guiNDB.db.*.bak`

当前已存在的备份：

- `guiNConfig.json.20260523-140208.bak`
- `guiNDB.db.20260523-140208.bak`
- `guiNDB.db.20260523-163636.address-change.bak`

恢复时建议先完整复制 `guiConfigs` 文件夹，再启动 v2rayN 检查节点、订阅、系统代理和路由规则。

## 注意事项

- 不要把 `guiConfigs`、节点链接、订阅地址、二维码、数据库文件发到公开仓库或公开聊天里。
- `guiNDB.db` 可能包含节点、订阅或服务端信息，按敏感文件处理。
- 如果浏览器能联网但命令行不能联网，优先检查命令行是否读取了 `HTTP_PROXY` / `HTTPS_PROXY` / `ALL_PROXY`。
- 如果软件退出后网络异常，检查 Windows 系统代理是否还停留在 `127.0.0.1:10809`。
- 如果代理可用但部分网站异常，检查 v2rayN 的路由模式、DNS、节点状态和 `geoip/geosite` 数据。

## 关联

- [[AI Agent 执行环境]]
- [[Horizon 信息雷达]]

## 更新记录

- 2026-06-04：首次沉淀本机代理资源位置、启动方式、端口、备份点和注意事项。
