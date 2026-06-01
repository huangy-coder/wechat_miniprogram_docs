# wx.getShareInfo(Object object)

> 官方文档：[wx.getShareInfo(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/share/wx.getShareInfo.html)
> 所属分类：[转发](转发目录.md)
> 导航路径：转发 / wx.getShareInfo
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

从基础库 [2.17.3](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 开始，本接口停止维护，请使用 [wx.getGroupEnterInfo](../15.开放接口/group/wx.getGroupEnterInfo.md) 代替

> 基础库 1.1.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#异步-API-返回-Promise) 调用**：不支持
> **需要页面权限**：当前是插件页面时，宿主小程序不能调用该接口，反之亦然
> **小程序插件**：支持，需要小程序基础库版本不低于 [2.1.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)
> 在小程序插件中使用时，只能在当前插件的页面中调用
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持
> **微信 鸿蒙 OS 版**：支持

## 功能描述

获取转发详细信息（主要是获取群ID）。 从群聊内的小程序消息卡片打开小程序时，调用此接口才有效。从基础库 v2.17.3 开始，推荐用 [wx.getGroupEnterInfo](../15.开放接口/group/wx.getGroupEnterInfo.md) 替代此接口。

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| shareTicket | string |   | 是 | shareTicket，详见[获取更多转发信息](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/share.html#获取更多转发信息) |   |
| timeout | number |   | 否 | 超时时间，单位 ms | [1.9.90](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| success | function |   | 否 | 接口调用成功的回调函数 |   |
| fail | function |   | 否 | 接口调用失败的回调函数 |   |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |   |

#### object.success 回调函数

##### 参数

###### Object res

| 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| errMsg | string | 错误信息 |   |
| encryptedData | string | 包括敏感数据在内的完整转发信息的加密数据，详细见[加密数据解密算法](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/signature.html) |   |
| iv | string | 加密算法的初始向量，详细见[加密数据解密算法](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/signature.html) |   |
| cloudID | string | 敏感数据对应的云 ID，开通[云开发](https://developers.weixin.qq.com/miniprogram/dev/wxcloudservice/wxcloud/basis/getting-started.html)的小程序才会返回，可通过云调用直接获取开放数据，详细见[云调用直接获取开放数据](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/signature.html#method-cloud) | [2.7.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |

## 示例代码

敏感数据获取方式 [加密数据解密算法](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/signature.html#加密数据解密算法) 。
获取得到的开放数据为以下 json 结构（其中 openGId 为当前群的唯一标识）：

```json
{
 "openGId": "OPENGID"
}
```

## Tips

- 如需要展示群名称，小程序可以使用 [开放数据组件](https://developers.weixin.qq.com/miniprogram/dev/component/open-data.html)
- 小游戏可以通过 [`wx.getGroupInfo`](https://developers.weixin.qq.com/miniprogram/dev/api/share/errorwx.getGroupInfo)) 接口获取群名称
