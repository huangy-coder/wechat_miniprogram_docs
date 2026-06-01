# 更新运单轨迹

> 官方文档：[更新运单轨迹](https://developers.weixin.qq.com/miniprogram/dev/server/API/express/express-by-provider/api_updatepath.html)
> 所属分类：[物流助手](../../物流助手目录.md)
> 导航路径：物流助手 / 运力方使用 / 更新运单轨迹
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

[调试诊断](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_tools)

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：updatePath

该接口用于更新运单轨迹。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/cgi-bin/express/delivery/path/update?access_token=ACCESS_TOKEN
```

### 云调用

- 调用方法：logistics.updatePath
- 出入参和 HTTPS 调用相同，调用方式可查看 [云调用](https://developers.weixin.qq.com/doc/oplatform/developers/dev/cloudCall) 说明文档。

### 第三方调用

- 本接口不支持第三方平台调用。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

## 3. 返回参数

### 返回体 Response Payload

## 4. 注意事项

## 其他说明

### action_type 轨迹变化类型的合法值

| 值 | 说明 |
| --- | --- |
| 100001 | 揽件阶段-揽件成功 |
| 100002 | 揽件阶段-揽件失败 |
| 100003 | 揽件阶段-分配业务员 |
| 200001 | 运输阶段-更新运输轨迹 |
| 300002 | 派送阶段-开始派送 |
| 300003 | 派送阶段-签收成功 |
| 300004 | 派送阶段-签收失败 |
| 400001 | 异常阶段-订单取消 |
| 400002 | 异常阶段-订单滞留 |

## 5. 代码示例

### 5.1 HTTPS调用

请求示例

```json
{
  "token": "TOKEN",
  "waybill_id": "12345678901234567890",
  "action_time": 1533052800,
  "action_type": 300002,
  "action_msg": "丽影邓丽君【18666666666】正在派件"
}
```

返回示例

```json
{
  "errcode": 0,
  "errmsg": "ok"
}
```

### 5.2 云函数调用

请求示例

```json
const cloud = require('wx-server-sdk')
cloud.init({
  env: cloud.DYNAMIC_CURRENT_ENV,
})
exports.main = async (event, context) => {
  try {
    const result = await cloud.openapi.logistics.updatePath({
        "token": 'TOKEN',
        "waybillId": '12345678901234567890',
        "actionTime": 1533052800,
        "actionType": 300002,
        "actionMsg": '丽影邓丽君【18666666666】正在派件'
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
  "errCode": 0,
  "errMsg": "openapi.logistics.updatePath:ok"
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
