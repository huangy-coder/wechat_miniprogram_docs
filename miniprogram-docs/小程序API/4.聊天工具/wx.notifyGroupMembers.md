# wx.notifyGroupMembers(Object object)

> 官方文档：[wx.notifyGroupMembers(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/chattool/wx.notifyGroupMembers.html)
> 所属分类：[聊天工具](聊天工具目录.md)
> 导航路径：聊天工具 / wx.notifyGroupMembers
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 3.7.8 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#异步-API-返回-Promise) 调用**：支持
> **小程序插件**：不支持

> 相关文档: [聊天工具模式](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/chatTool.html)

## 功能描述

提醒用户完成任务，标题长度不超过 30 个字符，支持中英文和数字，中文算2个字符。

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| title | string |   | 是 | 文字链标题，发送的内容将由微信拼接为：@的成员列表+“请完成：”/"请参与："+打开小程序的文字链，如「@alex @cindy 请完成：团建报名统计」。 |
| members | Array.<string> |   | 是 | 需要提醒的用户 group_openid 列表 |
| entrancePath | string |   | 是 | 文字链跳转路径 |
| type | string | complete | 否 | 展示的动词 |
| success | function |   | 否 | 接口调用成功的回调函数 |
| fail | function |   | 否 | 接口调用失败的回调函数 |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

补充表：
| 合法值 | 说明 |
| --- | --- |
| participate | 请参与 |
| complete | 请完成 |

## 示例代码

```javascript
  // 最终聊天内显示 @alex @cindy 请完成：团建报名统计
  wx.notifyGroupMembers({
    title: '团建报名统计',
    members: ['alex', 'cindy],
    entrancePath: '/path/to/page',
    type: 'complete',
  })
```
