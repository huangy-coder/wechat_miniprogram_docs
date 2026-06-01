# Tensor

> 官方文档：[Tensor](https://developers.weixin.qq.com/miniprogram/dev/api/ai/inference/Tensor.html)
> 所属分类：[AI](../AI目录.md)
> 导航路径：AI / AI 推理 / Tensor
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

> 基础库 2.30.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

Tensor

## 属性

### Array.<number> shape

Tensor shape （Tensor 形状，例如 `[1, 3, 224, 224]` 即表示一个4唯Tensor，每个维度的长度分别为1, 3, 224, 224）

### ArrayBuffer data

Tensor 值，一段 ArrayBuffer

### string type

ArrayBuffer 值的类型，合法值有 `uint8`, `int8`, `uint32`, `int32`, `float32`

```js
session.run({
  input1: {
    type: 'float32',
    data: new Float32Array(3 * 224 * 224).buffer,
    shape: [1, 3, 224, 224] // NCHW 顺序
  },
  input2: {
    type: 'uint8',
    data: new Uint8Array(224 * 224).buffer,
    shape: [1, 1, 224, 224]
  },
}).then(res => {
  console.log(res.output0)
  // output0 结构如下：
  // {
  //   type: 'uint8',
  //   data: new Uint8Array(224 * 224).buffer,
  //   shape: [1, 1, 224, 224]
  // }
})
```
