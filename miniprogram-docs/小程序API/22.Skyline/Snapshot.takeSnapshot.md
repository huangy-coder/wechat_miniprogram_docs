# Snapshot.takeSnapshot(Object object)

> 官方文档：[Snapshot.takeSnapshot(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/skyline/Snapshot.takeSnapshot.html)
> 所属分类：[Skyline](Skyline目录.md)
> 导航路径：Skyline / Snapshot / Snapshot.takeSnapshot
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 3.0.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#%E5%BC%82%E6%AD%A5-API-%E8%BF%94%E5%9B%9E-Promise) 调用**：不支持
> **小程序插件**：支持
> **微信 鸿蒙 OS 版**：支持

> 相关文档: [snapshot](https://developers.weixin.qq.com/miniprogram/dev/component/snapshot.html)

## 功能描述

对 snapshot 组件子树进行截图

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| type | String |   | 是 | 截图导出类型，'file' 保存到临时文件目录或 'arraybuffer' 返回图片二进制数据，默认值为 'file' |
| format | String |   | 是 | 截图文件格式，'rgba' 或 'png'，默认值为 'png' |
| success | function |   | 否 | 接口调用成功的回调函数 |
| fail | function |   | 否 | 接口调用失败的回调函数 |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

#### object.success 回调函数

##### 参数

###### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| tempFilePath | String | 截图保存的临时文件路径，当 type 为 file 该字段生效 |
| data | ArrayBuffer | 截图对应的二进制数据，当 type 为 arraybuffer 该字段生效 |
