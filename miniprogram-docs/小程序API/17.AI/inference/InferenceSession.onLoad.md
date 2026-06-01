# InferenceSession.onLoad(function callback)

> 官方文档：[InferenceSession.onLoad(function callback)](https://developers.weixin.qq.com/miniprogram/dev/api/ai/inference/InferenceSession.onLoad.html)
> 所属分类：[AI](../AI目录.md)
> 导航路径：AI / AI 推理 / InferenceSession / InferenceSession.onLoad
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.30.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持，需要小程序基础库版本不低于 [2.30.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)

## 功能描述

监听模型加载完成事件

## 参数

### function callback

模型加载完成回调函数

## 示例代码

```js
// 创建会话，加载模型
const session = wx.createInferenceSession({
  model: `${wx.env.USER_DATA_PATH}/MNIST.onnx`,
  precisionLevel: 4,
  typicalShape:{input1:[1, 3, 224, 224], input2:[1, 1, 224, 224]},  //除非使用动态轴，一般不用显式指定
  allowNPU: false,
  allowQuantize: false
})

// 监听模型加载完成事件
session.onLoad(() => {
  // 运行推理
  // 其中input1, input2, output0 必须与使用的onnx模型中实际的输入输出名字完全一致，不可随意填写。
  // 模型输入输出信息可以通过Netron 打开onnx模型看到
  session.run({
    input1: {
      type: 'float32',
      data: new Float32Array(3 * 224 * 224).buffer,
      shape: [1, 3, 224, 224] // NCHW 顺序
    },
    // 多个input的添加方法，假设第二个input需要数据类型为uint8
    input2: {
      type: 'uint8',
      data: new Uint8Array(224 * 224).buffer,
      shape: [1, 1, 224, 224]
    },
  }).then(res => {
    console.log(res.output0)
  })
})
```
