# SocketTask

> 官方文档：[SocketTask](https://developers.weixin.qq.com/miniprogram/dev/api/network/websocket/SocketTask.html)
> 所属分类：[网络](../网络目录.md)
> 导航路径：网络 / WebSocket / SocketTask
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 1.7.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> 相关文档: [网络使用说明](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/network.html)、[局域网通信](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/mDNS.html)

WebSocket 任务，可通过 wx.connectSocket() 接口创建返回

## 方法

### SocketTask.send(Object object)

通过 WebSocket 连接发送数据

### SocketTask.close(Object object)

关闭 WebSocket 连接

### SocketTask.onOpen(function listener)

监听 WebSocket 连接打开事件

### SocketTask.onClose(function listener)

监听 WebSocket 连接关闭事件

### SocketTask.onError(function listener)

监听 WebSocket 错误事件

### SocketTask.onMessage(function listener)

监听 WebSocket 接收到服务器的消息事件
