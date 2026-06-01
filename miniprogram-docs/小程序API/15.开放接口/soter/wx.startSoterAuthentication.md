# wx.startSoterAuthentication(Object object)

> 官方文档：[wx.startSoterAuthentication(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/soter/wx.startSoterAuthentication.html)
> 所属分类：[开放接口](../开放接口目录.md)
> 导航路径：开放接口 / 生物认证 / wx.startSoterAuthentication
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 1.5.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#异步-API-返回-Promise) 调用**：支持
> **小程序插件**：不支持
> **微信 鸿蒙 OS 版**：支持

> 相关文档: [生物认证](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/bio-auth.html)

## 功能描述

开始 SOTER 生物认证。验证流程请参考[说明](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/bio-auth.html)。

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| requestAuthModes | Array.<string> |   | 是 | 请求使用的可接受的生物认证方式 |
| challenge | string |   | 是 | 挑战因子。挑战因子为调用者为此次生物鉴权准备的用于签名的字符串关键识别信息，将作为 `resultJSON` 的一部分，供调用者识别本次请求。例如：如果场景为请求用户对某订单进行授权确认，则可以将订单号填入此参数。 |
| authContent | string | '' | 否 | 验证描述，即识别过程中显示在界面上的对话框提示内容 |
| success | function |   | 否 | 接口调用成功的回调函数 |
| fail | function |   | 否 | 接口调用失败的回调函数 |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

补充表：
| 合法值 | 说明 |
| --- | --- |
| fingerPrint | 指纹识别 |
| facial | 人脸识别 |
| speech | 声纹识别（暂未支持） |

#### object.success 回调函数

##### 参数

###### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| authMode | string | 生物认证方式 |
| resultJSON | string | 在设备安全区域（TEE）内获得的本机安全信息（如TEE名称版本号等以及防重放参数）以及本次认证信息（仅Android支持，本次认证的指纹ID）。具体说明见下文 |
| resultJSONSignature | string | 用SOTER安全密钥对 `resultJSON` 的签名(SHA256 with RSA/PSS, saltlen=20) |
| errCode | number | 错误码 |
| errMsg | string | 错误信息 |

## resultJSON 说明

此数据为设备TEE中，将传入的challenge和TEE内其他安全信息组成的数据进行组装而来的JSON，对下述字段的解释如下表。例子如下：

| 字段名 | 说明 |
| --- | --- |
| raw | 调用者传入的challenge |
| fid | （仅Android支持）本次生物识别认证的生物信息编号（如指纹识别则是指纹信息在本设备内部编号） |
| counter | 防重放特征参数 |
| tee_n | TEE名称（如高通或者trustonic等） |
| tee_v | TEE版本号 |
| fp_n | 指纹以及相关逻辑模块提供商（如FPC等） |
| fp_v | 指纹以及相关模块版本号 |
| cpu_id | 机器唯一识别ID |
| uid | 概念同Android系统定义uid，即应用程序编号 |

```json
{
  "raw":"msg",
  "fid":"2",
  "counter":123,
  "tee_n":"TEE Name",
  "tee_v":"TEE Version",
  "fp_n":"Fingerprint Sensor Name",
  "fp_v":"Fingerprint Sensor Version",
  "cpu_id":"CPU Id",
  "uid":"21"
}
```

## 示例代码

[在开发者工具中预览效果](https://developers.weixin.qq.com/s/q3tCKkmJ7g2e)

```js
wx.startSoterAuthentication({
   requestAuthModes: ['fingerPrint'],
   challenge: '123456',
   authContent: '请用指纹解锁',
   success(res) {
   }
})
```
