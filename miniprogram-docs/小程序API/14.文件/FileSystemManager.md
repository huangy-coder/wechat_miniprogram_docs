# FileSystemManager

> 官方文档：[FileSystemManager](https://developers.weixin.qq.com/miniprogram/dev/api/file/FileSystemManager.html)
> 所属分类：[文件](文件目录.md)
> 导航路径：文件 / FileSystemManager
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 相关文档: [文件系统](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/file-system.html)

文件管理器，可通过 [wx.getFileSystemManager](wx.getFileSystemManager.md) 获取。

## 方法

### FileSystemManager.access(Object object)

判断文件/目录是否存在

### FileSystemManager.appendFile(Object object)

在文件结尾追加内容

### FileSystemManager.saveFile(Object object)

保存临时文件到本地。此接口会移动临时文件，因此调用成功后，tempFilePath 将不可用。

### FileSystemManager.getSavedFileList(Object object)

获取该小程序下已保存的本地缓存文件列表

### FileSystemManager.removeSavedFile(Object object)

删除该小程序下已保存的本地缓存文件

### FileSystemManager.close(Object object)

关闭文件

### undefined FileSystemManager.closeSync(Object object)

同步关闭文件

### FileSystemManager.copyFile(Object object)

复制文件

### FileSystemManager.fstat(Object object)

获取文件的状态信息

### Stats FileSystemManager.fstatSync(Object object)

同步获取文件的状态信息

### FileSystemManager.ftruncate(Object object)

对文件内容进行截断操作

### undefined FileSystemManager.ftruncateSync(Object object)

对文件内容进行截断操作

### FileSystemManager.getFileInfo(Object object)

获取该小程序下的 本地临时文件 或 本地缓存文件 信息

### FileSystemManager.mkdir(Object object)

创建目录

### FileSystemManager.open(Object object)

打开文件，返回文件描述符

### string FileSystemManager.openSync(Object object)

同步打开文件，返回文件描述符

### FileSystemManager.read(Object object)

读文件

### ReadResult FileSystemManager.readSync(Object object)

读文件

### FileSystemManager.readCompressedFile(Object object)

读取指定压缩类型的本地文件内容

### ArrayBuffer FileSystemManager.readCompressedFileSync(Object object)

同步读取指定压缩类型的本地文件内容

### FileSystemManager.readFile(Object object)

读取本地文件内容。单个文件大小上限为100M。

### FileSystemManager.readZipEntry(Object object)

读取压缩包内的文件

### FileSystemManager.readdir(Object object)

读取目录内文件列表

### FileSystemManager.rename(Object object)

重命名文件。可以把文件从 oldPath 移动到 newPath

### FileSystemManager.rmdir(Object object)

删除目录

### FileSystemManager.stat(Object object)

获取文件 Stats 对象

### FileSystemManager.truncate(Object object)

对文件内容进行截断操作

### undefined FileSystemManager.truncateSync(Object object)

对文件内容进行截断操作 (truncate 的同步版本)

### FileSystemManager.unlink(Object object)

删除文件

### FileSystemManager.unzip(Object object)

解压文件

### FileSystemManager.write(Object object)

写入文件

### WriteResult FileSystemManager.writeSync(Object object)

同步写入文件

### FileSystemManager.writeFile(Object object)

写文件
