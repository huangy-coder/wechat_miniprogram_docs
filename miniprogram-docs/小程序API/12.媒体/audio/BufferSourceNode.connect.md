# BufferSourceNode.connect(AudioNode| AudioParam destination)

> 官方文档：[BufferSourceNode.connect(AudioNode| AudioParam destination)](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/BufferSourceNode.connect.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 音频 / BufferSourceNode / BufferSourceNode.connect
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **小程序插件**：不支持
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持

## 功能描述

连接到一个指定目标。这个指定的目标可能是另一个 AudioNode（从而将音频数据引导到下一个指定节点）或一个AudioParam, 以便上一个节点的输出数据随着时间流逝能自动地对下一个参数值进行改变

## 参数

### AudioNode| AudioParam destination

要建立连接的目标节点
