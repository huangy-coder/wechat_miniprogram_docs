# wx.shareToOfficialAccount(Object object)

> 官方文档：[wx.shareToOfficialAccount(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/share/wx.shareToOfficialAccount.html)
> 所属分类：[转发](转发目录.md)
> 导航路径：转发 / wx.shareToOfficialAccount
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 3.9.2 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#%E5%BC%82%E6%AD%A5-API-%E8%BF%94%E5%9B%9E-Promise) 调用**：不支持
> **需要页面权限**：当前是插件页面时，宿主小程序不能调用该接口，反之亦然
> **小程序插件**：不支持

## 功能描述

支持拉起贴图发表页，用户可将图片与文字内容发表为贴图。

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| title | string |   | 是 | 贴图的标题 |   |
| content | string |   | 否 | 贴图的正文 |   |
| tags | Array.<string> |   | 否 | 贴图的标签，上限10个 |   |
| images | Array.<string> |   | 否 | 贴图的图片，必须为本地路径或临时路径 |   |
| path | string |   | 否 | 开发者自定义小程序路径 |   |
| recommendLink | string |   | 否 | 贴图链接卡片字段，暂时只支持小程序短链 | [3.16.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| success | function |   | 否 | 接口调用成功的回调函数 |   |
| fail | function |   | 否 | 接口调用失败的回调函数 |   |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |   |

#### object.success 回调函数

##### 参数

###### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| status | string | 贴图发表状态 |
| postUrl | string | 贴图发表后的文章链接，仅在success回调中返回，并且只有在发表成功后链接才可访问 |

## 示例代码

```javascript
wx.shareToOfficialAccount({
  title: '标题',
  content: '正文',
  tags: ['标签1', '标签2'],
  success: (res) => {
    // 贴图发表成功时触发
    console.log(res)
  },
  fail: (err) => {
    // 用户主动退出贴图发表页时触发
    console.log(err)
  },
  complete: (res) => {
    // 统计接口总共调用次数
    console.log(res)
  },
})
```

## 推荐图标

推荐使用贴图品牌图标作为该功能按钮，可使用下列高清素材：
