# ReadResult

> 官方文档：[ReadResult](https://developers.weixin.qq.com/miniprogram/dev/api/file/ReadResult.html)
> 所属分类：[文件](文件目录.md)
> 导航路径：文件 / ReadResult
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

文件读取结果。 通过 [FileSystemManager.readSync](FileSystemManager.readSync.md) 接口返回

## 属性

### number bytesRead

实际读取的字节数

### ArrayBuffer arrayBuffer

被写入的缓存区的对象，即接口入参的 arrayBuffer
