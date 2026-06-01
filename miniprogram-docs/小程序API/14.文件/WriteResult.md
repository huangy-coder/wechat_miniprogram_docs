# WriteResult

> 官方文档：[WriteResult](https://developers.weixin.qq.com/miniprogram/dev/api/file/WriteResult.html)
> 所属分类：[文件](文件目录.md)
> 导航路径：文件 / WriteResult
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

文件写入结果。 通过 [FileSystemManager.writeSync](FileSystemManager.writeSync.md) 接口返回

## 属性

### number bytesWritten

实际被写入到文件中的字节数（注意，被写入的字节数不一定与被写入的字符串字符数相同）
