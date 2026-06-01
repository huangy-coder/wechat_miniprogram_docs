# UpdateManager.onCheckForUpdate(function listener)

> 官方文档：[UpdateManager.onCheckForUpdate(function listener)](https://developers.weixin.qq.com/miniprogram/dev/api/base/update/UpdateManager.onCheckForUpdate.html)
> 所属分类：[基础](../基础目录.md)
> 导航路径：基础 / 更新 / UpdateManager / UpdateManager.onCheckForUpdate
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **小程序插件**：不支持

## 功能描述

监听向微信后台请求检查更新结果事件。微信在小程序每次启动（包括热启动）时自动检查更新，不需由开发者主动触发。

## 参数

### function listener

向微信后台请求检查更新结果事件的监听函数

#### 参数

##### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| hasUpdate | boolean | 是否有新版本 |

## 示例代码

[示例代码](UpdateManager.md)
