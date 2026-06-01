# wx.checkEmployeeRelation(Object object)

> 官方文档：[wx.checkEmployeeRelation(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/employee-relation/wx.checkEmployeeRelation.html)
> 所属分类：[开放接口](../开放接口目录.md)
> 导航路径：开放接口 / 用工关系 / wx.checkEmployeeRelation
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 3.10.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#异步-API-返回-Promise) 调用**：不支持
> **小程序插件**：不支持

## 功能描述

检查小程序[用工关系](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/laboruse/intro.html)功能和用户之间的绑定关系

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |   | 否 | 接口调用成功的回调函数 |
| fail | function |   | 否 | 接口调用失败的回调函数 |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

#### object.success 回调函数

##### 参数

###### Object res

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| bindingStatus | string | 绑定状态 |

补充表：
| 合法值 | 说明 |
| --- | --- |
| accept | 已绑定 |
| reject | 已拒绝 |
| '' | 未绑定且未拒绝 |

## 示例代码

```js
wx.checkEmployeeRelation({
  success(res) {
    console.log(res.bindingStatus)
  },
})
```
