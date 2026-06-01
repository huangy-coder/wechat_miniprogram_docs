# Ndef

> 官方文档：[Ndef](https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/Ndef.html)
> 所属分类：[设备](../设备目录.md)
> 导航路径：设备 / NFC 读写 / Ndef
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.11.2 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> 相关文档: [近场通信 (NFC)](https://developers.weixin.qq.com/miniprogram/dev/framework/device/nfc.html)

Ndef 标签

## 方法

### Ndef.connect()

连接 NFC 标签

### Ndef.close()

断开连接

### Ndef.setTimeout(Object object)

设置超时时间

### Ndef.isConnected()

检查是否已连接

### Ndef.onNdefMessage(function callback)

监听 Ndef 消息

### Ndef.offNdefMessage(function callback)

取消监听 Ndef 消息

### Ndef.writeNdefMessage(Object object)

重写 Ndef 标签内容
