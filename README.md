# NoMoreWalls

[![Fetch Status](https://github.com/peasoft/NoMoreWalls/actions/workflows/fetch.yml/badge.svg)](https://github.com/peasoft/NoMoreWalls/actions/workflows/fetch.yml) [![Stars](https://img.shields.io/github/stars/peasoft/NoMoreWalls?style=flat)](https://github.com/peasoft/NoMoreWalls/stargazers) [![Watchers](https://img.shields.io/github/watchers/peasoft/NoMoreWalls?style=flat)](https://github.com/peasoft/NoMoreWalls/watchers) [![Forks](https://img.shields.io/github/forks/peasoft/NoMoreWalls?style=flat)](https://github.com/peasoft/NoMoreWalls/forks) [![Repo size](https://img.shields.io/github/repo-size/peasoft/NoMoreWalls)](https://github.com/peasoft/NoMoreWalls/commits) [![jsDelivr stats](https://data.jsdelivr.com/v1/package/gh/peasoft/NoMoreWalls/badge?style=rounded)](https://www.jsdelivr.com/package/gh/peasoft/NoMoreWalls) ![Vistors](https://visitor-badge.laobi.icu/badge?page_id=peasoft.NoMoreWalls) [![996.icu](https://img.shields.io/badge/link-996.icu-red.svg)](https://996.icu) [![LICENSE](https://img.shields.io/badge/license-Anti%20996-blue.svg)](https://github.com/peasoft/NoMoreWalls/blob/master/LICENSE.md)

自动抓取合并互联网上的公开节点。

## 公告

**我们拒绝为任何“女权组织”提供任何服务！我们绝不允许任何企图破坏中国国家和社会稳定的组织或个人使用本服务！**

本项目拒绝为**流氓资本家**提供任何服务！特别的，项目的许可证**严格禁止**实行 996 工作制的公司使用本项目！

此项目包含“反 996 许可证”，请各位使用者**不要违法违规要求别人加班，自觉遵守《中华人民共和国劳动法》及其它法律法规**！

**本项目提供的 Clash 订阅包含我们精心设计的分流规则，Google Play 软件秒下 (限国行机)，自动识别被墙域名，只需将 `🐟 漏网之鱼` 维持在 `DIRECT` 即可！**

由于 [BootCDN/Staticfile 已被病毒公司收购](https://www.52pojie.cn/thread-1944970-1-1.html)，我们拦截了这些网站。

如果您访问部分网站时遇到问题，可以将 `🚨 病毒网站` 分类切换为 `DIRECT`，但是您需要**自行承担一切安全风险，包括但不限于广告骚扰，账号被盗，设备中毒**等，请三思而后行！！！

为防止失联，我们建立了镜像：<https://peasoft.github.io/NWalls.html>

另有**理论上永不被墙的** jsDelivr 镜像，**强烈建议**收藏：<https://www.jsdelivr.com/package/gh/peasoft/NoMoreWalls>

我们新增了 [`snippets` 目录](./snippets/) 来存放从 `list.meta.yml` 中拆分出的配置片段，用于将本项目提供的一些配置整合到你自己的配置中。此目录中还有本项目的独立规则集覆写文件。

### 为什么 *不要* 使用付费节点？

1. 付费节点存在付完费厂商立即跑路的**诈骗风险**，且一旦被骗钱款**无法追回**！
2. 付费节点需要注册账号并付费，厂商可以借此收集你的**个人信息**然后倒卖！付费节点管理程序可能**存在漏洞**，由 ZF 支持的黑客也可能把你的个人信息提交给 ZF。

推荐阅读 [DiningFactory/panda-vpn-pro](https://github.com/DiningFactory/panda-vpn-pro)。

## 使用方法

添加 Base64 订阅：
- [原始链接](https://raw.githubusercontent.com/peasoft/NoMoreWalls/master/list.txt)
- [GhProxy.net](https://ghproxy.net/https://raw.githubusercontent.com/peasoft/NoMoreWalls/master/list.txt)
- 此处不公开部分私有镜像站

以下链接可能不是最新，但绝对不会被封：
- [JsDelivr 默认 (当前 Fastly)](https://cdn.jsdelivr.net/gh/peasoft/NoMoreWalls@master/list.txt)
- [JsDelivr Fastly CDN](https://fastly.jsdelivr.net/gh/peasoft/NoMoreWalls@master/list.txt)
- [JsDelivr Cloudflare CDN](https://testingcf.jsdelivr.net/gh/peasoft/NoMoreWalls@master/list.txt)
- [JsDelivr GCore CDN](https://gcore.jsdelivr.net/gh/peasoft/NoMoreWalls@master/list.txt)

或添加 Clash Meta 订阅：（如果使用的是原版 Clash，请将链接最后的 `.meta.yml` 替换成 `.yml`。我们始终建议您使用 Clash Meta 而不是已被废弃的 Clash。**提醒：Clash Meta (mihomo) 是有手机版的！还在用 Clash For Android 的用户请尽快迁移至 [Clash Meta For Android](https://github.com/MetaCubeX/ClashMetaForAndroid)！**）
- [原始链接](https://raw.githubusercontent.com/peasoft/NoMoreWalls/master/list.meta.yml)
- [GhProxy.net](https://ghproxy.net/https://raw.githubusercontent.com/peasoft/NoMoreWalls/master/list.meta.yml)
- 此处不公开部分私有镜像站

以下链接可能不是最新，但绝对不会被封：
- [JsDelivr 默认 (当前 Fastly)](https://cdn.jsdelivr.net/gh/peasoft/NoMoreWalls@master/list.meta.yml)
- [JsDelivr Fastly CDN](https://fastly.jsdelivr.net/gh/peasoft/NoMoreWalls@master/list.meta.yml)
- [JsDelivr Cloudflare CDN](https://testingcf.jsdelivr.net/gh/peasoft/NoMoreWalls@master/list.meta.yml)
- [JsDelivr GCore CDN](https://gcore.jsdelivr.net/gh/peasoft/NoMoreWalls@master/list.meta.yml)

或添加 Sing-Box 订阅：（第三方提供转换，不支持本项目的节点选择和分流规则。建议在本地搭建转换服务。）
- [转换链接（第三方）](https://subwork.top/singbox?config=https%3A%2F%2Fraw.githubusercontent.com%2Fpeasoft%2FNoMoreWalls%2Fmaster%2Fsnippets%2Fnodes.meta.yml&ua=&selectedRules=%5B%22Location%3ACN%22%2C%22Private%22%2C%22Non-China%22%2C%22Github%22%2C%22Google%22%2C%22Youtube%22%2C%22AI+Services%22%2C%22Telegram%22%5D&customRules=%5B%5D&enable_clash_ui=true)

## 免责声明

订阅节点仅作学习交流使用，用于查找资料，学习知识，不做任何违法行为。所有资源均来自互联网，仅供大家交流学习使用，出现违法问题概不负责。**做出违法行为需要承担法律责任，侥幸逃脱是不可能的**！~~为阻止违法行为，本项目随时可以停止运行~~ 本项目可以采取各种技术手段来尽力阻止违法行为。

## 关于 Fork 和在线部署

不是说不能 Fork，但是请记得定时点击仓库中的 Sync fork 来同步更新主程序。这个项目是有时效性的，老版本基本都不能用了。

## 本地部署

请确保你安装了 Python 且版本大于等于 3.8。

1. 使用 Git 克隆本仓库，由于本仓库的完整 Commit 历史极大，请务必指定 `--depth=1`：
    ```bash
    git clone https://github.com/peasoft/NoMoreWalls.git --depth=1
    ```
    或者 [下载项目文件](https://github.com/peasoft/NoMoreWalls/archive/refs/heads/master.zip) 并解压。
2. 安装依赖库
    ```bash
    pip install -r requirements.txt
    ```
3. 如果你所在地区没有墙或你在使用 Tun 模式或透明代理：创建空白文件 `local_proxy.conf`，填入 `NONE`，然后跳到第 9 步
4. 如果你已有代理，请跳到第 8 步。
5. 创建空白文件 `local_proxy.conf`
6. 运行 `fetch.py`
7. 将生成的订阅导入代理工具并正确配置好代理
8. 在 `local_proxy.conf` 中按如下格式填入你的代理工具的 http(s) 地址，如：
    ```plain
    http://127.0.0.1:7890/
    ```
9. 运行 `fetch.py`
10. 你已获得完整订阅

如果本地仓库长期未更新，也请使用 `--depth=1` 更新仓库：

```bash
git pull --depth=1
git reset --hard origin/master
```

## 一些题外话

- **[违法电影《监狱来的妈妈》，这些人是想对中国社会进行大规模脱敏训练](https://www.bilibili.com/video/BV1XcLD6BE6p/)**
- **什么才是真正的性别平等？（原视频已失效）我们要真正的平权而不是所谓的“女权”！“公平”不应成为特权的借口！**
- **[NGO 的影子借“公益”之名渗透名校！](https://www.bilibili.com/video/BV15JtnzMExo/)防范身边的境外势力渗透！**
- **[油罐车事件是最好的照妖镜，上赶着带节奏都是谁请大家记下来。](https://www.bilibili.com/video/BV1p1421b7Ki)私有化愈发严重影响的是所有中国人的切身利益，必须用公有平衡私有我们才有发展的前途。**

**上方事件的严重性已经远超下面的事情了！！！**

- **[百度？百毒！](https://user.guancha.cn/main/content?id=100552)魏则西去世3周年：害死他的百度广告和莆田系医院**
- **[没收违法所得的合法性与合理性基础欠缺——简评承德程序员事件](https://www.dehenglaw.com/CN/tansuocontent/0008/029562/7.aspx?MID=0902)**
- **[【BootCDN/Staticfile投毒分析】供应链投毒后，我们的选择还剩下哪些？](https://www.52pojie.cn/thread-1944970-1-1.html)**
- 未完待续……
<!-- - **[【独家恢复】我们的教育弄虚作假，到底是为了什么](https://peasoft.github.io/2023/08/26/cnedu.html)：如此视频，为何惨遭删除？我们恢复了这段视频，只为让更多人可以看清现实。** -->
<!-- - **[最流氓的软件可以流氓到什么程度？](https://www.zhihu.com/question/29129310)我翻开其他网页一查，歪歪斜斜的每页上都写着“危险网页”几个字。我横竖睡不着，仔细看了半夜，才从字缝里看出字来，满本都写着两个字是“霸权”！** -->
<!-- - **[《满江红》的行为艺术](https://www.bilibili.com/video/BV11v4y1t7Gw/)：秦桧竟是我自己？** -->
<!-- - **[「 深蓝洞察 」2022 年度最“不可赦”漏洞](https://mp.weixin.qq.com/s/P_EYQxOEupqdU0BJMRqWsw)：知名互联网厂商(TMD并夕夕)持续挖掘新的安卓 OEM 相关漏洞，在其公开发布的 App 中实现对目前市场主流手机系统的漏洞攻击**（[具体分析](https://mp.weixin.qq.com/s/kiLvnJSDZpYRHI_XiUx9gg)）~~现已被工信部提名~~ -->
<!-- - **[暑假学校敢补课？举报！](https://www.bilibili.com/video/BV1Vk4y1K79B)** -->
<!-- - **[一学校扔掉学生百余份外卖](https://www.bilibili.com/video/BV1a14y1S7n6)：涉嫌违法！** -->

## Star History

<a href="https://www.star-history.com/?repos=peasoft%2FNoMoreWalls&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=peasoft/NoMoreWalls&type=date&theme=dark&legend=top-left&sealed_token=8UVynllUplJa4vHl5DyiCpLI2RXSk29T0lsBrpwrzwLAbSJZj26QdM8Ci747u68K-UUMdH5GiH86o4tNu0hVYpj6AbR97k5HH730KfsO1wMCMWPsWiqu08zWfVjPUvj6qCu70vTw7w2ukyOzCl8Fzp_6-12EqObw3tw7JorvJ0nCXUB59L42IFPFYb_q" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=peasoft/NoMoreWalls&type=date&legend=top-left&sealed_token=8UVynllUplJa4vHl5DyiCpLI2RXSk29T0lsBrpwrzwLAbSJZj26QdM8Ci747u68K-UUMdH5GiH86o4tNu0hVYpj6AbR97k5HH730KfsO1wMCMWPsWiqu08zWfVjPUvj6qCu70vTw7w2ukyOzCl8Fzp_6-12EqObw3tw7JorvJ0nCXUB59L42IFPFYb_q" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=peasoft/NoMoreWalls&type=date&legend=top-left&sealed_token=8UVynllUplJa4vHl5DyiCpLI2RXSk29T0lsBrpwrzwLAbSJZj26QdM8Ci747u68K-UUMdH5GiH86o4tNu0hVYpj6AbR97k5HH730KfsO1wMCMWPsWiqu08zWfVjPUvj6qCu70vTw7w2ukyOzCl8Fzp_6-12EqObw3tw7JorvJ0nCXUB59L42IFPFYb_q" />
 </picture>
</a>
