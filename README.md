# NoMoreWalls

[![Fetch Status](https://github.com/peasoft/NoMoreWalls/actions/workflows/fetch.yml/badge.svg)](https://github.com/peasoft/NoMoreWalls/actions/workflows/fetch.yml) [![Stars](https://img.shields.io/github/stars/peasoft/NoMoreWalls?style=flat)](https://github.com/peasoft/NoMoreWalls/stargazers) [![Watchers](https://img.shields.io/github/watchers/peasoft/NoMoreWalls?style=flat)](https://github.com/peasoft/NoMoreWalls/watchers) [![Forks](https://img.shields.io/github/forks/peasoft/NoMoreWalls?style=flat)](https://github.com/peasoft/NoMoreWalls/forks) ![Vistors](https://visitor-badge.laobi.icu/badge?page_id=peasoft.NoMoreWalls) [![996.icu](https://img.shields.io/badge/link-996.icu-red.svg)](https://996.icu) [![LICENSE](https://img.shields.io/badge/license-Anti%20996-blue.svg)](https://github.com/peasoft/NoMoreWalls/blob/master/LICENSE.md) [![暮光计划](https://img.shields.io/badge/link-暮光计划--向戒网瘾学校宣战-red.svg)](https://proj3ctaurora.tilda.ws/)

自动抓取合并互联网上的公开节点。



## 关于 Google Play 等服务在国内无法使用的解决方法

~~由于 Google 调整了服务器安排，将原有的国外服务器的**域名**调整到了国内专版，但是**服务器**还没跟上，导致 Google Play 等服务在国内连上的是**空域名**，直接不能用了。~~

根据一些来源，这可能是一个多年以前的历史遗留问题了，只不过以前高质量的节点可以避开这个问题，而现在节点质量的下降导致这个问题又出现了。当前的解决办法有：


1. **把 V2Ray 和 Clash 都试一次**，部分高质量节点仅支持 V2Ray 或 Clash。Tip：对于 V2Ray，在 Play Store 开始下载软件后立即关掉 V2Ray，即可享受直连高速下载，下载完再把 V2Ray 打开。对于 Clash，使用本项目提供的**完整**订阅无需配置，自行配置的请看下一条。
2. **如果您使用的是本项目提供的 Rule Providers**，请在 `rules` 开头加上：
```yaml
  - DOMAIN-SUFFIX,googleapis.cn,🚀 选择代理
  - DOMAIN-SUFFIX,xn--ngstr-lra8j.com,DIRECT # Google Play 国外/国内 服务器
  - DOMAIN-SUFFIX,xn--ngstr-cn-8za9o.com,DIRECT # Google Play 纯国内 服务器，尚未完成部署
```
3. **自行寻找更好的机场**。

如果此问题有进展，我们会在此更新，请及时关注。

我们新增了 `snippets` 文件夹来存放从 `list.yml` 中拆分出的配置片段，用于将本项目提供的一些配置整合到你自己的配置中。

此项目现已添加“反 996 许可证”，请各位使用者**不要违法违规要求别人加班，自觉遵守《中华人民共和国劳动法》及其它法律法规**！

## 使用方法

注意：加速链接可能会失效，如果无法更新订阅，请把所有链接从上到下每个试一遍！你可以在电脑浏览器上安装油猴脚本 [Github 增强 - 高速下载](https://greasyfork.org/zh-CN/scripts/412245)，在目录浏览点开 `list.txt`，然后在 `Raw` 按钮边上找到最新的加速链接。

添加 Base64 订阅：
- [原始链接](https://raw.githubusercontent.com/peasoft/NoMoreWalls/master/list.txt)
- [JsDelivr 反代（zzko.cn）](https://cdn.jsdelivr.us/gh/peasoft/NoMoreWalls@master/list.txt)
- [JsDelivr Fastly CDN](https://fastly.jsdelivr.net/gh/peasoft/NoMoreWalls@master/list.txt)
- [JsDelivr Cloudflare CDN](https://testingcf.jsdelivr.net/gh/peasoft/NoMoreWalls@master/list.txt)
- [JsDelivr GCore CDN](https://gcore.jsdelivr.net/gh/peasoft/NoMoreWalls@master/list.txt)
- [GhProxy.com](https://mirror.ghproxy.com/https://raw.githubusercontent.com/peasoft/NoMoreWalls/master/list.txt)

以下加速链接可能无效：
- [FastGit](https://raw.fgit.cf/peasoft/NoMoreWalls/master/list.txt) (403 Forbidden)
- [KGithub](https://raw.kgithub.com/peasoft/NoMoreWalls/master/list.txt)
- [KKGithub](https://raw.kkgithub.com/peasoft/NoMoreWalls/master/list.txt)

或添加 Clash 订阅：（重磅：本项目同时提供 Meta 专用订阅，支持更多节点！要使用 Meta 专用订阅，请将链接最后的 `.yml` 替换成 `.meta.yml`。如果 Meta 提示解析错误，请**更新 Meta 至最新版本**！）
- [原始链接](https://raw.githubusercontent.com/peasoft/NoMoreWalls/master/list.yml)
- [JsDelivr 反代（zzko.cn）](https://cdn.jsdelivr.us/gh/peasoft/NoMoreWalls@master/list.yml)
- [JsDelivr Fastly CDN](https://fastly.jsdelivr.net/gh/peasoft/NoMoreWalls@master/list.yml)
- [JsDelivr Cloudflare CDN](https://testingcf.jsdelivr.net/gh/peasoft/NoMoreWalls@master/list.yml)
- [JsDelivr GCore CDN](https://gcore.jsdelivr.net/gh/peasoft/NoMoreWalls@master/list.yml)
- [FastGit](https://raw.fgit.cf/peasoft/NoMoreWalls/master/list.yml)
- [GhProxy.com](https://mirror.ghproxy.com/https://raw.githubusercontent.com/peasoft/NoMoreWalls/master/list.txt)

以下加速链接可能无效：
- [KGithub](https://raw.kgithub.com/peasoft/NoMoreWalls/master/list.yml)
- [KKGithub](https://raw.kkgithub.com/peasoft/NoMoreWalls/master/list.yml)

## 免责声明

订阅节点仅作学习交流使用，用于查找资料，学习知识，不做任何违法行为。所有资源均来自互联网，仅供大家交流学习使用，出现违法问题概不负责。**做出违法行为需要承担法律责任，侥幸逃脱是不可能的**！为阻止违法行为，本项目随时可以停止运行！！！


## Star History

<a href="https://star-history.com/#peasoft/NoMoreWalls">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=peasoft/NoMoreWalls&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=peasoft/NoMoreWalls" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=peasoft/NoMoreWalls" />
  </picture>
</a>
