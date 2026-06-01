# EditorContext

> 官方文档：[EditorContext](https://developers.weixin.qq.com/miniprogram/dev/api/media/editor/EditorContext.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 富文本 / EditorContext
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.7.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> 相关文档: [editor 组件](https://developers.weixin.qq.com/miniprogram/dev/component/editor.html)

EditorContext 实例，可通过 [wx.createSelectorQuery](../../19.WXML/wx.createSelectorQuery.md) 获取。

[EditorContext](EditorContext.md) 通过 `id` 跟一个 [editor](https://developers.weixin.qq.com/miniprogram/dev/component/editor.html) 组件绑定，操作对应的 [editor](https://developers.weixin.qq.com/miniprogram/dev/component/editor.html) 组件。

## 方法

### EditorContext.format(string name, string value)

修改样式

### EditorContext.insertDivider()

插入分割线

### EditorContext.insertImage(Object object)

插入图片。

地址为临时文件时，获取的编辑器html格式内容中 标签增加属性 data-local，delta 格式内容中图片 attributes 属性增加 data-local 字段，该值为传入的临时文件地址。

开发者可选择在提交阶段上传图片到服务器，获取到网络地址后进行替换。替换时对于html内容应替换掉 的 src 值，对于 delta 内容应替换掉 `insert { image: abc }` 值。

### EditorContext.insertText(Object object)

覆盖当前选区，设置一段文本

### EditorContext.setContents(Object object)

初始化编辑器内容，html和delta同时存在时仅delta生效

### EditorContext.getContents()

获取编辑器内容

### EditorContext.clear()

清空编辑器内容

### EditorContext.removeFormat()

清除当前选区的样式

### EditorContext.undo()

撤销

### EditorContext.redo()

恢复

### EditorContext.getHistoryState()

获取历史操作状态

### EditorContext.blur()

编辑器失焦，同时收起键盘。

### EditorContext.scrollIntoView()

使得编辑器光标处滚动到窗口可视区域内。

### EditorContext.getSelectionText()

获取编辑器已选区域内的纯文本内容。当编辑器失焦或未选中一段区间时，返回内容为空。

### EditorContext.insertCustomBlock(Object object)

插入自定义区块

### EditorContext.getSelection()

获取当前选区

### EditorContext.setSelection(Object object)

设置当前选区

### EditorContext.getBounds(Object object)

获取指定选区的位置和大小

### EditorContext.deleteText(Object object)

删除指定选取区的内容
