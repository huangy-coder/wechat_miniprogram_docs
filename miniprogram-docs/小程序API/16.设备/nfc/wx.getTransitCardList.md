# wx.getTransitCardList(Object args)

> 官方文档：[wx.getTransitCardList(Object args)](https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/wx.getTransitCardList.html)
> 所属分类：[设备](../设备目录.md)
> 导航路径：设备 / NFC 读写 / wx.getTransitCardList
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 3.16.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#%E5%BC%82%E6%AD%A5-API-%E8%BF%94%E5%9B%9E-Promise) 调用**：不支持
> **小程序插件**：不支持
> **微信 iOS 版**：不支持
> **微信 Android 版**：支持
> **微信 鸿蒙 OS 版**：不支持

## 功能描述

仅 Android 可用。获取设备中已开通的所有交通卡列表及基本状态

## 参数

### Object args

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| issuerID | String |   | 否 | 交通卡卡种标识 |
| success | function |   | 否 | 接口调用成功的回调函数 |
| fail | function |   | 否 | 接口调用失败的回调函数 |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

#### args.success 回调函数

##### 参数

###### Object object

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| result | boolean | 返回值 |
| errorMsg | String | 错误信息 |
| cards | Array.<String> | TransitCardInfo 的 JSON 字符串数组，需 JSON.parse 后使用 |

## 示例代码

```javascript
const { result, errorMsg, cards } = await wx.getTransitCardList({
  issuerID: 'changsha',
});
```
