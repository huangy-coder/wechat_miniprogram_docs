# horizontal-drag-gesture-handler

> 相关文档: [手势系统](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/gesture.html)

渲染框架支持情况：Skyline （使用最新 [Nightly](https://developers.weixin.qq.com/miniprogram/dev/devtools/nightly.html) 工具调试）

## 功能描述

横向滑动时触发手势

## 通用属性

|      | 类型           | 默认值 | 属性                                                         | 必填 | 说明                       |
| ---- | -------------- | ------ | ------------------------------------------------------------ | ---- | -------------------------- |
|      | string         |        | tag                                                          | 否   | 声明手势协商时的组件标识   |
|      | eventhandler   |        | worklet:ongesture                                            | 否   | 手势识别成功的回调         |
|      |                |        | eventhandler 回调参数说明state手势状态absoluteX相对于全局的 X 坐标absoluteY相对于全局的 Y 坐标deltaX相对上一次，X 轴方向移动的坐标deltaY相对上一次，Y 轴方向移动的坐标velocityX手指离开屏幕时的横向速度（pixel per second)velocityY手指离开屏幕时的纵向速度（pixel per second) |      |                            |
|      | callback       |        | worklet:should-response-on-move                              | 否   | 手指移动过程中手势是否响应 |
|      | callback       |        | worklet:should-accept-gesture                                | 否   | 手势是否应该被识别         |
|      | Array.<string> |        | simultaneous-handlers                                        | 否   | 声明可同时触发的手势节点   |
|      | string         |        | native-view                                                  | 否   | 代理的原生节点类型         |