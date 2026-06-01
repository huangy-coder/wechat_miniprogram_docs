# 发送订阅消息

> 官方文档：[发送订阅消息](https://developers.weixin.qq.com/miniprogram/dev/server/API/mp-message-management/subscribe-message/api_sendmessage.html)
> 所属分类：[消息相关](../../消息相关目录.md)
> 导航路径：消息相关 / 订阅消息 / 发送订阅消息
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：sendMessage

该接口用于发送订阅消息。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/cgi-bin/message/subscribe/send?access_token=ACCESS_TOKEN
```

### 云调用

- 调用方法：subscribeMessage.send
- 出入参和 HTTPS 调用相同，调用方式可查看 [云调用](https://developers.weixin.qq.com/doc/oplatform/developers/dev/cloudCall) 说明文档。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：18
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

## 3. 返回参数

### 返回体 Response Payload

## 4. 注意事项

#### 订阅消息参数值内容限制说明

| 参数类别 | 参数说明 | 参数值限制 | 说明 |
| --- | --- | --- | --- |
| thing.DATA | 事物 | 20个以内字符 | 可汉字、数字、字母或符号组合 |
| number.DATA | 数字 | 32位以内数字 | 只能数字，可带小数 |
| letter.DATA | 字母 | 32位以内字母 | 只能字母 |
| symbol.DATA | 符号 | 5位以内符号 | 只能符号 |
| character_string.DATA | 字符串 | 32位以内数字、字母或符号 | 可数字、字母或符号组合 |
| time.DATA | 时间 | 24小时制时间格式（支持+年月日），支持填时间段，两个时间点之间用“~”符号连接 | 例如：15:01，或：2019年10月1日 15:01 |
| date.DATA | 日期 | 年月日格式（支持+24小时制时间），支持填时间段，两个时间点之间用“~”符号连接 | 例如：2019年10月1日，或：2019年10月1日 15:01 |
| amount.DATA | 金额 | 1个币种符号+10位以内纯数字，可带小数，结尾可带“元” | 可带小数 |
| phone_number.DATA | 电话 | 17位以内，数字、符号 | 电话号码，例：+86-0766-66888866 |
| car_number.DATA | 车牌 | 8位以内，第一位与最后一位可为汉字，其余为字母或数字 | 车牌号码：粤A8Z888挂 |
| name.DATA | 姓名 | 10个以内纯汉字或20个以内纯字母或符号 | 中文名10个汉字内；纯英文名20个字母内；中文和字母混合按中文名算，10个字内 |
| phrase.DATA | 汉字 | 5个以内汉字 | 5个以内纯汉字，例如：配送中 |
| enum.DATA | 枚举值 | 只能上传枚举值范围内的字段值 | [调用接口获取参考枚举值](https://developers.weixin.qq.com/miniprogram/dev/server/API/mp-message-management/subscribe-message/api_getwxapubnewtemplate) |

符号表示除中文、英文、数字外的常见符号，不能带有换行等控制字符。 时间格式支持HH:MM:SS或者HH:MM。 日期包含年月日，为y年m月d日，y年m月、m月d日格式，或者用‘-’、‘/’、‘.’符号连接，如2018-01-01，2018/01/01，2018.01.01，2018-01，01-01。 每个模板参数都会以类型为前缀，例如第一个数字模板参数为number01.DATA，第二个为number02.DATA

例如，模板的内容为：

```text
姓名: {{name01.DATA}}
金额: {{amount01.DATA}}
行程: {{thing01.DATA}}
日期: {{date01.DATA}}
```

则对应的json为：

```json
{
  "touser": "OPENID",
  "template_id": "TEMPLATE_ID",
  "page": "index",
  "data": {
      "name01": {
          "value": "某某"
      },
      "amount01": {
          "value": "￥100"
      },
      "thing01": {
          "value": "广州至北京"
      } ,
      "date01": {
          "value": "2018-01-01"
      }
  }
}
```

## 5. 代码示例

### 5.1 HTTPS请求示例

请求示例

```json
{
  "touser": "OPENID",
  "template_id": "TEMPLATE_ID",
  "page": "index",
  "miniprogram_state": "developer",
  "lang": "zh_CN",
  "data": {
    "phrase3": {
      "value": "审核通过"
    },
    "name1": {
      "value": "订阅"
    },
    "date2": {
      "value": "2019-12-25 09:42"
    }
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

### 5.2 云函数调用示例

请求示例

```js
const cloud = require('wx-server-sdk')
cloud.init({
  env: cloud.DYNAMIC_CURRENT_ENV,
})
exports.main = async (event, context) => {
  try {
    const result = await cloud.openapi.subscribeMessage.send({
        "touser": 'OPENID',
        "page": 'index',
        "lang": 'zh_CN',
        "data": {
          "number01": {
            "value": '339208499'
          },
          "date01": {
            "value": '2015年01月05日'
          },
          "site01": {
            "value": 'TIT创意园'
          },
          "site02": {
            "value": '广州市新港中路397号'
          }
        },
        "templateId": 'TEMPLATE_ID',
        "miniprogramState": 'developer'
      })
    return result
  } catch (err) {
    return err
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

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

| 小程序 | 小游戏 |
| --- | --- |
| ✔ | ✔ |

- ✔：该账号可调用此接口。
- 其他未明确声明的账号类型，如无特殊说明，均不可调用此接口。
