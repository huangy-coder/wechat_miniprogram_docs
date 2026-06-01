# wx.getShowSplashAdStatus(Object object)

> 官方文档：[wx.getShowSplashAdStatus(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/ad/wx.getShowSplashAdStatus.html)
> 所属分类：[广告](广告目录.md)
> 导航路径：广告 / wx.getShowSplashAdStatus
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 3.7.8 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#异步-API-返回-Promise) 调用**：不支持
> **小程序插件**：不支持

## 功能描述

获取封面广告组件展示状态。请通过 [wx.getSystemInfoSync()](../1.基础/system/wx.getSystemInfoSync.md) 返回对象的 SDKVersion 判断基础库版本号后再使用该 API（小游戏端要求 >= 3.7.8， 小程序端要求 >= 3.7.8）。

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |   | 否 | 接口调用成功的回调函数 |
| fail | function |   | 否 | 接口调用失败的回调函数 |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

#### object.success 回调函数

##### 参数

###### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| status | string | 封面广告组件展示状态 |
| code | number | 封面广告组件展示状态码 |

补充表：
| 合法值 | 说明 |
| --- | --- |
| unknown | 初始值，状态未知 |
| pending | 进行展示中 |
| success | 展示成功 |
| fail | 展示失败 |

补充表：
| 合法值 | 说明 |
| --- | --- |
| -1 | 初始值，状态未知 |
| 1 | 展示成功 |
| 2 | 主动拦截过滤，不展示广告 |
| 3 | 展示超时 |

## 示例代码

```js
// 获取封面广告展示状态
wx.getShowSplashAdStatus({
  success: res => {
    console.log('getShowSplashAdStatus res', res.status, res.code)
  },
})
```
