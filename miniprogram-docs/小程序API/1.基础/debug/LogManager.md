# LogManager

> 官方文档：[LogManager](https://developers.weixin.qq.com/miniprogram/dev/api/base/debug/LogManager.html)
> 所属分类：[基础](../基础目录.md)
> 导航路径：基础 / 调试 / LogManager
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

日志管理器实例，可以通过 [wx.getLogManager](wx.getLogManager.md) 获取。

## 方法

### LogManager.debug()

写 debug 日志

### LogManager.info()

写 info 日志

### LogManager.log()

写 log 日志

### LogManager.warn()

写 warn 日志

## 使用说明

最多保存5M的日志内容，超过5M后，旧的日志内容会被删除。

对于**小程序**，用户可以通过使用 [button](https://developers.weixin.qq.com/miniprogram/dev/component/button.html) 组件的 `open-type="feedback"` 来上传打印的日志。

对于**小游戏**，用户可以通过使用 [wx.createFeedbackButton](https://developers.weixin.qq.com/miniprogram/dev/api/base/debug/(wx.createFeedbackButton)) 来创建上传打印的日志的按钮。

开发者可以通过小程序管理后台左侧菜单“反馈管理”页面查看相关打印日志。
 

基础库默认会把 `App`、`Page` 的生命周期函数和 `wx` 命名空间下的函数调用写入日志。
