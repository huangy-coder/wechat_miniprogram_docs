# wx.onMemoryWarning(function listener)

> 官方文档：[wx.onMemoryWarning(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/device/memory/wx.onMemoryWarning.html)
> 所属分类：[设备](../设备目录.md)
> 导航路径：设备 / 内存 / wx.onMemoryWarning
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.0.2 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：不支持

> 相关文档: [内存优化](https://developers.weixin.qq.com/miniprogram/dev/framework/performance/tips/runtime_memory.html)

## 功能描述

监听内存不足告警事件。

当 iOS/Android 向小程序进程发出内存警告时，触发该事件。触发该事件不意味小程序被杀，大部分情况下仅仅是告警，开发者可在收到通知后回收一些不必要资源避免进一步加剧内存紧张。

## 参数

### function listener

内存不足告警事件的监听函数

#### 参数

##### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| level | number | 内存告警等级，只有 Android 才有，对应系统宏定义 |

补充表：
| 合法值 | 说明 |
| --- | --- |
| 5 | TRIM_MEMORY_RUNNING_MODERATE |
| 10 | TRIM_MEMORY_RUNNING_LOW |
| 15 | TRIM_MEMORY_RUNNING_CRITICAL |

## 示例代码

```js
wx.onMemoryWarning(function () {
  console.log('onMemoryWarningReceive')
})
```
