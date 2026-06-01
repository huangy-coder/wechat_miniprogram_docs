# wx.getDeviceBenchmarkInfo(Object object)

> 官方文档：[wx.getDeviceBenchmarkInfo(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/base/system/wx.getDeviceBenchmarkInfo.html)
> 所属分类：[基础](../基础目录.md)
> 导航路径：基础 / 系统 / wx.getDeviceBenchmarkInfo
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 3.4.5 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#%E5%BC%82%E6%AD%A5-API-%E8%BF%94%E5%9B%9E-Promise) 调用**：不支持
> **小程序插件**：不支持
> **微信 鸿蒙 OS 版**：支持

## 功能描述

获取设备性能得分和机型档位数据

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

| 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| benchmarkLevel | number | 设备性能等级。-1（性能未知），>=1（设备性能值，该值越高，设备性能越好）<br>注意：<br>1. 设备的benchmarkLevel值不会随着时间的推移而变化，移动端设备目前最高不超过50 | [3.4.5](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| modelLevel | number | 设备机型档位。0（档位未知），1（高档机），2（中档机），3（低档机）<br> 注意：设备的机型档位会随着时间的推移而变化，因此在使用时请谨慎对待；若业务逻辑依赖于机型档位，但担心受到机型档位变化的影响，请参考[设备档位映射文档](https://developers.weixin.qq.com/minigame/dev/guide/performance/perf-benchmarkLevel.html)自行判断机型档位 | [3.4.5](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |

## 示例代码

```js
wx.getDeviceBenchmarkInfo({
  success (res) {
    console.log(res.benchmarkLevel)
    console.log(res.modelLevel)
  }
})
```
