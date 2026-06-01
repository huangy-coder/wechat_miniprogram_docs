# B2b门店助手服务端 API 目录

> 官方入口：[B2b门店助手](https://developers.weixin.qq.com/miniprogram/dev/server/API/B2b)
> 整理日期：2026-06-01
> 所属范围：微信小程序「开发 / 服务端」栏目。

## 功能范围

B2B 门店助手业务接口。

## 本地条目

- 本分类共整理 38 个独立服务端页面。
- 下方目录保持官方左侧导航层级，并链接到本地 Markdown 正文。

## 目录

- [B2b门店助手](B2b.md)
  - [门店认证授权](B2b/store_assistant.md)
    - [开通流程](B2b/store_assistant/api_retailbusinessapply.md)
    - [预录入门店信息](B2b/store_assistant/api_batchcreateretail.md)
    - [门店信息查询](B2b/store_assistant/api_getretailinfo.md)
    - [全量授权门店查询](B2b/store_assistant/api_getretailopenidlist.md)
  - [消息触达](B2b/notify.md)
    - [模板消息列表及下发](B2b/notify/api_retailnotifybusiness.md)
    - [消息效果数据](B2b/notify/api_getretailmessagelist.md)
  - [B2b支付](B2b/bill.md)
    - [商户号进件](B2b/bill/api_retailregistermch.md)
    - [上传商户图片](B2b/bill/api_retailuploadmchfile.md)
    - [查询商户号开通状态](B2b/bill/api_retailgetmchorder.md)
    - [申请开通银行转账](B2b/bill/api_registeronlywqf.md)
    - [跳转银行转账页面](B2b/bill/api_createwqflink.md)
    - [获取小程序下所有商户的信息](B2b/bill/api_getmchinfo.md)
    - [报名微信支付技术服务费优惠活动](B2b/bill/api_setmchprofitrate.md)
    - [报名银行转账技术服务费优惠活动](B2b/bill/api_updatewqfchargefee.md)
    - [查询银行转账的技术服务费率](B2b/bill/api_getwqfchargefee.md)
    - [查询订单](B2b/bill/api_getorder.md)
    - [关闭订单](B2b/bill/api_closeb2border.md)
    - [退款](B2b/bill/api_refundorder.md)
    - [查询退款](B2b/bill/api_getrefund.md)
    - [获取密钥AppKey](B2b/bill/api_getappkey.md)
    - [接口下载交易账单与资金账单](B2b/bill/api_downloadbill.md)
    - [查询账户余额](B2b/bill/api_getmchbalance.md)
    - [发起手动提现](B2b/bill/api_manualwithdraw.md)
    - [查询提现状态](B2b/bill/api_querywithdraw.md)
    - [微信支付自动提现接口](B2b/bill/api_setautowithdraw.md)
    - [添加分账方](B2b/bill/api_addprofitsharingaccount.md)
    - [删除分账方](B2b/bill/api_delprofitsharingaccount.md)
    - [查询分账方](B2b/bill/api_queryprofitsharingaccount.md)
    - [请求分账](B2b/bill/api_createprofitsharingorder.md)
    - [查询分账结果](B2b/bill/api_queryprofitsharingorder.md)
    - [查询分账剩余金额](B2b/bill/api_queryprofitsharingremainamt.md)
    - [完成分账](B2b/bill/api_finishprofitsharingorder.md)
    - [请求分账回退](B2b/bill/api_refundprofitsharing.md)
    - [查询分账回退结果](B2b/bill/api_queryrefundprofitsharingorder.md)
