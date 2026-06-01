# wx.onCopyUrl(function listener)

> 官方文档：[wx.onCopyUrl(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/share/wx.onCopyUrl.html)
> 所属分类：[转发](转发目录.md)
> 导航路径：转发 / wx.onCopyUrl
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.14.3 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：不支持

## 功能描述

监听用户点击右上角菜单的「复制链接」按钮时触发的事件。

## 参数

### function listener

用户点击右上角菜单的「复制链接」按钮时触发的事件的监听函数

#### 参数

##### Object res

| 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| query | string | 用短链打开小程序时当前页面携带的查询字符串，默认为空字符串。小程序中使用时，应在进入页面时调用 `wx.onCopyUrl` 自定义 `query`，退出页面时调用 `wx.offCopyUrl`，防止影响其它页面。 |   |
| title | string | 短链中的自定义标题，显示在小程序名称之后。在基础库3.15.1之前，默认是 navigationBarTitleText 的值，在基础库3.15.1及之后，默认为空字符串。 | [3.15.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| promise | Object | 如果该参数存在且为有效的 Promise，则最终的 `query` 和 `title` 将以该 Promise 的 resolve 结果为准；如果 Promise 在 2 秒内未 resolve 或 reject，则回退使用同步传入的默认参数。 | [3.16.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |

## 示例代码

```javascript
  // 基础用法：同步返回分享参数
  wx.onCopyUrl(() => {
    return { query: 'a=1&b=2' }
  })

  // 使用 promise 异步返回分享参数
  wx.onCopyUrl(() => {
    return {
      query: 'a=1',  // 兜底默认参数，promise 超时时使用
      title: '默认标题',
      promise: fetchSomeInfo().then((info) => ({ query: info.query, title: info.title }))
    }
  })

  // 取消绑定分享参数
  wx.offCopyUrl()
```
