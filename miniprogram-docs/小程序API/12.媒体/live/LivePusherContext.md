# LivePusherContext

> 官方文档：[LivePusherContext](https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePusherContext.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 实时音视频 / LivePusherContext
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 相关文档: [live-pusher 组件](https://developers.weixin.qq.com/miniprogram/dev/component/live-pusher.html)

LivePusherContext 实例，可通过 [wx.createLivePusherContext](wx.createLivePusherContext.md) 获取。

[LivePusherContext](LivePusherContext.md) 与页面内唯一的 [live-pusher](https://developers.weixin.qq.com/miniprogram/dev/component/live-pusher.html) 组件绑定，操作对应的 [live-pusher](https://developers.weixin.qq.com/miniprogram/dev/component/live-pusher.html) 组件。

## 方法

### LivePusherContext.start()

开始推流，同时开启摄像头预览

### LivePusherContext.stop()

停止推流，同时停止摄像头预览

### LivePusherContext.pause()

暂停推流

### LivePusherContext.resume()

恢复推流

### LivePusherContext.switchCamera()

切换前后摄像头

### LivePusherContext.snapshot(Object object)

快照

### LivePusherContext.toggleTorch()

切换手电筒

### LivePusherContext.playBGM(Object object)

播放背景音

### LivePusherContext.stopBGM()

停止背景音

### LivePusherContext.pauseBGM()

暂停背景音

### LivePusherContext.resumeBGM()

恢复背景音

### LivePusherContext.setBGMVolume(Object object)

设置背景音音量

### LivePusherContext.setMICVolume(Object object)

设置麦克风音量

### LivePusherContext.startPreview()

开启摄像头预览

### LivePusherContext.stopPreview()

关闭摄像头预览

### LivePusherContext.sendMessage(Object object)

发送SEI消息

### LivePusherContext.exitPictureInPicture()

退出小窗，该方法可在任意页面调用

### LivePusherContext.setZoom(Object object)

设置缩放级别

### LivePusherContext.getMaxZoom()

获取最大缩放级别

### LivePusherContext.applyFilter(Object object)

添加滤镜效果

### LivePusherContext.clearFilters()

清除所有滤镜效果

### LivePusherContext.applySticker(Object object)

添加贴纸特效

### LivePusherContext.clearStickers()

清除所有贴纸特效

### LivePusherContext.applyLipStickMakeup(Object object)

添加口红美妆特效

### LivePusherContext.applyEyeShadowMakeup(Object object)

添加眼影美妆特效

### LivePusherContext.applyBlusherStickMakeup(Object object)

添加腮红美妆特效

### LivePusherContext.applyFaceContourMakeup(Object object)

添加修容美妆特效

### LivePusherContext.applyEyeBrowMakeup(Object object)

添加眉毛美妆特效

### LivePusherContext.clearMakeups()

清除所有美妆特效

### LivePusherContext.onCustomRendererEvent(string event, LivePusherContext.customRendererFrameEventCallback|LivePusherContext.customRendererUpdateEventCallback callback)

开启自定义渲染时，开发者通过此方法订阅相关事件，客户端 8.0.31 版本开始支持。

### LivePusherContext.createOffscreenCanvas(object options)

创建一个能够承接 LivePusher 采集纹理的离屏 Canvas，客户端 8.0.31 版本开始支持。

## 示例代码

[在开发者工具中预览效果](https://developers.weixin.qq.com/s/KvWD9mmA62Yk)
