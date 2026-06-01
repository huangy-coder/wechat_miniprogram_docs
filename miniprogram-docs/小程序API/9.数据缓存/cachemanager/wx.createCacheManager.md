# CacheManager wx.createCacheManager(Object object)

> 官方文档：[CacheManager wx.createCacheManager(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/storage/cachemanager/wx.createCacheManager.html)
> 所属分类：[数据缓存](../数据缓存目录.md)
> 导航路径：数据缓存 / 缓存管理器 / wx.createCacheManager
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.24.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：不支持

> 相关文档: [弱网体验优化](https://developers.weixin.qq.com/miniprogram/dev/framework/performance/weak-network.html)

## 功能描述

创建缓存管理器

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| origin | string |   | 否 | 全局 origin |
| mode | string | weakNetwork | 否 | 缓存模式 |
| maxAge | number |   | 否 | 全局缓存有效时间，单位为毫秒，默认为 7 天，最长不超过 30 天 |
| extra | object |   | 否 | 额外的缓存处理 |

补充表：
| 合法值 | 说明 |
| --- | --- |
| weakNetwork | 弱网/离线使用缓存返回 |
| always | 总是使用缓存返回 |
| none | 不开启，后续可手动开启/停止使用缓存返回 |

补充表：
| 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| apiList | Array.<string> |   | 否 | 需要缓存的 wx api 接口，不传则表示支持缓存的接口全都做缓存处理。返回的如果是缓存数据，开发者可通过 fromCache 标记区分 |

补充表：
| 合法值 | 说明 |
| --- | --- |
| wx.login |   |
| wx.checkSession |   |
| wx.getSetting |   |

## 返回值

### CacheManager

缓存管理器

## 示例代码

[查看完整示例代码](https://github.com/wechat-miniprogram/miniprogram-offline-demo)

```js
const cacheManager = createCacheManager()
cacheManager.addRule(/https:\/\/(?:.*)/ig) // 表示所有 https 请求都匹配

cacheManager.on('request', evt => {
 // 在弱网时接收到 wx.request 请求
 return new Promise((resolve, reject) => {
   const matchRes = cm.match(evt)
   if (matchRes && matchRes.data) {
     // 有缓存，返回
     resolve(matchRes.data)
   } else {
     // 没缓存，抛错
     reject({ errMsg: 'no cache' })
   }
 })
})
```
