# wx.getExtConfig(Object object)

> 官方文档：[wx.getExtConfig(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/ext/wx.getExtConfig.html)
> 所属分类：[第三方平台](第三方平台目录.md)
> 导航路径：第三方平台 / wx.getExtConfig
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 1.1.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#%E5%BC%82%E6%AD%A5-API-%E8%BF%94%E5%9B%9E-Promise) 调用**：支持
> **小程序插件**：不支持
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持

## 功能描述

获取[第三方平台](https://developers.weixin.qq.com/miniprogram/dev/devtools/ext.html)自定义的数据字段。

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
| extConfig | Object | 第三方平台自定义的数据 |

## Tips

1. 本接口暂时无法通过 [wx.canIUse](../1.基础/wx.canIUse.md) 判断是否兼容，开发者需要自行判断 [wx.getExtConfig](wx.getExtConfig.md) 是否存在来兼容

```js
if (wx.getExtConfig) {
  wx.getExtConfig({
    success (res) {
      console.log(res.extConfig)
    }
  })
}
```
