视图容器 /cover-image /

目前[原生组件](https://developers.weixin.qq.com/miniprogram/dev/component/native-component.html)均已支持同层渲染，建议使用 [image](https://developers.weixin.qq.com/miniprogram/dev/component/image.html) 替代

> 基础库 1.4.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **微信 Windows 版**：支持
>
> **微信 Mac 版**：支持
>
> **微信 鸿蒙 OS 版**：支持

渲染框架支持情况：Skyline （使用最新 [Nightly](https://developers.weixin.qq.com/miniprogram/dev/devtools/nightly.html) 工具调试）、WebView

## [#](https://developers.weixin.qq.com/miniprogram/dev/component/cover-image.html#%E5%8A%9F%E8%83%BD%E6%8F%8F%E8%BF%B0) 功能描述

覆盖在原生组件之上的图片视图。

可覆盖的原生组件同[cover-view](https://developers.weixin.qq.com/miniprogram/dev/component/cover-view.html)，支持嵌套在[cover-view](https://developers.weixin.qq.com/miniprogram/dev/component/cover-view.html)里。

## [#](https://developers.weixin.qq.com/miniprogram/dev/component/cover-image.html#%E9%80%9A%E7%94%A8%E5%B1%9E%E6%80%A7) 通用属性

| 属性            | 类型        | 默认值      | 必填                                                         | 说明                                                         | 最低版本                                                     |
| --------------- | ----------- | ----------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| src             | string      | 否          | 图标路径，支持临时路径、网络地址（1.6.0起支持）、云文件ID（2.2.3起支持）。 | [1.4.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |                                                              |
| referrer-policy | string      | no-referrer | 否                                                           | 格式固定为 `https://servicewechat.com/{appid}/{version}/page-frame.html`，其中 {appid} 为小程序的 appid，{version} 为小程序的版本号，版本号为 0 表示为开发版、体验版以及审核版本，版本号为 devtools 表示为开发者工具，其余为正式版本； | [2.13.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| 合法值          |             |             |                                                              |                                                              |                                                              |
| bindload        | eventhandle | 否          | 图片加载成功时触发                                           | [2.1.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |                                                              |
| binderror       | eventhandle | 否          | 图片加载失败时触发                                           | [2.1.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |                                                              |

#### [#](https://developers.weixin.qq.com/miniprogram/dev/component/cover-image.html#%E6%94%AF%E6%8C%81%E7%9A%84%E6%A0%BC%E5%BC%8F) 支持的格式

| 格式   | iOS  | Android |
| ------ | ---- | ------- |
| JPG    | √    | √       |
| PNG    | √    | √       |
| SVG    | x    | x       |
| WEBP   | √    | √       |
| GIF    | √    | √       |
| BASE64 | x    | x       |