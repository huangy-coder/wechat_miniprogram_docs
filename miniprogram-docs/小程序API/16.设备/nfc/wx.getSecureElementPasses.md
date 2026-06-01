# wx.getSecureElementPasses(Object args)

> 官方文档：[wx.getSecureElementPasses(Object args)](https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/wx.getSecureElementPasses.html)
> 所属分类：[设备](../设备目录.md)
> 导航路径：设备 / NFC 读写 / wx.getSecureElementPasses
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 3.8.5 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#异步-API-返回-Promise) 调用**：不支持
> **小程序插件**：不支持

## 功能描述

获取设备中的所有卡信息

## 参数

### Object args

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | function |   | 否 | 接口调用成功的回调函数 |
| fail | function |   | 否 | 接口调用失败的回调函数 |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

#### args.success 回调函数

##### 参数

###### Object object

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| result | String | 返回值 |
| errorMsg | String | 错误信息 |
| passes | Array.<Object> | SimplePKPass 的 JSON字符串，这里给出定义，需要进行 JSON.parse 后才可使用 |

补充表：
| 结构属性 | 类型 | 说明 |
| --- | --- | --- |
| primaryAccountIdentifier | string | 支付卡的主账户唯一标识符（由 Apple Pay 生成，用于设备端管理） |
| primaryAccountNumberSuffix | string | 主实体卡号的后缀（如卡号末4位） |
| deviceAccountIdentifier | string | 设备端生成的虚拟卡唯一标识符（用于本地关联安全元件中的卡片） |
| deviceAccountNumberSuffix | string | 设备虚拟卡号的后缀（如虚拟卡号末4位） |
| passActivationState | number | 卡片激活状态，具体值参考 PKSecureElementPassActivationState |
| devicePassIdentifier | string | 设备端卡片的唯一 Pass ID（用于与 Wallet 应用交互） |
| pairedTerminalIdentifier | string | 配对的终端设备标识符（如交通闸机设备 ID） |
| isRemotePass | boolean | 是否为远程同步的卡片（如通过 iCloud 同步到设备的卡片） |

## 示例代码

```javascript
const { result, errorMsg, passes } = await wx.getSecureElementPasses();
```
