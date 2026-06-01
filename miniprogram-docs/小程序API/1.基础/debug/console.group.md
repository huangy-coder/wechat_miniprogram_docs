# console.group(string label)

> 官方文档：[console.group(string label)](https://developers.weixin.qq.com/miniprogram/dev/api/base/debug/console.group.html)
> 所属分类：[基础](../基础目录.md)
> 导航路径：基础 / 调试 / console / console.group
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> **小程序插件**：不支持

## 功能描述

在调试面板中创建一个新的分组。随后输出的内容都会被添加一个缩进，表示该内容属于当前分组。调用 [console.groupEnd](console.groupEnd.md)之后分组结束。

## 参数

### string label

分组标记，可选。

## 注意

仅在工具中有效，在 vConsole 中为空函数实现。
