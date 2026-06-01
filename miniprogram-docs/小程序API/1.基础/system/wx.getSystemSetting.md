# Object wx.getSystemSetting()

> 官方文档：[Object wx.getSystemSetting()](https://developers.weixin.qq.com/miniprogram/dev/api/base/system/wx.getSystemSetting.html)
> 所属分类：[基础](../基础目录.md)
> 导航路径：基础 / 系统 / wx.getSystemSetting
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.20.1 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持，需要小程序基础库版本不低于 [2.21.3](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持
> **微信 鸿蒙 OS 版**：支持

## 功能描述

获取设备设置

## 返回值

### Object

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| bluetoothEnabled | boolean | 蓝牙的系统开关 |
| locationEnabled | boolean | 地理位置的系统开关 |
| wifiEnabled | boolean | Wi-Fi 的系统开关 |
| deviceOrientation | string | 设备方向（注意：IOS客户端横屏游戏获取deviceOrientation可能不准，建议以屏幕宽高为准） |

补充表：
| 合法值 | 说明 |
| --- | --- |
| portrait | 竖屏 |
| landscape | 横屏 |

## 示例代码

```js
const systemSetting = wx.getSystemSetting()

console.log(systemSetting.bluetoothEnabled)
console.log(systemSetting.deviceOrientation)
console.log(systemSetting.locationEnabled)
console.log(systemSetting.wifiEnabled)
```
