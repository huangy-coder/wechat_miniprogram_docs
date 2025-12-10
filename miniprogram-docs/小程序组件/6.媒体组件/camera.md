# camera

> 基础库 1.6.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **微信 Mac 版**：支持
>
> **微信 鸿蒙 OS 版**：支持

> 相关文档: [wx.createCameraContext](https://developers.weixin.qq.com/miniprogram/dev/api/media/camera/wx.createCameraContext.html)

渲染框架支持情况：Skyline （使用最新 [Nightly](https://developers.weixin.qq.com/miniprogram/dev/devtools/nightly.html) 工具调试）、WebView

## 功能描述

系统相机。扫码二维码功能，需升级微信客户端至6.7.3。需要[用户授权](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/authorize.html)`scope.camera`。 [2.10.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)起 initdone 事件返回 maxZoom，最大变焦范围，相关接口 [CameraContext.setZoom](https://developers.weixin.qq.com/miniprogram/dev/api/media/camera/CameraContext.setZoom.html)。

## 通用属性

|      | 属性                                                         | 类型        | 默认值 | 必填 | 说明                                              | 最低版本                                                     |
| ---- | ------------------------------------------------------------ | ----------- | ------ | ---- | ------------------------------------------------- | ------------------------------------------------------------ |
|      | mode                                                         | string      | normal | 否   | 应用模式，只在初始化时有效，不能动态变更          | [2.1.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
|      | 合法值说明normal相机模式scanCode扫码模式                     |             |        |      |                                                   |                                                              |
|      | resolution                                                   | string      | medium | 否   | 分辨率，不支持动态修改                            | [2.10.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
|      | 合法值说明low低medium中high高                                |             |        |      |                                                   |                                                              |
|      | device-position                                              | string      | back   | 否   | 摄像头朝向                                        | [1.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
|      | 合法值说明front前置back后置                                  |             |        |      |                                                   |                                                              |
|      | flash                                                        | string      | auto   | 否   | 闪光灯，值为auto, on, off                         | [1.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
|      | 合法值说明最低版本auto自动on打开off关闭torch常亮[2.8.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |             |        |      |                                                   |                                                              |
|      | frame-size                                                   | string      | medium | 否   | 指定期望的相机帧数据尺寸                          | [2.7.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
|      | 合法值说明small小尺寸帧数据medium中尺寸帧数据large大尺寸帧数据 |             |        |      |                                                   |                                                              |
|      | bindstop                                                     | eventhandle |        | 否   | 摄像头在非正常终止时触发，如退出后台等情况        | [1.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
|      | binderror                                                    | eventhandle |        | 否   | 用户不允许使用摄像头时触发                        | [1.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
|      | bindinitdone                                                 | eventhandle |        | 否   | 相机初始化完成时触发，`e.detail = {maxZoom}`      | [2.7.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |
|      | bindscancode                                                 | eventhandle |        | 否   | 在扫码识别成功时触发，仅在 mode="scanCode" 时生效 | [2.1.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) |

## Bug & Tip

1. `tip`: 同一页面只能插入一个 `camera` 组件
2. `tip`:请注意[原生组件使用限制](https://developers.weixin.qq.com/miniprogram/dev/component/native-component.html#原生组件的使用限制)
3. `tip`:onCameraFrame 接口根据 frame-size 返回不同尺寸的原始帧数据，与 Camera 组件展示的图像不同，其实际像素值由系统决定

## 示例代码

[在开发者工具中预览效果](https://developers.weixin.qq.com/s/VBZ3Jim26zYu)

```xml
<camera device-position="back" flash="off" binderror="error" style="width: 100%; height: 300px;"></camera>
<button type="primary" bindtap="takePhoto">拍照</button>
<view>预览</view>
<image mode="widthFix" src="{{src}}"></image>

```

```js

Page({
  takePhoto() {
    const ctx = wx.createCameraContext()
    ctx.takePhoto({
      quality: 'high',
      success: (res) => {
        this.setData({
          src: res.tempImagePath
        })
      }
    })
  },
  error(e) {
    console.log(e.detail)
  }
})
```

