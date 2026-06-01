# router.addRouteBuilder(string routeType, function routeBuilder)

> 官方文档：[router.addRouteBuilder(string routeType, function routeBuilder)](https://developers.weixin.qq.com/miniprogram/dev/api/route/router/base/router.addRouteBuilder.html)
> 所属分类：[路由](../../路由目录.md)
> 导航路径：路由 / 自定义路由 / 基础 / router.addRouteBuilder
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **小程序插件**：不支持

> 相关文档: [自定义路由](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/custom-route.html)

## 功能描述

添加自定义路由配置

## 参数

### string routeType

路由类型

### function routeBuilder

[路由动画定义函数](https://developers.weixin.qq.com/miniprogram/dev/api/route/router/base/(CustomRouteBuilder))

## 自定义路由示例

[在开发者工具中预览效果](https://developers.weixin.qq.com/s/y1IbQpmA7wGZ)

```js
// 定义自定义效果，从右侧推入
const slideRouteBuilder = (customRouteContext) => {
  const { primaryAnimation } = customRouteContext
  const handlePrimaryAnimation = () => {
    'worklet'
    const transX = windowWidth * (1 - primaryAnimation.value)
	   return {
		   transform: `translateX(${transX}px)`,
	   }
  }
  return {
    handlePrimaryAnimation
  }
}

wx.router.addRouteBuilder('slide', slideRouteBuilder)

// 使用自定义路由
wx.navigateTo({
  url: 'xxx',
  routeType: 'slide'
})
```
