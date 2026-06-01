# Object wx.getExptInfoSync(Array.<string> keys)

> 官方文档：[Object wx.getExptInfoSync(Array.<string> keys)](https://developers.weixin.qq.com/miniprogram/dev/api/data-analysis/wx.getExptInfoSync.html)
> 所属分类：[数据分析](数据分析目录.md)
> 导航路径：数据分析 / wx.getExptInfoSync
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.17.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：不支持

## 功能描述

给定实验参数数组，获取对应的实验参数值

## 参数

### Array.<string> keys

实验参数数组，不填则获取所有实验参数

## 返回值

### Object

结果对象，key 为传入的 keys 中的各项，value 为参数值

## 提示

假设实验参数有 `color`, `size`
调用 wx.getExptInfoSync() 会返回 `{color:'#fff',size:20}` 类似的结果
而 wx.getExptInfoSync(['color']) 则只会返回 `{color:'#fff'}`
