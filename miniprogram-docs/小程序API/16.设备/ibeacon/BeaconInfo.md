# BeaconInfo

> 官方文档：[BeaconInfo](https://developers.weixin.qq.com/miniprogram/dev/api/device/ibeacon/BeaconInfo.html)
> 所属分类：[设备](../设备目录.md)
> 导航路径：设备 / 蓝牙-信标(Beacon) / BeaconInfo
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 相关文档: [蓝牙信标 (Beacon)](https://developers.weixin.qq.com/miniprogram/dev/framework/device/beacon.html)

Beacon 设备

## 属性

### string uuid

Beacon 设备广播的 UUID

### number major

Beacon 设备的主 ID

### number minor

Beacon 设备的次 ID

### number proximity

表示设备距离的枚举值（仅iOS）

**proximity 的合法值**

| 值 | 说明 | 最低版本 |
| --- | --- | --- |
| 0 | 信号太弱不足以计算距离，或非 iOS 设备 |   |
| 1 | 十分近 |   |
| 2 | 比较近 |   |
| 3 | 远 |   |

### number accuracy

Beacon 设备的距离，单位 m。iOS 上，proximity 为 0 时，accuracy 为 -1。

### number rssi

表示设备的信号强度，单位 dBm
