# 添加地点

> 官方文档：[添加地点](https://developers.weixin.qq.com/miniprogram/dev/server/API/nearby-poi/api_addnearbypoi.html)
> 所属分类：[附近小程序](../附近小程序目录.md)
> 导航路径：附近小程序 / 添加地点
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

[调试诊断](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_tools)

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：addNearbyPoi

该接口用于添加附近小程序的地点。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxa/addnearbypoi?access_token=ACCESS_TOKEN
```

### 云调用

- 调用方法：nearbyPoi.add
- 出入参和 HTTPS 调用相同，调用方式可查看 [云调用](https://developers.weixin.qq.com/doc/oplatform/developers/dev/cloudCall) 说明文档。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：37
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

## 3. 返回参数

### 返回体 Response Payload

### Res.data Object Payload

附近小程序的数据

## 4. 注意事项

- 添加请求暂不支持并发调用，建议使用时间隔1s进行串行调用

## 5. 代码示例

请求示例

```json
{
  "is_comm_nearby": 1,
  "pic_list": "{\"list\":[\"http://mmbiz.qpic.cn/mmbiz_jpg/xdtQKcpj6RuwiafT12xxxxxxxxxibSVYicfUicy2fRqiacjriatWVZPeZsVlI0eztm5Mzjfdy4wcQVicscfapoqlzQ2g/0\"]}",
  "store_name": "xxx黄焖鸡米饭(xxxx店)",
  "hour": "00:00-23:59",
  "credential": "92321324MA24xxxxxxx",
  "address": "江苏省宿迁市泗洪县尚城府邸xxxxxxxx",
  "company_name": "xxxx县阿庆小吃部",
  "service_infos": "{\"service_infos\":[{\"id\":\"1\",\"type\":\"1\",\"name\":\"外卖\",\"appid\":\"wx4e96615821xxxxxx\",\"path\":\"/pages/index/store/store?scene=148897\"}]}",
  "qualification_list": "rNdNSNGaFDIGsyhucEPyANpW9_OIMa9iXSh-CdEXqL8pkqxxxxxx",
  "kf_info": "{\"open_kf\":false}",
  "contract_phone": "18071xxxxxx",
  "map_poi_id": "30323090226254xxxxx"
}
```

返回示例

```json
{
  "errcode": 0,
  "errmsg": "ok",
  "data": {
    "audit_id": 416620525,
    "poi_id": 112333
  }
}
```

## 6. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 7. 适用范围

本接口支持「小程序」账号类型调用。其他账号类型如无特殊说明，均不可调用。
