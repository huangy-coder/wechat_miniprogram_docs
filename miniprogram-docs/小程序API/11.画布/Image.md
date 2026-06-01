# Image

> 官方文档：[Image](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/Image.html)
> 所属分类：[画布](画布目录.md)
> 导航路径：画布 / Image
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.7.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> 相关文档: [画布指南](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/canvas.html)、[canvas 组件介绍](https://developers.weixin.qq.com/miniprogram/dev/component/canvas.html)

图片对象

## 属性

### string src

图片的 URL。v2.11.0 起支持传递 base64 Data URI

### number width

图片的真实宽度

### number height

图片的真实高度

### string referrerPolicy

> 基础库 2.13.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

`origin`: 发送完整的referrer; `no-referrer`: 不发送。格式固定为 `https://servicewechat.com/{appid}/{version}/page-frame.html`，其中 {appid} 为小程序的 appid，{version} 为小程序的版本号，版本号为 0 表示为开发版、体验版以及审核版本，版本号为 devtools 表示为开发者工具，其余为正式版本；

### function onload

图片加载完成后触发的回调函数

### function onerror

图片加载发生错误后触发的回调函数
