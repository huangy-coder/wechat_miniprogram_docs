# wx.shareToWeRun(Object object)

> 官方文档：[wx.shareToWeRun(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/werun/wx.shareToWeRun.html)
> 所属分类：[开放接口](../开放接口目录.md)
> 导航路径：开放接口 / 微信运动 / wx.shareToWeRun
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#异步-API-返回-Promise) 调用**：支持
> **小程序插件**：不支持

> 相关文档: [分享数据到微信运动](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/share-werun.html)

## 功能描述

分享数据到微信运动。

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| recordList | Array.<Object> |   | 是 | 运动数据列表 |
| success | function |   | 否 | 接口调用成功的回调函数 |
| fail | function |   | 否 | 接口调用失败的回调函数 |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

补充表：
| 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| typeId | number |   | 是 | 运动项目id |
| time | number |   | 是 | 运动时长 |
| distance | number |   | 是 | 运动距离 |
| calorie | number |   | 是 | 消耗卡路里 |
