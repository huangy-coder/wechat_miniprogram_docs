# wx.openStoreOrderDetail(Object object)

> 官方文档：[wx.openStoreOrderDetail(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/store/wx.openStoreOrderDetail.html)
> 所属分类：[开放接口](../开放接口目录.md)
> 导航路径：开放接口 / 微信小店 / wx.openStoreOrderDetail
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 3.7.1 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#异步-API-返回-Promise) 调用**：不支持
> **小程序插件**：不支持

> 相关文档: [微信小店指引](https://developers.weixin.qq.com/doc/store/API/basics/component.html)

## 功能描述

打开微信小店订单详情页

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| orderId | string |   | 是 | 订单id，通过[回调事件](https://developers.weixin.qq.com/miniprogram/dev/platform-capabilities/business-capabilities/cooperation_shop/order_callback.html#%E4%BA%94%E3%80%81%E5%90%88%E4%BD%9C%E8%B4%A6%E5%8F%B7%E5%BA%97%E9%93%BA%E8%AE%A2%E5%8D%95%E9%80%9A%E7%9F%A5%E4%BA%8B%E4%BB%B6)获取 |
| success | function |   | 否 | 接口调用成功的回调函数 |
| fail | function |   | 否 | 接口调用失败的回调函数 |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

#### object.fail 回调函数

##### 参数

###### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| message | string | 错误信息 |
| code | number | 错误码 |

补充表：
| 合法值 | 说明 |
| --- | --- |
| -1 | 系统失败 |
| 0 | 成功 |
| 1001 | 缺少必要参数 |
| 1002 | 网络错误 |
| 817323001 | 合作账号订单id不合法 |
| 817323002 | 无法获取该订单 |
| 817323003 | 当前小程序不是绑定的合作账号 |
