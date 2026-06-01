# EntryList

> 官方文档：[EntryList](https://developers.weixin.qq.com/miniprogram/dev/api/base/performance/EntryList.html)
> 所属分类：[基础](../基础目录.md)
> 导航路径：基础 / 性能 / EntryList
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.11.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

EntryList 对象

## 方法

### Array.<PerformanceEntry> EntryList.getEntries()

该方法返回当前列表中的所有性能数据

### Array.<PerformanceEntry> EntryList.getEntriesByType(string entryType)

获取当前列表中所有类型为 [entryType] 的性能数据

### Array.<PerformanceEntry> EntryList.getEntriesByName(string name, string entryType)

获取当前列表中所有名称为 [name] 且类型为 [entryType] 的性能数据
