# wx.onApiCategoryChange(function listener)

> 官方文档：[wx.onApiCategoryChange(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/life-cycle/wx.onApiCategoryChange.html)
> 所属分类：[基础](../../基础目录.md)
> 导航路径：基础 / 小程序 / 生命周期 / wx.onApiCategoryChange
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.33.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：不支持

## 功能描述

监听 API 类别变化事件

## 参数

### function listener

API 类别变化事件的监听函数

#### 参数

##### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| apiCategory | number | API 类别 |

补充表：
| 合法值 | 说明 |
| --- | --- |
| default | 默认类别 |
| nativeFunctionalized | 原生功能化，视频号直播商品、商品橱窗等场景打开的小程序 |
| browseOnly | 仅浏览，朋友圈快照页等场景打开的小程序 |
| embedded | 内嵌，通过打开半屏小程序能力打开的小程序 |
| chatTool | 聊天工具打开小程序 |

## 不同 apiCategory 场景下的 API 限制

`X` 表示 API 被限制无法使用；不在表格中的 API 不限制。

|   | default | nativeFunctionalized | browseOnly | embedded | chatTool |
| --- | --- | --- | --- | --- | --- |
| openSetting |   |   | `X` |   |   |
| <button open-type="share"> |   | `X` | `X` | `X` | `X` |
| <button open-type="feedback"> |   |   | `X` |   |   |
| <button open-type="open-setting"> |   |   | `X` |   |   |
| navigateToMiniProgram |   | `X` | `X` |   | `X` |
| openEmbeddedMiniProgram |   | `X` | `X` | `X` | `X` |
| openOfficialAccountArticle |   |   |   |   | `X` |
| openChannelsUserProfile |   |   |   |   | `X` |
| ad |   |   |   |   | `X` |
| ad-custom |   |   |   |   | `X` |
| 小程序菜单分享 |   |   |   |   | `X` |

## 示例代码

```js
const func = function (res) {
  console.log(res.apiCategory)
}
wx.onApiCategoryChange(func)
// 取消监听
wx.offApiCategoryChange(func)
```
