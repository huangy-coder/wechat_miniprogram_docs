# 更新商户审核结果

> 官方文档：[更新商户审核结果](https://developers.weixin.qq.com/miniprogram/dev/server/API/express/express-by-provider/api_updatebusiness.html)
> 所属分类：[物流助手](../../物流助手目录.md)
> 导航路径：物流助手 / 运力方使用 / 更新商户审核结果
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

[调试诊断](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_tools)

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：updateBusiness

该接口用于更新商户审核结果。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/cgi-bin/express/delivery/service/business/update?access_token=ACCESS_TOKEN
```

### 云调用

- 调用方法：logistics.updateBusiness
- 出入参和 HTTPS 调用相同，调用方式可查看 [云调用](https://developers.weixin.qq.com/doc/oplatform/developers/dev/cloudCall) 说明文档。

### 第三方调用

- 本接口不支持第三方平台调用。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

## 3. 返回参数

### 返回体 Response Payload

## 4. 注意事项

本接口无特殊注意事项

## 5. 代码示例

### 5.1 HTTPS调用

请求示例

```json
{
  "shop_app_id": "wxABCD",
  "biz_id": "xyz",
  "result_code": 0,
  "result_msg": "审核通过"
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
    const result = await cloud.openapi.logistics.updateBusiness({
        "shopAppId": 'wxABCD',
        "bizId": 'xyz',
        "resultCode": 0,
        "resultMsg": '审核通过'
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
  "errMsg": "openapi.logistics.updateBusiness:ok"
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
