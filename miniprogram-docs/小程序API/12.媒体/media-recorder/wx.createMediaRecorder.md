# MediaRecorder wx.createMediaRecorder(Object canvas, Object options)

> 官方文档：[MediaRecorder wx.createMediaRecorder(Object canvas, Object options)](https://developers.weixin.qq.com/miniprogram/dev/api/media/media-recorder/wx.createMediaRecorder.html)
> 所属分类：[媒体](../媒体目录.md)
> 导航路径：媒体 / 画面录制器 / wx.createMediaRecorder
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.11.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持，需要小程序基础库版本不低于 [2.11.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)

## 功能描述

创建 WebGL 画面录制器，可逐帧录制在 WebGL 上渲染的画面并导出视频文件

## 参数

### Object canvas

WebGL 对象，通过 [SelectorQuery](../../19.WXML/SelectorQuery.md) 获取到的 node 对象或通过 [wx.createOffscreenCanvas](../../11.画布/wx.createOffscreenCanvas.md) 创建的离屏 WebGL Canvas 对象

### Object options

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| duration | number | 600 | 否 | 指定录制的时长（s)，到达自动停止。最大 7200，最小 5 |
| videoBitsPerSecond | number | 1000 | 否 | 视频比特率（kbps），最小值 600，最大值 3000 |
| gop | number | 12 | 否 | 视频关键帧间隔 |
| fps | number | 24 | 否 | 视频 fps |
| width | number | canvas.width | 否 | 画布录制宽度 |
| height | number | canvas.height | 否 | 画布录制高度 |

## 返回值

### MediaRecorder

## 示例代码

```javascript
// 准备 canvas 对象，可以是 wxml 声明的 node 对象
const canvas = await new Promise(resolve => {
  wx.createSelectQuery().select('#canvas').node(res => resolve(res.node)).exec()
})
// 也可以是 wx.createOffscreenCanvas 创建的离屏 canvas
const canvas = wx.createOffscreenCanvas()
canvas.width = 300
canvas.height = 150

// 准备一个 canvas 绘制函数，这里使用 three.js
const THREE = require('threejs-miniprogram').createScopedThreejs(canvas)
const camera = new THREE.PerspectiveCamera(70, canvas.width / canvas.height, 1, 1000)
const scene = new THREE.Scene()
const texture = await new Promise(resolve => new THREE.TextureLoader().load('./test.png', resolve)) // 准备一个图片加载为贴图
const geometry = new THREE.BoxBufferGeometry(200, 200, 200)
const material = new THREE.MeshBasicMaterial({ map: texture })
const mesh = new THREE.Mesh(geometry, material)
camera.position.z = 400;
scene.add(mesh)
const renderer = new THREE.WebGLRenderer({ antialias: false })
renderer.setPixelRatio(1)
renderer.setSize(canvas.width, canvas.height)

// canvas 绘制函数
const render = () => {
  mesh.rotation.x += 0.005
  mesh.rotation.y += 0.1
  renderer.render(scene, camera)
}

// 创建 mediaRecorder
const fps = 30
const recorder = wx.createMediaRecorder(canvas, {
  fps,
})

// 启动 mediaRecorder
await recorder.start()

// 录制 5s 的视频
let frames = fps * 5
// 逐帧绘制
while (frames--) {
  await recorder.requestFrame()
  render()
}

// 绘制完成，生成视频
const {tempFilePath} = await recorder.stop()
// 销毁 mediaRecorder
recorder.destroy()
```

## 示例代码

[在开发者工具中预览效果](https://developers.weixin.qq.com/s/MCz3kPmC7zpa)

## 低版本异步接口兼容

对基础库 2.16.1 版本前的 mediaRecorder，所有的接口都没有返回 Promise 对象，若需要兼容低版本，则可采用如下方式的写法：

```javascript
// 启动 mediaRecorder
await new Promise(resolve => {
  recorder.on('start', resolve)
  recorder.start()
})

// 逐帧绘制
while (frames--) {
  await new Promise(resolve => recorder.requestFrame(resolve))
  render()
}

// 绘制完成，生成视频
const {tempFilePath} = await new Promise(resolve => {
  recorder.on('stop', resolve)
  recorder.stop()
})
```
