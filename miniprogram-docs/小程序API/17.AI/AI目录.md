# AI API 目录

> 官方入口：[AI](https://developers.weixin.qq.com/miniprogram/dev/api/ai/inference/wx.getInferenceEnvInfo.html)
> 整理日期：2026-05-29
> 所属范围：微信小程序「开发 / API」栏目。

## 功能范围

推理环境、模型管理、NLP、OCR、翻译、语音识别、图像分割等 AI 能力。

## 本地条目

- 本分类共整理 58 个独立 API 页面。
- 下方目录保持官方左侧导航层级，并链接到本地 API 文档。

## 目录

- [AI 推理](inference/wx.getInferenceEnvInfo.md)
  - [wx.getInferenceEnvInfo](inference/wx.getInferenceEnvInfo.md)
  - [wx.createInferenceSession](inference/wx.createInferenceSession.md)
  - [InferenceSession](inference/InferenceSession.md)
    - [InferenceSession.destroy](inference/InferenceSession.destroy.md)
    - [InferenceSession.offError](inference/InferenceSession.offError.md)
    - [InferenceSession.offLoad](inference/InferenceSession.offLoad.md)
    - [InferenceSession.onError](inference/InferenceSession.onError.md)
    - [InferenceSession.onLoad](inference/InferenceSession.onLoad.md)
    - [InferenceSession.run](inference/InferenceSession.run.md)
  - [Tensor](inference/Tensor.md)
  - [Tensors](inference/Tensors.md)
- [视觉算法](visionkit/wx.isVKSupport.md)
  - [wx.isVKSupport](visionkit/wx.isVKSupport.md)
  - [wx.createVKSession](visionkit/wx.createVKSession.md)
  - [VKBodyAnchor](visionkit/VKBodyAnchor.md)
  - [VKCamera](visionkit/VKCamera.md)
    - [VKCamera.getProjectionMatrix](visionkit/VKCamera.getProjectionMatrix.md)
  - [VKDepthAnchor](visionkit/VKDepthAnchor.md)
  - [VKFaceAnchor](visionkit/VKFaceAnchor.md)
  - [VKFrame](visionkit/VKFrame.md)
    - [VKFrame.getCameraBuffer](visionkit/VKFrame.getCameraBuffer.md)
    - [VKFrame.getCameraJpgBuffer](visionkit/VKFrame.getCameraJpgBuffer.md)
    - [VKFrame.getCameraTexture](visionkit/VKFrame.getCameraTexture.md)
    - [VKFrame.getDepthBuffer](visionkit/VKFrame.getDepthBuffer.md)
    - [VKFrame.getDisplayTransform](visionkit/VKFrame.getDisplayTransform.md)
    - [VKFrame.getLegSegmentBuffer](visionkit/VKFrame.getLegSegmentBuffer.md)
  - [VKHandAnchor](visionkit/VKHandAnchor.md)
  - [VKMarkerAnchor](visionkit/VKMarkerAnchor.md)
  - [VKOCRAnchor](visionkit/VKOCRAnchor.md)
  - [VKOSDAnchor](visionkit/VKOSDAnchor.md)
  - [VKPlaneAnchor](visionkit/VKPlaneAnchor.md)
  - [VKSession](visionkit/VKSession.md)
    - [VKSession.addMarker](visionkit/VKSession.addMarker.md)
    - [VKSession.addOSDMarker](visionkit/VKSession.addOSDMarker.md)
    - [VKSession.cancelAnimationFrame](visionkit/VKSession.cancelAnimationFrame.md)
    - [VKSession.destroy](visionkit/VKSession.destroy.md)
    - [VKSession.detectBody](visionkit/VKSession.detectBody.md)
    - [VKSession.detectDepth](visionkit/VKSession.detectDepth.md)
    - [VKSession.detectFace](visionkit/VKSession.detectFace.md)
    - [VKSession.detectHand](visionkit/VKSession.detectHand.md)
    - [VKSession.getAllMarker](visionkit/VKSession.getAllMarker.md)
    - [VKSession.getAllOSDMarker](visionkit/VKSession.getAllOSDMarker.md)
    - [VKSession.getVKFrame](visionkit/VKSession.getVKFrame.md)
    - [VKSession.hitTest](visionkit/VKSession.hitTest.md)
    - [VKSession.off](visionkit/VKSession.off.md)
    - [VKSession.on](visionkit/VKSession.on.md)
    - [VKSession.removeMarker](visionkit/VKSession.removeMarker.md)
    - [VKSession.removeOSDMarker](visionkit/VKSession.removeOSDMarker.md)
    - [VKSession.requestAnimationFrame](visionkit/VKSession.requestAnimationFrame.md)
    - [VKSession.runOCR](visionkit/VKSession.runOCR.md)
    - [VKSession.setDepthOccRange](visionkit/VKSession.setDepthOccRange.md)
    - [VKSession.start](visionkit/VKSession.start.md)
    - [VKSession.stop](visionkit/VKSession.stop.md)
    - [VKSession.update3DMode](visionkit/VKSession.update3DMode.md)
    - [VKSession.updateMaskMode](visionkit/VKSession.updateMaskMode.md)
    - [VKSession.updateOSDThreshold](visionkit/VKSession.updateOSDThreshold.md)
- [人脸检测](face/wx.stopFaceDetect.md)
  - [wx.stopFaceDetect](face/wx.stopFaceDetect.md)
  - [wx.initFaceDetect](face/wx.initFaceDetect.md)
  - [wx.faceDetect](face/wx.faceDetect.md)
