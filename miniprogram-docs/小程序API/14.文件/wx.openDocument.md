# wx.openDocument(Object object)

> 官方文档：[wx.openDocument(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/file/wx.openDocument.html)
> 所属分类：[文件](文件目录.md)
> 导航路径：文件 / wx.openDocument
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#异步-API-返回-Promise) 调用**：支持
> **小程序插件**：支持，需要小程序基础库版本不低于 [2.15.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持
> **微信 鸿蒙 OS 版**：支持

> 相关文档: [文件系统](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/file-system.html)

## 功能描述

新开页面打开文档。微信客户端 `7.0.12` 版本前默认显示右上角菜单按钮，之后的版本默认不显示，需主动传入 `showMenu`。

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| filePath | string |   | 是 | 文件路径 (本地路径) ，可通过 downloadFile 获得 |   |
| showMenu | boolean | false | 否 | 是否显示右上角菜单 | [2.11.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| fileType | string |   | 否 | 文件类型，指定文件类型打开文件 | [1.4.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| success | function |   | 否 | 接口调用成功的回调函数 |   |
| fail | function |   | 否 | 接口调用失败的回调函数 |   |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |   |

补充表：
| 合法值 | 说明 |
| --- | --- |
| doc | doc 格式 |
| docx | docx 格式 |
| xls | xls 格式 |
| xlsx | xlsx 格式 |
| ppt | ppt 格式 |
| pptx | pptx 格式 |
| pdf | pdf 格式 |

## 示例代码

```javascript
wx.downloadFile({
  // 示例 url，并非真实存在
  url: 'http://example.com/somefile.pdf',
  success: function (res) {
    const filePath = res.tempFilePath
    wx.openDocument({
      filePath: filePath,
      success: function (res) {
        console.log('打开文档成功')
      }
    })
  }
})
```
