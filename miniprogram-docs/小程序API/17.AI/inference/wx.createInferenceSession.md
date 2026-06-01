# InferenceSession wx.createInferenceSession(Object object)

> 官方文档：[InferenceSession wx.createInferenceSession(Object object)](https://developers.weixin.qq.com/miniprogram/dev/api/ai/inference/wx.createInferenceSession.html)
> 所属分类：[AI](../AI目录.md)
> 导航路径：AI / AI 推理 / wx.createInferenceSession
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.30.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

> **小程序插件**：支持，需要小程序基础库版本不低于 [2.30.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)

## 功能描述

创建 AI 推理 Session。使用前可参考[AI指南文档](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/inference/tutorial.html)

## 参数

### Object object

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| model | string |   | 是 | 模型文件路径，目前只执行后缀为.onnx格式(支持代码包路径，和本地文件系统路径） |
| precisionLevel | number | 4 | 否 | 推理精度，有效值为 0 - 4。一般来说，使用的precisionLevel等级越低，推理速度越快，但可能会损失精度。推荐开发者在开发时，在效果满足需求时优先使用更低精度以提高推理速度，节约能耗。 |
| allowQuantize | boolean | false | 否 | 是否生成量化模型推理 |
| allowNPU | boolean | false | 否 | 是否使用NPU推理，仅对IOS有效 |
| typicalShape | Object |   | 否 | 输入典型分辨率 |

补充表：
| 合法值 | 说明 |
| --- | --- |
| 0 | 使用fp16 存储浮点，fp16计算，Winograd 算法也采取fp16 计算，开启近似math计算 |
| 1 | 使用fp16 存储浮点，fp16计算，禁用 Winograd 算法，开启近似math计算 |
| 2 | 使用fp16 存储浮点，fp32计算，开启 Winograd，开启近似math计算 |
| 3 | 使用fp32 存储浮点，fp32计算，开启 Winograd，开启近似math计算 |
| 4 | 使用fp32 存储浮点，fp32计算，开启 Winograd，关闭近似math计算 |

## 返回值

### InferenceSession

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

// 监听error事件
session.onError(err => {
  console.error(err)
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

// 销毁Session
// session完成创建后可以多次调用run进行推理，直到调用`session.destroy()`释放相关内存。

// 销毁会话
session.destroy()
```
