# 配置片段

这里存放了一些从 `list.meta.yml` 中拆分出的配置片段，用于将本项目提供的一些配置整合到其它配置中。

# 配置示例

见 [example.yml](./example.yml)。

你也可以在不支持自动更新订阅的客户端中直接使用该配置文件，或是直接将其作为内核配置而不使用客户端。尽管该文件很少变更，我们仍然建议您定期手动更新本地配置。该配置未启用局域网访问，包括代理和控制 API。

# 文件说明

## 覆写规则集

这些文件仅支持 Meta (mihomo) 内核！

- [rules_online.yml](./rules_online.yml)：基于下方 Rule Providers 制成的统一规则集，可以用作代理工具的“覆写配置”。
- [rules.yml](./rules.yml)：与上一个文件类似，但内置了所有规则，无需二次联网下载，可以用于订阅转换工具的“覆写配置”或支持“自动更新覆写配置”的代理工具的“覆写配置”。

比如，你可以在 subs-check 配置中设置：

```yaml
mihomo-overwrite-url: "https://ghproxy.net/https://raw.githubusercontent.com/peasoft/NoMoreWalls/master/snippets/rules.yml"
```

## Proxy Providers 规则集

- [nodes.meta.yml](./nodes.meta.yml)：适用于 Meta (mihomo) 内核的节点列表。
- [nodes.yml](./nodes.yml)：适用于原版 Clash 内核的节点列表，注意**不要**和下文的 `proxy.yml` 搞混了。
- nodes_地区码.meta.yml：相应地区的节点列表，根据名称识别，不保证准确性，也不保证使用第三方服务时是否会被判断为国区。对于原版 Clash 内核 (不推荐)，请去掉 `.meta`。
<!-- - [nodes_redir.yml](./nodes_redir.yml)：在多个地区中转的节点列表，其余同上。 -->

## Rule Providers 规则集

- [adblock.yml](./adblock.yml)：广告屏蔽域名列表。
- [proxy.yml](./proxy.yml)：需要走代理的域名列表。
- [direct.yml](./direct.yml)：需要直连的域名列表。
- [region.yml](./region.yml)：存在锁区的域名列表。
- [malware.yml](./malware.yml)：包含病毒软件的域名列表。

注意：广告拦截列表中的域名不会出现在需要走代理的域名列表中，因此即使您没有使用广告屏蔽规则，仍有一些广告会无法加载。

# 加速链接（以 Meta 节点列表为例）

注意：下列 JsDelivr 链接有长时间缓存，得到的订阅可能存在 1 小时 ～ 7 天 不等的延迟。更新订阅时优先使用非 JsDelivr 订阅；如无法更新再使用 JsDelivr 订阅，然后在开启代理的情况下从“原始链接”更新。

- 原始链接: `https://raw.githubusercontent.com/peasoft/NoMoreWalls/master/snippets/nodes.meta.yml`
- GhProxy.net: `https://ghproxy.net/https://raw.githubusercontent.com/peasoft/NoMoreWalls/master/snippets/nodes.meta.yml`
- 此处不公开部分私有镜像站
- JsDelivr 默认 (当前 Fastly)：`https://cdn.jsdelivr.net/gh/peasoft/NoMoreWalls@master/snippets/nodes.meta.yml`
- JsDelivr Fastly CDN: `https://fastly.jsdelivr.net/gh/peasoft/NoMoreWalls@master/snippets/nodes.meta.yml`
- JsDelivr Cloudflare CDN: `https://testingcf.jsdelivr.net/gh/peasoft/NoMoreWalls@master/snippets/nodes.meta.yml`
- JsDelivr GCore CDN: `https://gcore.jsdelivr.net/gh/peasoft/NoMoreWalls@master/snippets/nodes.meta.yml`
