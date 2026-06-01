# 修改动态消息

> 官方文档：[修改动态消息](https://developers.weixin.qq.com/miniprogram/dev/server/API/mp-message-management/updatable-message/api_setupdatablemsg.html)
> 所属分类：[消息相关](../../消息相关目录.md)
> 导航路径：消息相关 / 动态消息 / 修改动态消息
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

[调试诊断](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_tools)

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：setUpdatableMsg

该接口用于修改被分享的动态消息。详见[动态消息](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/share/updatable-message.html)。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/cgi-bin/message/wxopen/updatablemsg/send?access_token=ACCESS_TOKEN
```

### 云调用

- 调用方法：updatableMessage.setUpdatableMsg
- 调用说明：请求参数改为驼峰命名，具体看下文调用示例
- 出入参和 HTTPS 调用相同，调用方式可查看 [云调用](https://developers.weixin.qq.com/doc/oplatform/developers/dev/cloudCall) 说明文档。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：18
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

### Body.template_info Object Payload

动态消息对应的模板信息

### Body.template_info.parameter_list(Array) Object Payload

模板中需要修改的参数

## 3. 返回参数

### 返回体 Response Payload

## 4. 枚举信息

### Body.target_state Enum

动态消息修改后的状态

## 5. 注意事项

### name 的合法值

| 值 | 说明 |
| --- | --- |
| member_count | target_state = 0 时必填，文字内容模板中 member_count 的值 |
| room_limit | target_state = 0 时必填，文字内容模板中 room_limit 的值 |
| path | target_state = 1 时必填，点击「进入」启动小程序时使用的路径。对于小游戏，没有页面的概念，可以用于传递查询字符串（query），如 "?foo=bar" |
| version_type | target_state = 1 时必填，点击「进入」启动小程序时使用的版本。有效参数值为：develop（开发版），trial（体验版），release（正式版） |

### 消息状态

消息有两个状态（target_state），分别有其对应的文字内容和颜色。文字内容模板和颜色不支持变更。

| 状态 | 文字内容 | 颜色 | 允许转移的状 |
| --- | --- | --- | --- |
| 0 | "成员正在加入，当前 {member_count}/{room_limit} 人" | #FA9D39 | 0, 1 |
| 1 | "已开始" | #CCCCCC | 无 |

活动的默认有效期是 24 小时。活动结束后，消息内容会变成统一的样式：

- 文字内容：“已结束”
- 文字颜色：#00ff00

## 6. 代码示例

### 6.1 HTTPS调用

请求示例

```json
{
  "activity_id": "966_NGiqxxxxxxxxxx...xxxxxxxxE33BlwX",
  "target_state": 0,
  "template_info": {
    "parameter_list": [
      {
        "name": "member_count",
        "value": "2"
      },
      {
        "name": "room_limit",
        "value": "5"
      }
    ]
  }
}
```

返回示例

```json
{
"errcode": 0, 
"errmsg": "ok"
}
```

### 6.2 云调用示例

请求示例

```js
const cloud = require('wx-server-sdk');
cloud.init({
  env: cloud.DYNAMIC_CURRENT_ENV,
});
exports.main = async (event, context) => {
  try {
    const result = await cloud.openapi.updatableMessage.setUpdatableMsg({
      "activityId": "966_NGiqxxxxxxxxxx...xxxxxxxxE33BlwX",
      "targetState": 0,
      "templateInfo": {
        "parameterList": [
          {
            "name": "member_count",
            "value": "2"
          },
          {
            "name": "room_limit",
            "value": "5"
          }
        ]
      }
    });
    return result;
  } catch (err) {
    return err;
  }
};
```

返回示例

```json
{
    "errCode": 0,
    "errMsg": ""
}
```

## 7. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 8. 适用范围

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

- ✔：该账号可调用此接口。
- 其他未明确声明的账号类型，如无特殊说明，均不可调用此接口。
