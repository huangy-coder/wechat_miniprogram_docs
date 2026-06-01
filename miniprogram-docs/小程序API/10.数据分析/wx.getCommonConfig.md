# wx.getCommonConfig(Object object)

> 官方文档：[wx.getCommonConfig(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/data-analysis/wx.getCommonConfig.html)
> 所属分类：[数据分析](数据分析目录.md)
> 导航路径：数据分析 / wx.getCommonConfig
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.33.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#%E5%BC%82%E6%AD%A5-API-%E8%BF%94%E5%9B%9E-Promise) 调用**：不支持
> **小程序插件**：不支持
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持
> **微信 鸿蒙 OS 版**：支持

## 功能描述

给定实验参数数组，获取对应的实验参数值。

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| keys | Array.<string> |   | 否 | 需要获取的数据指标的对象数组，每个string的格式约定：配置类型_分表key |
| mode | number |   | 是 | 0：通用配置模式 1：实验模式, 参数与返回结果的使用等效于接口[wx.getExptInfoSync](wx.getExptInfoSync.md) |
| success | function |   | 否 | 接口调用成功的回调函数 |
| fail | function |   | 否 | 接口调用失败的回调函数 |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

#### object.success 回调函数

##### 参数

###### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | 错误码 |
| errmsg | string | 错误信息 |
| conf_type | number | 配置类型, 1-表类型 2-kv类型 |
| conf | string | 根据conf_type来确定conf内容,conf_type为1时conf是一个json数组, 类似"[{xxx},{xxx}]", 每一项对应表类型每一行配置内容, 其中conf_type为2时conf是一个json对象，类似"{xxxx}" |
| expire_sec | number | 过期时间,单位秒. 0表示当次有效 |

## 示例代码

```js
  wx.getCommonConfig({
      keys:["key1", "key2"],
      mode: 0,
      success: (res)=>{
        console.log("success")
        console.log(res)
      },
    fail: (res)=>{
      console.log("fail")
      console.log(res)
    }})
```
