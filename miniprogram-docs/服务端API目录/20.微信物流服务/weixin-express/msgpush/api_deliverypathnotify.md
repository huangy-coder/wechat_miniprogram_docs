# 推送已绑定物流轨迹信息

> 官方文档：[推送已绑定物流轨迹信息](https://developers.weixin.qq.com/miniprogram/dev/server/API/weixin-express/msgpush/api_deliverypathnotify.html)
> 所属分类：[微信物流服务](../../微信物流服务目录.md)
> 导航路径：微信物流服务 / 消息推送 / 推送已绑定物流轨迹信息
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：deliveryPathNotify

运力方可以调用此接口来推送物流轨迹消息

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/cgi-bin/express/delivery/pathnotify?access_token=ACCESS_TOKEN
```

### 云调用

- 本接口不支持云调用。

### 第三方调用

- 本接口不支持第三方平台调用。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

### Body.sender Object Payload

寄件人

### Body.receiver Object Payload

收件人

### Body.path Object Payload

当前需要推送消息的轨迹

## 3. 返回参数

### 返回体 Response Payload

## 4. 枚举信息

### Body.path.action_type Enum

轨迹变化类型，与普通单保持一致，参见下方其他说明action_type定义

## 5. 注意事项

本接口无特殊注意事项

## 6. 代码示例

请求示例

```json
{
"path": {
  "action_time": 1597396101,
  "action_type": 200001,
  "action_msg": "快件到达 【泉州磁灶集散中心】",
  "pickup_courier_name":"",
  "pickup_courier_phone":"",
  "delivery_courier_name":"",
  "delivery_courier_phone":""
 },
 "receiver": {
  "area": "晋江市",
  "address": "庄宅北区158-6",
  "province": "福建省",
  "city": "泉州市",
  "phone": "13800138000",
  "name": "李四"
 },
 "sender": {
  "area": "柯桥区",
  "address": "纺都路137号",
  "province": "浙江省",
  "city": "绍兴市",
  "phone": "13800138001",
  "name": "张三"
 },
 "waybill_id": "1234567890"
 }
```

返回示例

```json
{
    "errcode": 0,
    "errmsg": "ok",
    "exist": 0
}
```

## 7. 错误码

以下是本接口的错误码列表，其他错误码可参考 [通用错误码](https://developers.weixin.qq.com/doc/oplatform/developers/errCode/)；调用接口遇到报错，可使用官方提供的 [API 诊断工具](https://developers.weixin.qq.com/console/devtools/debug?utm_source=api_errcode) 辅助定位和分析问题。

## 8. 适用范围

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
