# wx.getGroupEnterInfo(Object object)

> 官方文档：[wx.getGroupEnterInfo(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/group/wx.getGroupEnterInfo.html)
> 所属分类：[开放接口](../开放接口目录.md)
> 导航路径：开放接口 / 微信群 / wx.getGroupEnterInfo
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.10.4 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#%E5%BC%82%E6%AD%A5-API-%E8%BF%94%E5%9B%9E-Promise) 调用**：不支持
> **小程序插件**：不支持
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持
> **微信 鸿蒙 OS 版**：支持

## 功能描述

获取微信群聊场景下的小程序启动信息。群聊场景包括群聊小程序消息卡片、群待办、群工具。可用于获取当前群的 opengid。

## 注意事项

- 基础库 v2.10.4 开始支持获取群工具小程序启动信息
- 基础库 v2.17.3 开始支持获取群聊小程序消息卡片、群待办小程序启动信息
- 基础库 v3.7.8 支持获取单聊群启动信息，获取的群(含单聊)唯一标识，可用于[聊天工具模式](../../4.聊天工具/wx.openChatTool.md)。

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| allowSingleChat | boolean | false | 否 | 开启后单聊下返回 open_single_roomid | [3.7.8](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| needGroupOpenID | boolean | false | 否 | 开启后返回用户在群(含单聊)下的 group_openid | [3.7.8](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
| success | function |   | 否 | 接口调用成功的回调函数 |   |
| fail | function |   | 否 | 接口调用失败的回调函数 |   |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |   |

#### object.success 回调函数

##### 参数

###### Object res

| 属性 | 类型 | 说明 | 最低版本 |
| --- | --- | --- | --- |
| errMsg | string | 错误信息 |   |
| encryptedData | string | 包括敏感数据在内的完整转发信息的加密数据，详细见[加密数据解密算法](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/signature.html) |   |
| iv | string | 加密算法的初始向量，详细见[加密数据解密算法](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/signature.html) |   |
| cloudID | string | 敏感数据对应的云 ID，开通[云开发](https://developers.weixin.qq.com/miniprogram/dev/wxcloudservice/wxcloud/basis/getting-started.html)的小程序才会返回，可通过云调用直接获取开放数据，详细见[云调用直接获取开放数据](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/signature.html#method-cloud) | [2.7.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |

## 错误

| 错误码 | 错误信息 | 说明 |
| --- | --- | --- |
| 40097 |   | 场景错误 |
| 65206 |   | 用户已不在该群内 |

## 示例代码

```js
wx.getGroupEnterInfo({
  success(res) {
    // res
    {
      errMsg: 'getGroupEnterInfo:ok',
      encryptedData: '',
      iv: ''
    }
  },
  fail() {

  }
})
```

敏感数据有两种获取方式，一是使用 [加密数据解密算法](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/signature.html#%E5%8A%A0%E5%AF%86%E6%95%B0%E6%8D%AE%E8%A7%A3%E5%AF%86%E7%AE%97%E6%B3%95) 。
获取得到的开放数据为以下 json 结构（其中 opengid 为当前群的唯一标识）：

```json
{
 "opengid": "OPENGID",       // 多聊群下返回的群唯一标识
 "open_single_roomid": "",   // 单聊群下返回的群唯一标识
 "group_openid": "",         // 用户在当前群的唯一标识
 "chat_type": 3,             // 聊天室类型
}
```

## Tips

- 如需要展示群名称，小程序可以使用[开放数据组件](https://developers.weixin.qq.com/miniprogram/dev/component/open-data.html)
- 小游戏可以通过 `wx.getGroupInfo` 接口获取群名称
