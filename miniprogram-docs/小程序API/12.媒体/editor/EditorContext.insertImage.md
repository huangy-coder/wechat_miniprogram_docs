# EditorContext.insertImage(Object object)

> 官方文档：[EditorContext.insertImage(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/media/editor/EditorContext.insertImage.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 富文本 / EditorContext / EditorContext.insertImage
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.7.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#%E5%BC%82%E6%AD%A5-API-%E8%BF%94%E5%9B%9E-Promise) 调用**：不支持
> **小程序插件**：支持

> 相关文档: [editor 组件](https://developers.weixin.qq.com/miniprogram/dev/component/editor.html)

## 功能描述

插入图片。

地址为临时文件时，获取的编辑器html格式内容中 <img> 标签增加属性 data-local，delta 格式内容中图片 attributes 属性增加 data-local 字段，该值为传入的临时文件地址。

开发者可选择在提交阶段上传图片到服务器，获取到网络地址后进行替换。替换时对于html内容应替换掉 <img> 的 src 值，对于 delta 内容应替换掉 `insert { image: abc }` 值。

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| src | string |   | 是 | 图片地址，仅支持 http(s)、base64、云图片(2.8.0)、临时文件(2.8.3)。 |
| nowrap | boolean | false | 否 | 插入图片后是否自动换行，默认换行 |
| alt | string |   | 否 | 图像无法显示时的替代文本 |
| width | string |   | 否 | 图片宽度（pixels/百分比) |
| height | string |   | 否 | 图片高度 (pixels/百分比) |
| extClass | string |   | 否 | 添加到图片 img 标签上的类名 |
| data | Object |   | 否 | data 被序列化为 name=value;name1=value2 的格式挂在属性 data-custom 上 |
| success | function |   | 否 | 接口调用成功的回调函数 |
| fail | function |   | 否 | 接口调用失败的回调函数 |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

## 示例代码

```javascript
this.editorCtx.insertImage({
  src: 'xx',
  width: '100px',
  height: '50px',
  extClass: className
})
```
