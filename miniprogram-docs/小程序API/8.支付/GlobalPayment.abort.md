# Promise GlobalPayment.abort()

> 官方文档：[Promise GlobalPayment.abort()](https://developers.weixin.qq.com/miniprogram/dev/api/payment/GlobalPayment.abort.html)
> 所属分类：[支付](支付目录.md)
> 导航路径：支付 / GlobalPayment / GlobalPayment.abort
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 3.7.3 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：不支持

## 功能描述

用户选择TPG的支付方式，界面会进入加载的Toast，等待开发者前往TPG完成预下单后携带预支付信息和交易单号调用 requestGlobalPayment，若开发者在
TPG预下单未成功或出现异常情况，可调用该接口主动终止TPG支付流程，界面加载的Toast将会隐藏，提示用户下单失败。

## 返回值

### Promise

object { errno: number, errMsg: string, requestId: string // 每个payment对象唯一 }
