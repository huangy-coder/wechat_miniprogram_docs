# 广告数据源报表查询（ad.getUserActionSetReports）

> 官方文档：[广告数据源报表查询（ad.getUserActionSetReports）](https://developers.weixin.qq.com/miniprogram/dev/server/ad/Advertising_data_source_report_query.html)
> 所属分类：[广告](广告目录.md)
> 导航路径：广告 / 广告数据源报表查询
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide.html)

广告数据源报表查询

微信广告文档：[https://ad.weixin.qq.com/guide/457](https://ad.weixin.qq.com/guide/457)

```bash
https://api.weixin.qq.com/marketing/user_action_set_reports/get
```

### 云调用使用说明

外链文档中可能只有 HTTP 形式的定义，对云调用方式，调用时参数与 HTTP 需求的参数一致，但是无需传入 `access_token`，同时所有的参数无论 get/post 都只需作为接口参数 JS 对象中的一个字段传入即可。

而对于 FormData 的请求，如果一个参数的类型是 Buffer，则其字段应传入有如下字段的对象：

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| contentType | string |   | 是 | 数据类型，传入 MIME Type |
| value | Buffer |   | 是 | 文件 Buffer |

**示例**

假设外链文档要求是 POST 方法，要求传入如下参数

| 属性 | 类型 | 位置 | 说明 |
| --- | --- | --- | --- |
| xxx | string | URL 参数 | ... |
| yyy | number | JSON body | ... |

则调用示例如下：

```js
cloud.openapi.ad.getUserActionSetReports({
  xxx: '字符串',
  yyy: 100,
})
```

假设外链文档要求是 POST FormData，要求传入如下参数

| 属性 | 类型 | 位置 | 说明 |
| --- | --- | --- | --- |
| xxx | string | URL 参数 | ... |
| media | buffer | FormData | 图片 buffer |

则调用示例如下：

```js
cloud.openapi.ad.getUserActionSetReports({
  xxx: '字符串',
  media: {
    contentType: 'image/png',
    value: Buffer
  },
})
```
