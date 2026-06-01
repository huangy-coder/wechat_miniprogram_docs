# CacheManager

> 官方文档：[CacheManager](https://developers.weixin.qq.com/miniprogram/dev/api/storage/cachemanager/CacheManager.html)
> 所属分类：[数据缓存](../数据缓存目录.md)
> 导航路径：数据缓存 / 缓存管理器 / CacheManager
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.24.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> 相关文档: [弱网体验优化](https://developers.weixin.qq.com/miniprogram/dev/framework/performance/weak-network.html)

缓存管理器。全局只有唯一实例，一旦被创建出来即表示接入缓存管理器。其有以下几个能力：

1. 在网络通畅时，符合一定规则的用户网络请求（目前只包括普通 wx.request 请求）会被缓存。
2. 在网络通畅时，某些 wx api 调用会被缓存。
3. 进入弱网/离线状态时，会提供事件给用户，用户可以决定是否使用缓存返回。
4. 提供进入和退出弱网/离线状态的事件。

> 1. 缓存管理器中涉及的网络请求如无特指，均指普通的 wx.request 异步请求，参数和返回值中均不考虑涉及 ArrayBuffer 或 TypedArray 的情形。
> 2. 缓存管理器中的缓存不会占用 storage 空间，但是有大小限制，请勿在非必要的请求上使用缓存。

## 属性

### string mode

当前缓存模式

**mode 的合法值**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| weakNetwork | 默认值，弱网/离线使用缓存返回 |   |
| always | 总是使用缓存返回 |   |
| none | 不开启，后续可手动开启/停止使用缓存返回 |   |

### string origin

全局 origin

### number maxAge

全局缓存有效时间

### number state

当前缓存管理器状态

**state 的合法值**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| 0 | 不使用缓存返回 |   |
| 1 | 使用缓存返回 |   |
| 2 | 未知 |   |

## 方法

### Array.<string> CacheManager.addRules(Array.<(string|RegExp|Record.<string, any>)> rules)

批量添加规则，规则写法可参考 [CacheManager.addRule](CacheManager.addRule.md)。

### string CacheManager.addRule(string|RegExp|Record.<string, any> rule)

添加规则。

### CacheManager.deleteRules(Array.<string> ids)

批量删除规则，同时会删除对应规则下所有缓存。

### CacheManager.deleteRule(string id)

删除规则，同时会删除对应规则下所有缓存。

### CacheManager.clearRules()

清空所有规则，同时会删除对应规则下所有缓存。

### CacheManager.on(string eventName, function handler)

监听事件。

### CacheManager.off(string eventName, function handler)

取消事件监听。

### CacheManager.start()

开启缓存，仅在 mode 为 none 时生效，调用后缓存管理器的 state 会置为 1。

### CacheManager.stop()

关闭缓存，仅在 mode 为 none 时生效，调用后缓存管理器的 state 会置为 0。

### Object CacheManager.match(Object evt)

匹配命中的缓存规则，一般需要和 request 事件搭配使用。

### CacheManager.deleteCaches(Array.<string> ids)

批量删除缓存。

### CacheManager.deleteCache(string id)

删除缓存。

### CacheManager.clearCaches()

清空所有缓存。
