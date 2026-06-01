# wx.offCopyUrl()

> 官方文档：[wx.offCopyUrl()](https://developers.weixin.qq.com/miniprogram/dev/api/share/wx.offCopyUrl.html)
> 所属分类：[转发](转发目录.md)
> 导航路径：转发 / wx.offCopyUrl
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.14.3 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：不支持

## 功能描述

移除用户点击右上角菜单的「复制链接」按钮时触发的事件的全部监听函数

## 示例代码

```javascript
  // 绑定分享参数
  wx.onCopyUrl(() => {
    return { query: 'a=1&b=2' }
  })

  // 取消绑定分享参数
  wx.offCopyUrl()
```
