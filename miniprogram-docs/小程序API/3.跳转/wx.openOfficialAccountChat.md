# wx.openOfficialAccountChat(Object object)

> 官方文档：[wx.openOfficialAccountChat(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/navigate/wx.openOfficialAccountChat.html)
> 所属分类：[跳转](跳转目录.md)
> 导航路径：跳转 / wx.openOfficialAccountChat
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 3.10.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#%E5%BC%82%E6%AD%A5-API-%E8%BF%94%E5%9B%9E-Promise) 调用**：不支持
> **小程序插件**：不支持

## 功能描述

通过小程序打开公众号会话界面

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| username | string |   | 是 | 需要打开的公众号的微信号 |
| success | function |   | 否 | 接口调用成功的回调函数 |
| fail | function |   | 否 | 接口调用失败的回调函数 |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

## 示例代码

```js
  wx.openOfficialAccountChat({
         username: '', // 此处填写公众号的微信号
         success: res => {
         },
         fail: res => {
         }
     })
```

## Tips

1. 跳转的公众号需与小程序为同主体或关联主体
2. 如果用户没有关注则进行回退，跳转到公众号主页
