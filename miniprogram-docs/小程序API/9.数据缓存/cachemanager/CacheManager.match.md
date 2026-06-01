# Object CacheManager.match(Object evt)

> 官方文档：[Object CacheManager.match(Object evt)](https://developers.weixin.qq.com/miniprogram/dev/api/storage/cachemanager/CacheManager.match.html)
> 所属分类：[数据缓存](../数据缓存目录.md)
> 导航路径：数据缓存 / 缓存管理器 / CacheManager / CacheManager.match
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.24.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：不支持

> 相关文档: [弱网体验优化](https://developers.weixin.qq.com/miniprogram/dev/framework/performance/weak-network.html)

## 功能描述

匹配命中的缓存规则，一般需要和 request 事件搭配使用。

## 参数

### Object evt

request 事件对象

## 返回值

### Object

匹配到的缓存

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| ruleId | string | 命中的规则 id |
| cacheId | string | 缓存 id |
| data | any | 缓存内容，会带有 fromCache 标记，方便开发者区分内容是否来自缓存 |
| createTime | number | 缓存创建时间 |
| maxAge | number | 缓存有效时间 |

## 示例代码

```js
function handler(evt) {
  const cache = cacheManager.match(evt)
  // 若有重复监听，则取第一个 handler 返回的 promise
  return new Promise((resolve, reject) => {
    if (cache.data) {
      resolve(cache.data)
    } else {
      reject('no cache')
    }
  })
}
cacheManager.on('request', handler)
```
