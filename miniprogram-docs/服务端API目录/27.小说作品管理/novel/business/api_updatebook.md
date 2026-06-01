# 编辑作品

> 官方文档：[编辑作品](https://developers.weixin.qq.com/miniprogram/dev/server/API/novel/business/api_updatebook.html)
> 所属分类：[小说作品管理](../../小说作品管理目录.md)
> 导航路径：小说作品管理 / 作品管理 / 编辑作品
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

> 接口应在服务器端调用，不可在前端（小程序、网页、APP等）直接调用，具体可参考[接口调用指南](https://developers.weixin.qq.com/doc/oplatform/developers/dev/guide)。

接口英文名：updateBook

该接口用于编辑作品编辑版的基础信息、章节顺序、分卷信息，不直接影响发布版，需要提审通过后才会更新发布版。

## 1. 调用方式

### HTTPS 调用

```bash
POST https://api.weixin.qq.com/wxa/book/updatebook?access_token=ACCESS_TOKEN
```

### 云调用

- 本接口不支持云调用。

### 第三方调用

- 本接口支持第三方平台代商家调用。
- 该接口所属的权限集 id 为：169
- 服务商获得其中之一权限集授权后，可通过使用 [authorizer_access_token](https://developers.weixin.qq.com/doc/oplatform/developers/dev/AuthorizerAccessToken) 代商家进行调用，具体可查看 [第三方调用](https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/api/Before_Develop/call_interface.html) 说明文档。

## 2. 请求参数

### 查询参数 Query String Parameters

### 请求体 Request Payload

### Body.volume_list(Array) Object Payload

分卷信息

## 3. 返回参数

### 返回体 Response Payload

## 4. 注意事项

1. 除了 book_id 必填以外，其余字段是需要修改才设置。
2. 若要修改作品类型，必须同时传入三级类型id。
3. 审核中的作品不支持修改信息。
4. 作品若需要分卷，则所有章节都需要被划入某个分卷，不能有某个章节未被划入分卷。
5. 创建/删除章节后，需要主动修改作品分卷信息，否则无法提审。
6. 分卷管理涉及两个字段 need_volume 和 volume_list。need_volume 不设置时为不修改分卷；need_volume 设置为 true 时表示需要用 volume_list 来修改作品分卷；need_volume 设置为 false 时表示作品不需要分卷，会清除当前作品的分卷信息。
7. 分卷列表里需要按照分卷顺序传入参数，即第一卷的信息需要在第二卷之前，否则会报错。
8. 分卷信息里的章节范围为左闭右闭，即包含 start_index 和 end_index 对应章节。第一卷的 start_index 应等于 0，后续每一卷的 start_index 应等于前一卷的 end_index + 1，最后一卷的 end_index 应等于作品章节总数 - 1。不同分卷的章节范围不能重叠，且合并所有分卷信息的区间应等于 [0, 章节总数 - 1]。
9. 章节排序方式切换规则：从“追加”调整为“seq 递增”不保留当前章节顺序，自动按照章节 seq 重新排序；从“seq 递增”调整为“追加”会保留当前章节顺序，不清除章节 seq 信息。
10. 题材关键词、精彩片段用于平台推荐场景。精彩片段需为本书内容

## 5. 代码示例

请求示例

```json
{
    "book_id": "A1b2C3d4",
    "complete_status": 2,
    "need_volume": true,
    "volume_list": [
        {
            "volume_title": "第一卷",
            "start_index": 0,
            "end_index": 2
        },
        {
            "volume_title": "第二卷",
            "start_index": 2,
            "end_index": 5
        }
    ]
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

本接口暂未明确可调用账号类型，或在业务中根据调用传参自行确定是否可调用，请以实际调用情况为准。
