# wx.preloadAssets(Object object)

> 官方文档：[wx.preloadAssets(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/base/performance/wx.preloadAssets.html)
> 所属分类：[基础](../基础目录.md)
> 导航路径：基础 / 性能 / wx.preloadAssets
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.22.1 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **以 [Promise 风格](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html#异步-API-返回-Promise) 调用**：不支持
> **小程序插件**：不支持
> **微信 Windows 版**：支持
> **微信 Mac 版**：支持
> **微信 鸿蒙 OS 版**：支持

## 功能描述

为视图层预加载媒体资源文件, 目前支持：font，image

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| data | Array.<Object> |   | 是 |   |
| success | function |   | 否 | 接口调用成功的回调函数 |
| fail | function |   | 否 | 接口调用失败的回调函数 |
| complete | function |   | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

补充表：
| 结构属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| type | string |   | 是 |   |
| src | string |   | 是 |   |

补充表：
| 合法值 | 说明 |
| --- | --- |
| 'font' | 字体 |
| 'image' | 图片 |

## 示例代码

```js
wx.preloadAssets({
  data: [
    {
      type: 'image',
      src: imgUrl,
    },
  ],
  success(resp) {
    console.log('preloadAssets success', resp)
  },
  fail(err) {
    console.log('preloadAssets fail', err)
  },
})
```

- 开发过程中，可在开发者工具network面板查看预加载情况。
