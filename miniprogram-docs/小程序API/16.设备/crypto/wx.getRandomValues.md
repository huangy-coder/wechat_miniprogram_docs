# wx.getRandomValues(Object object)

> 官方文档：[wx.getRandomValues(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/device/crypto/wx.getRandomValues.html)
> 所属分类：[设备](../设备目录.md)
> 导航路径：设备 / 加密 / wx.getRandomValues
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.15.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#%E5%BC%82%E6%AD%A5-API-%E8%BF%94%E5%9B%9E-Promise) 调用**：支持
> **小程序插件**：不支持
> **微信 鸿蒙 OS 版**：支持

## 功能描述

获取密码学安全随机数

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| length | number |   | 是 | 整数，生成随机数的字节数，最大 1048576 |
| success | function |   | 否 | 接口调用成功的回调函数 |
| fail | function |   | 否 | 接口调用失败的回调函数 |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

#### object.success 回调函数

##### 参数

###### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| randomValues | ArrayBuffer | 随机数内容，长度为传入的字节数 |

## 示例代码

```js
wx.getRandomValues({
  length: 6, // 生成 6 个字节长度的随机数
  success: res => {
    console.log(wx.arrayBufferToBase64(res.randomValues)) // 转换为 base64 字符串后打印
  }
})
```
