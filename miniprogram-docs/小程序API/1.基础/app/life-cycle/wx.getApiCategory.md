# string wx.getApiCategory()

> 官方文档：[string wx.getApiCategory()](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/life-cycle/wx.getApiCategory.html)
> 所属分类：[基础](../../基础目录.md)
> 导航路径：基础 / 小程序 / 生命周期 / wx.getApiCategory
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.33.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：不支持

## 功能描述

获取当前 API 类别

## 返回值

### string

API 类别

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
