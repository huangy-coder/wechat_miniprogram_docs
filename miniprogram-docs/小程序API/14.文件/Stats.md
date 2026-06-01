# Stats

> 官方文档：[Stats](https://developers.weixin.qq.com/miniprogram/dev/api/file/Stats.html)
> 所属分类：[文件](文件目录.md)
> 导航路径：文件 / Stats
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 相关文档: [文件系统](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/file-system.html)

描述文件状态的对象

## 属性

### number mode

文件的类型和存取的权限，对应 POSIX stat.st_mode

### number size

文件大小，单位：B，对应 POSIX stat.st_size

### number lastAccessedTime

文件最近一次被存取或被执行的时间，UNIX 时间戳，对应 POSIX stat.st_atime

### number lastModifiedTime

文件最后一次被修改的时间，UNIX 时间戳，对应 POSIX stat.st_mtime

## 方法

### boolean Stats.isDirectory()

判断当前文件是否一个目录

### boolean Stats.isFile()

判断当前文件是否一个普通文件
