# IsoDep

> 官方文档：[IsoDep](https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/IsoDep.html)
> 所属分类：[设备](../设备目录.md)
> 导航路径：设备 / NFC 读写 / IsoDep
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.11.2 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> 相关文档: [近场通信 (NFC)](https://developers.weixin.qq.com/miniprogram/dev/framework/device/nfc.html)

IsoDep 标签

## 方法

### IsoDep.connect()

连接 NFC 标签

### IsoDep.close()

断开连接

### IsoDep.setTimeout(Object object)

设置超时时间

### IsoDep.isConnected()

检查是否已连接

### IsoDep.getMaxTransceiveLength()

获取最大传输长度

### IsoDep.transceive(Object object)

发送数据

### IsoDep.getHistoricalBytes()

获取复位信息
