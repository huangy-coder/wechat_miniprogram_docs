# Object wx.getDeviceInfo()

> 官方文档：[Object wx.getDeviceInfo()](https://developers.weixin.qq.com/miniprogram/dev/api/base/system/wx.getDeviceInfo.html)
> 所属分类：[基础](../基础目录.md)
> 导航路径：基础 / 系统 / wx.getDeviceInfo
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.20.1 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持，需要小程序基础库版本不低于 [2.21.3](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持
> **微信 鸿蒙 OS 版**：支持

## 功能描述

获取设备基础信息

## 返回值

### Object

| 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| abi | string | 应用（微信APP）二进制接口类型（仅 Android 支持） |   |
| deviceAbi | string | 设备二进制接口类型（仅 Android 支持） | [2.25.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| benchmarkLevel | number | 设备性能等级（仅 Android 支持）。取值为：-2 或 0（该设备无法运行小游戏），-1（性能未知），>=1（设备性能值，该值越高，设备性能越好，目前最高不到50）<br> 注意：从基础库3.4.5开始，本返回值停止维护，请使用[wx.getDeviceBenchmarkInfo](wx.getDeviceBenchmarkInfo.md)获取设备性能等级 |   |
| brand | string | 设备品牌 |   |
| model | string | 设备型号。新机型刚推出一段时间会显示unknown，微信会尽快进行适配。 |   |
| system | string | 操作系统及版本 |   |
| platform | string | 客户端平台 |   |
| cpuType | string | 设备 CPU 型号（仅 Android 支持）（Tips: GPU 型号可通过 WebGLRenderingContext.getExtension('WEBGL_debug_renderer_info') 来获取） | [2.29.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| memorySize | string | 设备内存大小，单位为 MB | [2.30.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |

补充表：
| 合法值 | 说明 |
| --- | --- |
| ios | iOS微信（包含 iPhone、iPad） |
| android | Android微信 |
| ohos | HarmonyOS 手机端微信 |
| ohos_pc | HarmonyOS PC微信 |
| windows | Windows微信 |
| mac | macOS微信 |
| devtools | 微信开发者工具 |

## 示例代码

```js
const deviceInfo = wx.getDeviceInfo()

console.log(deviceInfo.abi)
console.log(deviceInfo.benchmarkLevel)
console.log(deviceInfo.brand)
console.log(deviceInfo.model)
console.log(deviceInfo.platform)
console.log(deviceInfo.system)
```
