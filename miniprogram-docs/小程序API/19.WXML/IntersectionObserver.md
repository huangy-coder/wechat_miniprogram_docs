# IntersectionObserver

> 官方文档：[IntersectionObserver](https://developers.weixin.qq.com/miniprogram/dev/api/wxml/IntersectionObserver.html)
> 所属分类：[WXML](WXML目录.md)
> 导航路径：WXML / IntersectionObserver
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 相关文档: [获取界面上的节点信息](https://developers.weixin.qq.com/miniprogram/dev/framework/view/selector.html)

IntersectionObserver 对象，用于推断某些节点是否可以被用户看见、有多大比例可以被用户看见。

## 方法

### IntersectionObserver IntersectionObserver.relativeTo(string selector, Object margins)

使用选择器指定一个节点，作为参照区域之一。

### IntersectionObserver IntersectionObserver.relativeToViewport(Object margins)

指定页面显示区域作为参照区域之一

### IntersectionObserver.observe(string targetSelector, IntersectionObserver.observeCallback callback)

指定目标节点并开始监听相交状态变化情况

### IntersectionObserver.disconnect()

停止监听。回调函数将不再触发
