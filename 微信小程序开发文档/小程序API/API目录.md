# 微信开放文档 / API

> 以下服务端接口可免 access_token 调用的场景：使用[微信云托管](https://developers.weixin.qq.com/miniprogram/dev/wxcloudrun/src/basic/intro.html)通过[微信令牌/开放接口服务](https://developers.weixin.qq.com/miniprogram/dev/wxcloudrun/src/guide/weixin/token.html)调用；使用[微信云开发](https://developers.weixin.qq.com/miniprogram/dev/wxcloud/basis/getting-started.html)通过云函数免服务器发起[云调用](https://developers.weixin.qq.com/miniprogram/dev/wxcloud/guide/openapi/openapi.html)。  

## 基础

|                                                       API                                                       | 功能                            |
| :-------------------------------------------------------------------------------------------------------------: | ----------------------------- |
|                 [wx.env](https://developers.weixin.qq.com/miniprogram/dev/api/base/wx.env.html)                 | 环境变量                          |
|             [wx.canIUse](https://developers.weixin.qq.com/miniprogram/dev/api/base/wx.canIUse.html)             | 判断小程序的API，回调，参数，组件等是否在当前版本可用  |
| [wx.base64ToArrayBuffer](https://developers.weixin.qq.com/miniprogram/dev/api/base/wx.base64ToArrayBuffer.html) | 将 Base64 字符串转成 ArrayBuffer 对象 |
| [wx.arrayBufferToBase64](https://developers.weixin.qq.com/miniprogram/dev/api/base/wx.arrayBufferToBase64.html) | 将 ArrayBuffer 对象转成 Base64 字符串 |

### 系统

| API                                                                                                                                  | 功能                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------- |
| [wx.openSystemBluetoothSetting](https://developers.weixin.qq.com/miniprogram/dev/api/base/system/wx.openSystemBluetoothSetting.html) | 跳转系统蓝牙设置页                                                                                                                     |
| [wx.openAppAuthorizeSetting](https://developers.weixin.qq.com/miniprogram/dev/api/base/system/wx.openAppAuthorizeSetting.html)       | 跳转系统微信授权管理页                                                                                                                   |
| [wx.getWindowInfo](https://developers.weixin.qq.com/miniprogram/dev/api/base/system/wx.getWindowInfo.html)                           | 获取窗口信息                                                                                                                        |
| [wx.getSystemSetting](https://developers.weixin.qq.com/miniprogram/dev/api/base/system/wx.getSystemSetting.html)                     | 获取设备设置                                                                                                                        |
| [wx.getSystemInfoSync](https://developers.weixin.qq.com/miniprogram/dev/api/base/system/wx.getSystemInfoSync.html)                   | [wx.getSystemInfo](https://developers.weixin.qq.com/miniprogram/dev/api/base/system/wx.getSystemInfo.html) 的同步版本              |
| [wx.getSystemInfoAsync](https://developers.weixin.qq.com/miniprogram/dev/api/base/system/wx.getSystemInfoAsync.html)                 | 异步获取系统信息                                                                                                                      |
| [wx.getSystemInfo](https://developers.weixin.qq.com/miniprogram/dev/api/base/system/wx.getSystemInfo.html)                           | 获取系统信息                                                                                                                        |
| [wx.getSkylineInfoSync](https://developers.weixin.qq.com/miniprogram/dev/api/base/system/wx.getSkylineInfoSync.html)                 | 获取当前运行环境对于 [Skyline 渲染引擎](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/introduction.html) 的支持情况 |
| [wx.getSkylineInfo](https://developers.weixin.qq.com/miniprogram/dev/api/base/system/wx.getSkylineInfo.html)                         | 获取当前运行环境对于 [Skyline 渲染引擎](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/introduction.html) 的支持情况 |
| [wx.getRendererUserAgent](https://developers.weixin.qq.com/miniprogram/dev/api/base/system/wx.getRendererUserAgent.html)             | 获取 Webview 小程序的 UserAgent                                                                                                     |
| [wx.getDeviceInfo](https://developers.weixin.qq.com/miniprogram/dev/api/base/system/wx.getDeviceInfo.html)                           | 获取设备基础信息                                                                                                                      |
| [wx.getDeviceBenchmarkInfo](https://developers.weixin.qq.com/miniprogram/dev/api/base/system/wx.getDeviceBenchmarkInfo.html)         | 获取设备性能得分和机型档位数据                                                                                                               |
| [wx.getAppBaseInfo](https://developers.weixin.qq.com/miniprogram/dev/api/base/system/wx.getAppBaseInfo.html)                         | 获取微信APP基础信息                                                                                                                   |
| [wx.getAppAuthorizeSetting](https://developers.weixin.qq.com/miniprogram/dev/api/base/system/wx.getAppAuthorizeSetting.html)<br>     | 获取微信APP授权设置                                                                                                                   |
### 更新

| API                                                                                                                                    | 功能                                                                                                                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [wx.updateWeChatApp](https://developers.weixin.qq.com/miniprogram/dev/api/base/update/wx.updateWeChatApp.html)                         | 更新客户端版本                                                                                                                                                                                                                                                                             |
| [wx.getUpdateManager](https://developers.weixin.qq.com/miniprogram/dev/api/base/update/wx.getUpdateManager.html)                       | 获取**全局唯一**的版本更新管理器，用于管理小程序更新[UpdateManager](https://developers.weixin.qq.com/miniprogram/dev/api/base/update/UpdateManager.html)UpdateManager 对象，用来管理更新，可通过 [wx.getUpdateManager](https://developers.weixin.qq.com/miniprogram/dev/api/base/update/wx.getUpdateManager.html) 接口获取实例 |
| [UpdateManager.applyUpdate](https://developers.weixin.qq.com/miniprogram/dev/api/base/update/UpdateManager.applyUpdate.html)           | 强制小程序重启并使用新版本                                                                                                                                                                                                                                                                       |
| [UpdateManager.onCheckForUpdate](https://developers.weixin.qq.com/miniprogram/dev/api/base/update/UpdateManager.onCheckForUpdate.html) | 监听向微信后台请求检查更新结果事件                                                                                                                                                                                                                                                                   |
| [UpdateManager.onUpdateFailed](https://developers.weixin.qq.com/miniprogram/dev/api/base/update/UpdateManager.onUpdateFailed.html)     | 监听小程序更新失败事件                                                                                                                                                                                                                                                                         |
| [UpdateManager.onUpdateReady](https://developers.weixin.qq.com/miniprogram/dev/api/base/update/UpdateManager.onUpdateReady.html)       | 监听小程序有版本更新事件<br>                                                                                                                                                                                                                                                                    |

### 生命周期

| API                                                                                                                              | 功能                 |
| -------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| [wx.onApiCategoryChange](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/life-cycle/wx.onApiCategoryChange.html)   | 监听 API 类别变化事件      |
| [wx.offApiCategoryChange](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/life-cycle/wx.offApiCategoryChange.html) | 移除 API 类别变化事件的监听函数 |
| [wx.getLaunchOptionsSync](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/life-cycle/wx.getLaunchOptionsSync.html) | 获取小程序启动时的参数        |
| [wx.getEnterOptionsSync](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/life-cycle/wx.getEnterOptionsSync.html)   | 获取本次小程序启动时的参数      |
| [wx.getApiCategory](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/life-cycle/wx.getApiCategory.html)             | 获取当前 API 类别        |

### 应用级事件

| API                                                                                                                                                     | 功能                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [wx.postMessageToReferrerPage](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.postMessageToReferrerPage.html)               | 向跳转的源页面发送消息                                                                                                                                                                                                                                               |
| [wx.postMessageToReferrerMiniProgram](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.postMessageToReferrerMiniProgram.html) | 向跳转的源小程序发送消息，源小程序可在 [wx.onShow](https://developers.weixin.qq.com/miniprogram/dev/api/errorwx.onShow)) 或 [wx.getEnterOptionsSync](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/life-cycle/wx.getEnterOptionsSync.html) 中通过 extraData 接收消息 |
| [wx.onUnhandledRejection](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.onUnhandledRejection.html)                         | 监听未处理的 Promise 拒绝事件                                                                                                                                                                                                                                       |
| [wx.onPageNotFound](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.onPageNotFound.html)                                     | 监听小程序要打开的页面不存在事件                                                                                                                                                                                                                                          |
| [wx.onThemeChange](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.onThemeChange.html)                                       | 监听系统主题改变事件                                                                                                                                                                                                                                                |
| [wx.onLazyLoadError](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.onLazyLoadError.html)                                   | 监听小程序异步组件加载失败事件                                                                                                                                                                                                                                           |
| [wx.onError](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.onError.html)                                                   | 监听小程序错误事件                                                                                                                                                                                                                                                 |
| [wx.onAudioInterruptionEnd](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.onAudioInterruptionEnd.html)                     | 监听音频中断结束事件                                                                                                                                                                                                                                                |
| [wx.onAudioInterruptionBegin](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.onAudioInterruptionBegin.html)                 | 监听音频因为受到系统占用而被中断开始事件                                                                                                                                                                                                                                      |
| [wx.onAppShow](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.onAppShow.html)                                               | 监听小程序切前台事件                                                                                                                                                                                                                                                |
| [wx.onAppHide](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.onAppHide.html)                                               | 监听小程序切后台事件                                                                                                                                                                                                                                                |
| [wx.offUnhandledRejection](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.offUnhandledRejection.html)                       | 移除未处理的 Promise 拒绝事件的监听函数                                                                                                                                                                                                                                  |
| [wx.offThemeChange](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.offThemeChange.html)                                     | 移除系统主题改变事件的监听函数                                                                                                                                                                                                                                           |
| [wx.offPageNotFound](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.offPageNotFound.html)                                   | 移除小程序要打开的页面不存在事件的监听函数                                                                                                                                                                                                                                     |
| [wx.offLazyLoadError](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.offLazyLoadError.html)                                 | 移除小程序异步组件加载失败事件的监听函数                                                                                                                                                                                                                                      |
| [wx.offError](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.offError.html)                                                 | 移除小程序错误事件的监听函数                                                                                                                                                                                                                                            |
| [wx.offAudioInterruptionEnd](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.offAudioInterruptionEnd.html)                   | 移除音频中断结束事件的监听函数                                                                                                                                                                                                                                           |
| [wx.offAudioInterruptionBegin](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.offAudioInterruptionBegin.html)               | 移除音频因为受到系统占用而被中断开始事件的监听函数                                                                                                                                                                                                                                 |
| [wx.offAppShow](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.offAppShow.html)                                             | 移除小程序切前台事件的监听函数                                                                                                                                                                                                                                           |
| [wx.offAppHide](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.offAppHide.html)                                             | 移除小程序切后台事件的监听函数                                                                                                                                                                                                                                           |


### 路由事件

| API                                                                                                                                                                                                                                                                   | 功能                                                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| [wx.onBeforePageUnload](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-route/wx.onBeforePageUnload.html)                                                                                                                                           | 监听路由事件引起现有页面实例销毁时，页面实例销毁前的事件监听，详见 [页面路由监听](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/route-event-listener.html) |
| [wx.onBeforePageLoad](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-route/wx.onBeforePageLoad.html)                                                                                                                                               | 监听路由事件引起新的页面实例化时，页面实例化前的事件监听，详见 [页面路由监听](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/route-event-listener.html)   |
| [wx.onBeforeAppRoute](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-route/wx.onBeforeAppRoute.html)                                                                                                                                               | 监听路由事件下发后，执行路由逻辑前的事件监听，详见 [页面路由监听](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/route-event-listener.html)         |
| [wx.onAppRouteDone](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-route/wx.onAppRouteDone.html)监听当前路由动画执行完成的事件监听，详见 [页面路由监听](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/route-event-listener.html)                    |                                                                                                                                              |
| [wx.onAppRoute](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-route/wx.onAppRoute.html)监听路由事件下发后，执行路由逻辑后的事件监听，详见 [页面路由监听](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/route-event-listener.html)                       |                                                                                                                                              |
| [wx.onAfterPageUnload](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-route/wx.onAfterPageUnload.html)监听路由事件引起现有页面实例销毁时，页面实例销毁后的事件监听，详见 [页面路由监听](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/route-event-listener.html) |                                                                                                                                              |
| [wx.onAfterPageLoad](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-route/wx.onAfterPageLoad.html)监听路由事件引起新的页面实例化时，页面实例化完成的事件监听，详见 [页面路由监听](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/route-event-listener.html)      |                                                                                                                                              |
| [wx.offBeforePageUnload](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-route/wx.offBeforePageUnload.html)移除路由事件的监听函数                                                                                                                              |                                                                                                                                              |
| [wx.offBeforePageLoad](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-route/wx.offBeforePageLoad.html)移除路由事件的监听函数                                                                                                                                  |                                                                                                                                              |
| [wx.offBeforeAppRoute](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-route/wx.offBeforeAppRoute.html)移除路由事件的监听函数                                                                                                                                  |                                                                                                                                              |
| [wx.offAppRouteDone](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-route/wx.offAppRouteDone.html)移除当前路由动画执行完成的事件的监听函数                                                                                                                             |                                                                                                                                              |
| [wx.offAppRoute](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-route/wx.offAppRoute.html)移除路由事件的监听函数                                                                                                                                              |                                                                                                                                              |
| [wx.offAfterPageUnload](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-route/wx.offAfterPageUnload.html)移除路由事件的监听函数                                                                                                                                |                                                                                                                                              |
| [wx.offAfterPageLoad](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-route/wx.offAfterPageLoad.html)移除路由事件的监听函数                                                                                                                                    |                                                                                                                                              |

### 调试

| API                                                                                                                       | 功能                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [wx.setEnableDebug](https://developers.weixin.qq.com/miniprogram/dev/api/base/debug/wx.setEnableDebug.html)               | 设置是否打开调试开关                                                                                                                                                |
| [wx.getRealtimeLogManager](https://developers.weixin.qq.com/miniprogram/dev/api/base/debug/wx.getRealtimeLogManager.html) | 获取实时日志管理器对象                                                                                                                                               |
| [wx.getLogManager](https://developers.weixin.qq.com/miniprogram/dev/api/base/debug/wx.getLogManager.html)                 | 获取日志管理器对象                                                                                                                                                 |
| [console](https://developers.weixin.qq.com/miniprogram/dev/api/base/debug/console.html)                                   | 向调试面板中打印日志                                                                                                                                                |
| [LogManager](https://developers.weixin.qq.com/miniprogram/dev/api/base/debug/LogManager.html)                             | 日志管理器实例，可以通过 [wx.getLogManager](https://developers.weixin.qq.com/miniprogram/dev/api/base/debug/wx.getLogManager.html) 获取                                 |
| [RealtimeLogManager](https://developers.weixin.qq.com/miniprogram/dev/api/base/debug/RealtimeLogManager.html)             | 实时日志管理器实例，可以通过 [wx.getRealtimeLogManager](https://developers.weixin.qq.com/miniprogram/dev/api/base/debug/wx.getRealtimeLogManager.html) 获取               |
| [RealtimeTagLogManager](https://developers.weixin.qq.com/miniprogram/dev/api/base/debug/RealtimeTagLogManager.html)       | 给定标签的实时日志管理器实例，可以通过 [RealtimeLogManager.tag](https://developers.weixin.qq.com/miniprogram/dev/api/base/debug/RealtimeLogManager.tag.html) 接口获取，目前只支持在插件使用 |


### 性能
| API                                                                                                                         | 功能                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| [wx.requestIdleCallback](https://developers.weixin.qq.com/miniprogram/dev/api/base/performance/wx.requestIdleCallback.html) | 注册一个函数，将在空闲时期被调用                                                                                                         |
| [wx.reportPerformance](https://developers.weixin.qq.com/miniprogram/dev/api/base/performance/wx.reportPerformance.html)     | 小程序测速上报                                                                                                                  |
| [wx.preloadWebview](https://developers.weixin.qq.com/miniprogram/dev/api/base/performance/wx.preloadWebview.html)           | 预加载下个页面的 WebView                                                                                                         |
| [wx.preloadSkylineView](https://developers.weixin.qq.com/miniprogram/dev/api/base/performance/wx.preloadSkylineView.html)   | 预加载下个页面所需要的 [Skyline](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/introduction.html) 运行环境 |
| [wx.preloadAssets](https://developers.weixin.qq.com/miniprogram/dev/api/base/performance/wx.preloadAssets.html)             | 为视图层预加载媒体资源文件, 目前支持：font，image                                                                                           |
| [wx.getPerformance](https://developers.weixin.qq.com/miniprogram/dev/api/base/performance/wx.getPerformance.html)           | 获取当前小程序性能相关的信息                                                                                                           |
| [wx.cancelIdleCallback](https://developers.weixin.qq.com/miniprogram/dev/api/base/performance/wx.cancelIdleCallback.html)   | 取消之前注册的指定回调函数                                                                                                            |
| [EntryList](https://developers.weixin.qq.com/miniprogram/dev/api/base/performance/EntryList.html)                           | EntryList 对象                                                                                                             |
| [Performance](https://developers.weixin.qq.com/miniprogram/dev/api/base/performance/Performance.html)                       | Performance 对象，用于获取性能数据及创建性能监听器                                                                                          |
| [PerformanceEntry](https://developers.weixin.qq.com/miniprogram/dev/api/base/performance/PerformanceEntry.html)             | 单条性能数据                                                                                                                   |
| [PerformanceObserver](https://developers.weixin.qq.com/miniprogram/dev/api/base/performance/PerformanceObserver.html)       | PerformanceObserver 对象，用于监听性能相关                                                                                          |

### 分包加载
| API                                                                                                                              | 功能                    |
| -------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| [wx.preDownloadSubpackage](https://developers.weixin.qq.com/miniprogram/dev/api/base/subpackage/wx.preDownloadSubpackage.html)   | 触发分包预下载               |
| [PreDownloadSubpackageTask](https://developers.weixin.qq.com/miniprogram/dev/api/base/subpackage/PreDownloadSubpackageTask.html) | 预下载分包任务实例，用于获取分包预下载状态 |
### 加密
| API                                                                                                                      | 功能       |
| ------------------------------------------------------------------------------------------------------------------------ | -------- |
| [wx.getUserCryptoManager](https://developers.weixin.qq.com/miniprogram/dev/api/base/crypto/wx.getUserCryptoManager.html) | 获取用户加密模块 |
| [UserCryptoManager](https://developers.weixin.qq.com/miniprogram/dev/api/base/crypto/UserCryptoManager.html)             | 用户加密模块   |

## 路由

| API                                                                                                | 功能                                                                                                                |
| -------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| [wx.switchTab](https://developers.weixin.qq.com/miniprogram/dev/api/route/wx.switchTab.html)       | 跳转到 tabBar 页面，并关闭其他所有非 tabBar 页面                                                                                  |
| [wx.rewriteRoute](https://developers.weixin.qq.com/miniprogram/dev/api/route/wx.rewriteRoute.html) | 重写正在进行中的路由事件，详见 [路由重写](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/route-rewrite.html) |
| [wx.reLaunch](https://developers.weixin.qq.com/miniprogram/dev/api/route/wx.reLaunch.html)         | 关闭所有页面，打开到应用内的某个页面                                                                                                |
| [wx.redirectTo](https://developers.weixin.qq.com/miniprogram/dev/api/route/wx.redirectTo.html)     | 关闭当前页面，跳转到应用内的某个页面                                                                                                |
| [wx.navigateTo](https://developers.weixin.qq.com/miniprogram/dev/api/route/wx.navigateTo.html)     | 保留当前页面，跳转到应用内的某个页面                                                                                                |
| [wx.navigateBack](https://developers.weixin.qq.com/miniprogram/dev/api/route/wx.navigateBack.html) | 关闭当前页面，返回上一页面或多级页面                                                                                                |
| [EventChannel](https://developers.weixin.qq.com/miniprogram/dev/api/route/EventChannel.html)       | 页面间事件通信通道                                                                                                         |
| [wx.router](https://developers.weixin.qq.com/miniprogram/dev/api/route/router/wx.router.html)      | outer 对象，可以通过 `wx.router` 获取（自定义路由）                                                                               |

## 跳转

| API                                                                                                                                               | 功能                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| [wx.restartMiniProgram](https://developers.weixin.qq.com/miniprogram/dev/api/navigate/wx.restartMiniProgram.html)                                 | 重启当前小程序                                           |
| [wx.openOfficialAccountProfile](https://developers.weixin.qq.com/miniprogram/dev/api/navigate/wx.openOfficialAccountProfile.html)                 | 通过小程序打开公众号主页                                      |
| [wx.openOfficialAccountChat](https://developers.weixin.qq.com/miniprogram/dev/api/navigate/wx.openOfficialAccountChat.html)                       | 通过小程序打开公众号会话界面                                    |
| [wx.openOfficialAccountArticle](https://developers.weixin.qq.com/miniprogram/dev/api/navigate/wx.openOfficialAccountArticle.html)                 | 通过小程序打开任意公众号文章（不包括临时链接等异常状态下的公众号文章），必须有点击行为才能调用成功 |
| [wx.openEmbeddedMiniProgram](https://developers.weixin.qq.com/miniprogram/dev/api/navigate/wx.openEmbeddedMiniProgram.html)                       | 打开半屏小程序                                           |
| [wx.onEmbeddedMiniProgramHeightChange](https://developers.weixin.qq.com/miniprogram/dev/api/navigate/wx.onEmbeddedMiniProgramHeightChange.html)   | 监听半屏小程序可视高度变化事件                                   |
| [wx.offEmbeddedMiniProgramHeightChange](https://developers.weixin.qq.com/miniprogram/dev/api/navigate/wx.offEmbeddedMiniProgramHeightChange.html) | 移除半屏小程序可视高度变化事件的监听函数                              |
| [wx.navigateToMiniProgram](https://developers.weixin.qq.com/miniprogram/dev/api/navigate/wx.navigateToMiniProgram.html)                           | 打开另一个小程序                                          |
| [wx.navigateBackMiniProgram](https://developers.weixin.qq.com/miniprogram/dev/api/navigate/wx.navigateBackMiniProgram.html)                       | 返回到上一个小程序                                         |
| [wx.exitMiniProgram](https://developers.weixin.qq.com/miniprogram/dev/api/navigate/wx.exitMiniProgram.html)                                       | 退出当前小程序                                           |



## 聊天工具

| API                                                                                                                       | 功能                                       |
| ------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| [wx.shareVideoToGroup](https://developers.weixin.qq.com/miniprogram/dev/api/chattool/wx.shareVideoToGroup.html)           | 转发视频到聊天                                  |
| [wx.shareImageToGroup](https://developers.weixin.qq.com/miniprogram/dev/api/chattool/wx.shareImageToGroup.html)           | 转发图片到聊天                                  |
| [wx.shareFileToGroup](https://developers.weixin.qq.com/miniprogram/dev/api/chattool/wx.shareFileToGroup.html)             | 转发文件到聊天                                  |
| [wx.shareEmojiToGroup](https://developers.weixin.qq.com/miniprogram/dev/api/chattool/wx.shareEmojiToGroup.html)           | 转发表情到聊天                                  |
| [wx.shareAppMessageToGroup](https://developers.weixin.qq.com/miniprogram/dev/api/chattool/wx.shareAppMessageToGroup.html) | 转发小程序卡片到聊天                               |
| [wx.selectGroupMembers](https://developers.weixin.qq.com/miniprogram/dev/api/chattool/wx.selectGroupMembers.html)         | 选择聊天室的成员，并返回选择成员的 group_openid           |
| [wx.openChatTool](https://developers.weixin.qq.com/miniprogram/dev/api/chattool/wx.openChatTool.html)                     | 进入聊天工具模式                                 |
| [wx.notifyGroupMembers](https://developers.weixin.qq.com/miniprogram/dev/api/chattool/wx.notifyGroupMembers.html)         | 提醒用户完成任务，标题长度不超过 30 个字符，支持中英文和数字，中文算2个字符 |
| [wx.getChatToolInfo](https://developers.weixin.qq.com/miniprogram/dev/api/chattool/wx.getChatToolInfo.html)               | 获取聊天工具模式下的群聊信息                           |

## 转发

| API                                                                                                                    | 功能                                |
| ---------------------------------------------------------------------------------------------------------------------- | --------------------------------- |
| [wx.updateShareMenu](https://developers.weixin.qq.com/miniprogram/dev/api/share/wx.updateShareMenu.html)               | 更新转发属性                            |
| [wx.showShareMenu](https://developers.weixin.qq.com/miniprogram/dev/api/share/wx.showShareMenu.html)                   | 设置右上角点开的详情界面中的分享按钮是否可用            |
| [wx.showShareImageMenu](https://developers.weixin.qq.com/miniprogram/dev/api/share/wx.showShareImageMenu.html)         | 打开分享图片弹窗，可以将图片发送给朋友、分享至朋友圈、收藏或下载  |
| [wx.shareVideoMessage](https://developers.weixin.qq.com/miniprogram/dev/api/share/wx.shareVideoMessage.html)           | 转发视频到聊天                           |
| [wx.shareToOfficialAccount](https://developers.weixin.qq.com/miniprogram/dev/api/share/wx.shareToOfficialAccount.html) | 支持拉起公众号图文发表页，用户可将图片与文字内容发表至公众号    |
| [wx.shareFileMessage](https://developers.weixin.qq.com/miniprogram/dev/api/share/wx.shareFileMessage.html)             | 转发文件到聊天                           |
| [wx.onCopyUrl](https://developers.weixin.qq.com/miniprogram/dev/api/share/wx.onCopyUrl.html)                           | 监听用户点击右上角菜单的「复制链接」按钮时触发的事件        |
| [wx.offCopyUrl](https://developers.weixin.qq.com/miniprogram/dev/api/share/wx.offCopyUrl.html)                         | 移除用户点击右上角菜单的「复制链接」按钮时触发的事件的全部监听函数 |
| [wx.hideShareMenu](https://developers.weixin.qq.com/miniprogram/dev/api/share/wx.hideShareMenu.html)                   | 隐藏当前页面的转发按钮                       |
| [wx.getShareInfo](https://developers.weixin.qq.com/miniprogram/dev/api/share/wx.getShareInfo.html)                     | 获取转发详细信息（主要是获取群ID）                |
| [wx.authPrivateMessage](https://developers.weixin.qq.com/miniprogram/dev/api/share/wx.authPrivateMessage.html)         | 验证私密消息                            |

## 界面
### 交互

| API                                                                                                                                 | 功能             |
| ----------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| [wx.showToast](https://developers.weixin.qq.com/miniprogram/dev/api/ui/interaction/wx.showToast.html)                               | 显示消息提示框        |
| [wx.showModal](https://developers.weixin.qq.com/miniprogram/dev/api/ui/interaction/wx.showModal.html)                               | 显示模态对话框        |
| [wx.showLoading](https://developers.weixin.qq.com/miniprogram/dev/api/ui/interaction/wx.showLoading.html)                           | 显示 loading 提示框 |
| [wx.showActionSheet](https://developers.weixin.qq.com/miniprogram/dev/api/ui/interaction/wx.showActionSheet.html)                   | 显示操作菜单         |
| [wx.hideToast](https://developers.weixin.qq.com/miniprogram/dev/api/ui/interaction/wx.hideToast.html)                               | 隐藏消息提示框        |
| [wx.hideLoading](https://developers.weixin.qq.com/miniprogram/dev/api/ui/interaction/wx.hideLoading.html)                           | 隐藏 loading 提示框 |
| [wx.enableAlertBeforeUnload](https://developers.weixin.qq.com/miniprogram/dev/api/ui/interaction/wx.enableAlertBeforeUnload.html)   | 开启小程序页面返回询问对话框 |
| [wx.disableAlertBeforeUnload](https://developers.weixin.qq.com/miniprogram/dev/api/ui/interaction/wx.disableAlertBeforeUnload.html) | 关闭小程序页面返回询问对话框 |

### 导航栏
| API                                                                                                                                    | 功能             |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| [wx.showNavigationBarLoading](https://developers.weixin.qq.com/miniprogram/dev/api/ui/navigation-bar/wx.showNavigationBarLoading.html) | 在当前页面显示导航条加载动画 |
| [wx.setNavigationBarTitle](https://developers.weixin.qq.com/miniprogram/dev/api/ui/navigation-bar/wx.setNavigationBarTitle.html)       | 动态设置当前页面的标题    |
| [wx.setNavigationBarColor](https://developers.weixin.qq.com/miniprogram/dev/api/ui/navigation-bar/wx.setNavigationBarColor.html)       | 设置页面导航条颜色      |
| [wx.hideNavigationBarLoading](https://developers.weixin.qq.com/miniprogram/dev/api/ui/navigation-bar/wx.hideNavigationBarLoading.html) | 在当前页面隐藏导航条加载动画 |
| [wx.hideHomeButton](https://developers.weixin.qq.com/miniprogram/dev/api/ui/navigation-bar/wx.hideHomeButton.html)                     | 隐藏返回首页按钮       |
### 背景
| API                                                                                                                            | 功能                      |
| ------------------------------------------------------------------------------------------------------------------------------ | ----------------------- |
| [wx.setBackgroundTextStyle](https://developers.weixin.qq.com/miniprogram/dev/api/ui/background/wx.setBackgroundTextStyle.html) | 动态设置下拉背景字体、loading 图的样式 |
| [wx.setBackgroundColor](https://developers.weixin.qq.com/miniprogram/dev/api/ui/background/wx.setBackgroundColor.html)         | 动态设置窗口的背景色              |
### Tab Bar
| API                                                                                                               | 功能                                        |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| [wx.showTabBarRedDot](https://developers.weixin.qq.com/miniprogram/dev/api/ui/tab-bar/wx.showTabBarRedDot.html)   | 显示 tabBar 某一项的右上角的红点                      |
| [wx.showTabBar](https://developers.weixin.qq.com/miniprogram/dev/api/ui/tab-bar/wx.showTabBar.html)               | 显示 tabBar                                 |
| [wx.setTabBarStyle](https://developers.weixin.qq.com/miniprogram/dev/api/ui/tab-bar/wx.setTabBarStyle.html)       | 动态设置 tabBar 的整体样式                         |
| [wx.setTabBarItem](https://developers.weixin.qq.com/miniprogram/dev/api/ui/tab-bar/wx.setTabBarItem.html)         | 动态设置 tabBar 某一项的内容，`2.7.0` 起图片支持临时文件和网络文件 |
| [wx.setTabBarBadge](https://developers.weixin.qq.com/miniprogram/dev/api/ui/tab-bar/wx.setTabBarBadge.html)       | 为 tabBar 某一项的右上角添加文本                      |
| [wx.removeTabBarBadge](https://developers.weixin.qq.com/miniprogram/dev/api/ui/tab-bar/wx.removeTabBarBadge.html) | 移除 tabBar 某一项右上角的文本                       |
| [wx.hideTabBarRedDot](https://developers.weixin.qq.com/miniprogram/dev/api/ui/tab-bar/wx.hideTabBarRedDot.html)   | 隐藏 tabBar 某一项的右上角的红点                      |
| [wx.hideTabBar](https://developers.weixin.qq.com/miniprogram/dev/api/ui/tab-bar/wx.hideTabBar.html)               | 隐藏 tabBar                                 |
### 字体
| API                                                                                                                | 功能       |
| ------------------------------------------------------------------------------------------------------------------ | -------- |
| [wx.loadFontFace](https://developers.weixin.qq.com/miniprogram/dev/api/ui/font/wx.loadFontFace.html)               | 动态加载网络字体 |
| [wx.loadBuiltInFontFace](https://developers.weixin.qq.com/miniprogram/dev/api/ui/font/wx.loadBuiltInFontFace.html) | 加载内置字体   |
### 下拉刷新
| API                                                                                                                               | 功能         |
| --------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| [wx.stopPullDownRefresh](https://developers.weixin.qq.com/miniprogram/dev/api/ui/pull-down-refresh/wx.stopPullDownRefresh.html)   | 停止当前页面下拉刷新 |
| [wx.startPullDownRefresh](https://developers.weixin.qq.com/miniprogram/dev/api/ui/pull-down-refresh/wx.startPullDownRefresh.html) | 开始下拉刷新     |
### 滚动
| API                                                                                                        | 功能                                                                                                                                                                                                                                       |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [wx.pageScrollTo](https://developers.weixin.qq.com/miniprogram/dev/api/ui/scroll/wx.pageScrollTo.html)     | 将页面滚动到目标位置，支持选择器和滚动距离两种方式定位                                                                                                                                                                                                              |
| [ScrollViewContext](https://developers.weixin.qq.com/miniprogram/dev/api/ui/scroll/ScrollViewContext.html) | 增强 ScrollView 实例，可通过 [wx.createSelectorQuery](https://developers.weixin.qq.com/miniprogram/dev/api/wxml/wx.createSelectorQuery.html) 的 [NodesRef.node](https://developers.weixin.qq.com/miniprogram/dev/api/wxml/NodesRef.node.html)方法获取 |
### 动画

| API                                                                                                             | 功能                                                                                                     |
| --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| [wx.createAnimation](https://developers.weixin.qq.com/miniprogram/dev/api/ui/animation/wx.createAnimation.html) | 创建一个动画实例 [animation](https://developers.weixin.qq.com/miniprogram/dev/api/ui/animation/Animation.html) |
| [Animation](https://developers.weixin.qq.com/miniprogram/dev/api/ui/animation/Animation.html)                   | 动画对象                                                                                                   |
### 顶置
| API                                                                                                      | 功能          |
| -------------------------------------------------------------------------------------------------------- | ----------- |
| [wx.setTopBarText](https://developers.weixin.qq.com/miniprogram/dev/api/ui/sticky/wx.setTopBarText.html) | 动态设置置顶栏文字内容 |

### 自定义组件
| API                                                                                                      | 功能                |
| -------------------------------------------------------------------------------------------------------- | ----------------- |
| [wx.nextTick](https://developers.weixin.qq.com/miniprogram/dev/api/ui/custom-component/wx.nextTick.html) | 延迟一部分操作到下一个时间片再执行 |
### 菜单
| API                                                                                                                                                                | 功能                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------- |
| [ wx.onOnUserTriggerTranslation](https://developers.weixin.qq.com/miniprogram/dev/api/ui/menu/wx.onOnUserTriggerTranslation.html)                                  | 监听用户触发小程序菜单中翻译功能的事件             |
| [wx.onMenuButtonBoundingClientRectWeightChange](https://developers.weixin.qq.com/miniprogram/dev/api/ui/menu/wx.onMenuButtonBoundingClientRectWeightChange.html)   | 监听菜单按钮（右上角胶囊按钮）的布局位置信息变化事件      |
| [wx.offOnUserTriggerTranslation](https://developers.weixin.qq.com/miniprogram/dev/api/ui/menu/wx.offOnUserTriggerTranslation.html)                                 | 移除用户触发小程序菜单中翻译功能的事件的监听函数        |
| [wx.offMenuButtonBoundingClientRectWeightChange](https://developers.weixin.qq.com/miniprogram/dev/api/ui/menu/wx.offMenuButtonBoundingClientRectWeightChange.html) | 移除菜单按钮（右上角胶囊按钮）的布局位置信息变化事件的监听函数 |
| [wx.getMenuButtonBoundingClientRect](https://developers.weixin.qq.com/miniprogram/dev/api/ui/menu/wx.getMenuButtonBoundingClientRect.html)                         | 获取菜单按钮（右上角胶囊按钮）的布局位置信息          |
### 窗口
| API                                                                                                                                      | 功能                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| [wx.setWindowSize](https://developers.weixin.qq.com/miniprogram/dev/api/ui/window/wx.setWindowSize.html)                                 | 设置窗口大小，该接口仅适用于 PC 平台，使用细则请参见指南                      |
| [wx.onWindowStateChange](https://developers.weixin.qq.com/miniprogram/dev/api/ui/window/wx.onWindowStateChange.html)                     | 监听小程序窗口状态变化事件                                       |
| [wx.onWindowResize](https://developers.weixin.qq.com/miniprogram/dev/api/ui/window/wx.onWindowResize.html)                               | 监听窗口尺寸变化事件                                          |
| [wx.onOnParallelStateChange](https://developers.weixin.qq.com/miniprogram/dev/api/ui/window/wx.onOnParallelStateChange.html)             | 监听小程序分栏状态变化事件                                       |
| [wx.offWindowStateChange](https://developers.weixin.qq.com/miniprogram/dev/api/ui/window/wx.offWindowStateChange.html)                   | 移除小程序窗口状态变化事件的监听函数                                  |
| [wx.offWindowResize](https://developers.weixin.qq.com/miniprogram/dev/api/ui/window/wx.offWindowResize.html)                             | 移除窗口尺寸变化事件的监听函数                                     |
| [wx.offOnParallelStateChange](https://developers.weixin.qq.com/miniprogram/dev/api/ui/window/wx.offOnParallelStateChange.html)           | 移除小程序分栏状态变化事件的监听函数                                  |
| [wx.checkIsPictureInPictureActive](https://developers.weixin.qq.com/miniprogram/dev/api/ui/window/wx.checkIsPictureInPictureActive.html) | 返回当前是否存在小窗播放（小窗在 video/live-player/live-pusher 下可用） |
### worklet动画
| API                                                                                           | 功能                              |
| --------------------------------------------------------------------------------------------- | ------------------------------- |
| [wx.worklet](https://developers.weixin.qq.com/miniprogram/dev/api/ui/worklet/wx.worklet.html) | worklet 对象，可以通过 `wx.worklet` 获取 |
#### 基础
| API                                                                                                                                                | 功能                                                 |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| [  worklet.cancelAnimation](https://developers.weixin.qq.com/miniprogram/dev/api/ui/worklet/base/worklet.cancelAnimation.html)                     | 取消由 `SharedValue` 驱动的动画                            |
| [worklet.derived](https://developers.weixin.qq.com/miniprogram/dev/api/ui/worklet/base/worklet.derived.html)                                       | 衍生值 `DerivedValue`，可基于已有的 `SharedValue` 生成其它共享变量   |
| [worklet.scrollViewContext](https://developers.weixin.qq.com/miniprogram/dev/api/ui/worklet/base/worklet.scrollViewContext.html)                   | `ScrollView` 实例，可在 `worklet` 函数内操作 `scroll-view`组件 |
| [worklet.scrollViewContext.scrollTo](https://developers.weixin.qq.com/miniprogram/dev/api/ui/worklet/base/worklet.scrollViewContext.scrollTo.html) | 滚动至指定位置                                            |
| [worklet.shared](https://developers.weixin.qq.com/miniprogram/dev/api/ui/worklet/base/worklet.shared.html)                                         | 创建共享变量 `SharedValue`，用于跨线程共享数据和驱动动画                |
#### 动画
| API                                                                                                             | 功能                                                                                                                                                         |     |
| --------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
| [worklet.decay](https://developers.weixin.qq.com/miniprogram/dev/api/ui/worklet/animation/worklet.decay.html)   | 基于滚动衰减的动画                                                                                                                                                  |     |
| [worklet.Easing](https://developers.weixin.qq.com/miniprogram/dev/api/ui/worklet/animation/worklet.Easing.html) | Easing 模块实现了常见的动画缓动函数（动画效果参考 https://easings.net/ ），可从 [wx.worklet](https://developers.weixin.qq.com/miniprogram/dev/api/ui/worklet/wx.worklet.html) 对象中读取 |     |
| [worklet.spring](https://developers.weixin.qq.com/miniprogram/dev/api/ui/worklet/animation/worklet.spring.html) | 基于物理的动画                                                                                                                                                    |     |
| [worklet.timing](https://developers.weixin.qq.com/miniprogram/dev/api/ui/worklet/animation/worklet.timing.html) | 基于时间的动画                                                                                                                                                    |     |
#### 组合动画
| API                                                                                                                         | 功能               |
| --------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| [worklet.delay](https://developers.weixin.qq.com/miniprogram/dev/api/ui/worklet/combine-animation/worklet.delay.html)       | 延迟执行动画           |
| [worklet.repeat](https://developers.weixin.qq.com/miniprogram/dev/api/ui/worklet/combine-animation/worklet.repeat.html)     | 重复执行动画           |
| [worklet.sequence](https://developers.weixin.qq.com/miniprogram/dev/api/ui/worklet/combine-animation/worklet.sequence.html) | 组合动画序列，依次执行传入的动画 |
#### 工具函数
| API                                                                                                                   | 功能                                                                                                |
| --------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| [worklet.runOnJS](https://developers.weixin.qq.com/miniprogram/dev/api/ui/worklet/tool-function/worklet.runOnJS.html) | `worklet` 函数运行在 `UI` 线程时，捕获的外部函数可能为 `worklet` 类型或普通函数，为了更明显的对其区分，要求必须使用 `runOnJS` 调回 `JS` 线程的普通函数 |
| [worklet.runOnUI](https://developers.weixin.qq.com/miniprogram/dev/api/ui/worklet/tool-function/worklet.runOnUI.html) | 在 UI 线程执行 worklet 函数                                                                              |

## 网络
### 发起请求
| API                                                                                                  | 功能            |
| ---------------------------------------------------------------------------------------------------- | ------------- |
| [wx.request](https://developers.weixin.qq.com/miniprogram/dev/api/network/request/wx.request.html)   | 发起 HTTPS 网络请求 |
| [RequestTask](https://developers.weixin.qq.com/miniprogram/dev/api/network/request/RequestTask.html) | 网络请求任务对象      |
### 下载
| API                                                                                                           | 功能                         |
| ------------------------------------------------------------------------------------------------------------- | -------------------------- |
| [wx.downloadFile](https://developers.weixin.qq.com/miniprogram/dev/api/network/download/wx.downloadFile.html) | 下载文件资源到本地                  |
| [DownloadTask](https://developers.weixin.qq.com/miniprogram/dev/api/network/download/DownloadTask.html)       | 一个可以监听下载进度变化事件，以及取消下载任务的对象 |
### 上传
| API                                                                                                       | 功能                         |
| --------------------------------------------------------------------------------------------------------- | -------------------------- |
| [  wx.uploadFile](https://developers.weixin.qq.com/miniprogram/dev/api/network/upload/wx.uploadFile.html) | 将本地资源上传到服务器                |
| [UploadTask](https://developers.weixin.qq.com/miniprogram/dev/api/network/upload/UploadTask.html)         | 一个可以监听上传进度变化事件，以及取消上传任务的对象 |
### WebSocket
| API                                                                                                                      | 功能                                         |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------ |
| [wx.sendSocketMessage](https://developers.weixin.qq.com/miniprogram/dev/api/network/websocket/wx.sendSocketMessage.html) | 通过 WebSocket 连接发送数据                        |
| [wx.onSocketOpen](https://developers.weixin.qq.com/miniprogram/dev/api/network/websocket/wx.onSocketOpen.html)           | 监听 WebSocket 连接打开事件                        |
| [wx.onSocketMessage](https://developers.weixin.qq.com/miniprogram/dev/api/network/websocket/wx.onSocketMessage.html)     | 监听 WebSocket 接收到服务器的消息事件                   |
| [wx.onSocketError](https://developers.weixin.qq.com/miniprogram/dev/api/network/websocket/wx.onSocketError.html)         | 监听 WebSocket 错误事件                          |
| [wx.onSocketClose](https://developers.weixin.qq.com/miniprogram/dev/api/network/websocket/wx.onSocketClose.html)         | 监听 WebSocket 连接关闭事件                        |
| [wx.connectSocket](https://developers.weixin.qq.com/miniprogram/dev/api/network/websocket/wx.connectSocket.html)         | 创建一个 WebSocket 连接                          |
| [wx.closeSocket](https://developers.weixin.qq.com/miniprogram/dev/api/network/websocket/wx.closeSocket.html)             | 关闭 WebSocket 连接                            |
| [SocketTask](https://developers.weixin.qq.com/miniprogram/dev/api/network/websocket/SocketTask.html)                     | WebSocket 任务，可通过 wx.connectSocket() 接口创建返回 |
### mDNS
| API                                                                                                                                       | 功能                     |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| [ wx.stopLocalServiceDiscovery](https://developers.weixin.qq.com/miniprogram/dev/api/network/mdns/wx.stopLocalServiceDiscovery.html)      | 停止搜索 mDNS 服务           |
| [wx.startLocalServiceDiscovery](https://developers.weixin.qq.com/miniprogram/dev/api/network/mdns/wx.startLocalServiceDiscovery.html)     | 开始搜索局域网下的 mDNS 服务      |
| [wx.onLocalServiceResolveFail](https://developers.weixin.qq.com/miniprogram/dev/api/network/mdns/wx.onLocalServiceResolveFail.html)       | 监听 mDNS 服务解析失败的事件      |
| [wx.onLocalServiceLost](https://developers.weixin.qq.com/miniprogram/dev/api/network/mdns/wx.onLocalServiceLost.html)                     | 监听 mDNS 服务离开的事件        |
| [wx.onLocalServiceFound](https://developers.weixin.qq.com/miniprogram/dev/api/network/mdns/wx.onLocalServiceFound.html)                   | 监听 mDNS 服务发现的事件        |
| [wx.onLocalServiceDiscoveryStop](https://developers.weixin.qq.com/miniprogram/dev/api/network/mdns/wx.onLocalServiceDiscoveryStop.html)   | 监听 mDNS 服务停止搜索的事件      |
| [wx.offLocalServiceResolveFail](https://developers.weixin.qq.com/miniprogram/dev/api/network/mdns/wx.offLocalServiceResolveFail.html)     | 移除 mDNS 服务解析失败的事件的监听函数 |
| [wx.offLocalServiceLost](https://developers.weixin.qq.com/miniprogram/dev/api/network/mdns/wx.offLocalServiceLost.html)                   | 移除 mDNS 服务离开的事件的监听函数   |
| [wx.offLocalServiceFound](https://developers.weixin.qq.com/miniprogram/dev/api/network/mdns/wx.offLocalServiceFound.html)                 | 移除 mDNS 服务发现的事件的监听函数   |
| [wx.offLocalServiceDiscoveryStop](https://developers.weixin.qq.com/miniprogram/dev/api/network/mdns/wx.offLocalServiceDiscoveryStop.html) | 移除 mDNS 服务停止搜索的事件的监听函数 |
### TCP通信
| API                                                                                                            | 功能                            |
| -------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| [wx.createTCPSocket](https://developers.weixin.qq.com/miniprogram/dev/api/network/tcp/wx.createTCPSocket.html) | 创建一个 TCP Socket 实例            |
| [TCPSocket](https://developers.weixin.qq.com/miniprogram/dev/api/network/tcp/TCPSocket.html)                   | 一个 TCP Socket 实例，默认使用 IPv4 协议 |
### UDP通信
| API                                                                                                            | 功能                            |
| -------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| [wx.createUDPSocket](https://developers.weixin.qq.com/miniprogram/dev/api/network/udp/wx.createUDPSocket.html) | 创建一个 UDP Socket 实例            |
| [UDPSocket](https://developers.weixin.qq.com/miniprogram/dev/api/network/udp/UDPSocket.html)                   | 一个 UDP Socket 实例，默认使用 IPv4 协议 |

## 支付

| API                                                                                                                        | 功能                                  |
| -------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| [wx.requestVirtualPayment](https://developers.weixin.qq.com/miniprogram/dev/api/payment/wx.requestVirtualPayment.html)     | 发起米大师虚拟支付                           |
| [wx.requestPluginPayment](https://developers.weixin.qq.com/miniprogram/dev/api/payment/wx.requestPluginPayment.html)       | 插件中发起支付                             |
| [wx.requestPayment](https://developers.weixin.qq.com/miniprogram/dev/api/payment/wx.requestPayment.html)                   | 发起微信支付                              |
| [wx.requestMerchantTransfer](https://developers.weixin.qq.com/miniprogram/dev/api/payment/wx.requestMerchantTransfer.html) | 商家转账用户确认模式下，在微信客户端通过小程序拉起页面请求用户确认收款 |
| [wx.requestCommonPayment](https://developers.weixin.qq.com/miniprogram/dev/api/payment/wx.requestCommonPayment.html)       | 发起通用支付                              |
| [wx.openHKOfflinePayView](https://developers.weixin.qq.com/miniprogram/dev/api/payment/wx.openHKOfflinePayView.html)       | 拉起WeChat Pay HK付款码                  |
| [wx.createGlobalPayment](https://developers.weixin.qq.com/miniprogram/dev/api/payment/wx.createGlobalPayment.html)         | 创建全球支付方式的对象                         |
| [GlobalPayment](https://developers.weixin.qq.com/miniprogram/dev/api/payment/GlobalPayment.html)                           | 全球收银对象 GlobalPayment                |

## 数据缓存

| 名称                                                                                                                 | 功能                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------- |
| [wx.setStorageSync](https://developers.weixin.qq.com/miniprogram/dev/api/storage/wx.setStorageSync.html)           | 将数据存储在本地缓存中指定的 key 中                                                                                           |
| [wx.setStorage](https://developers.weixin.qq.com/miniprogram/dev/api/storage/wx.setStorage.html)                   | 将数据存储在本地缓存中指定的 key 中                                                                                           |
| [wx.revokeBufferURL](https://developers.weixin.qq.com/miniprogram/dev/api/storage/wx.revokeBufferURL.html)         | 根据 URL 销毁存在内存中的数据                                                                                              |
| [wx.removeStorageSync](https://developers.weixin.qq.com/miniprogram/dev/api/storage/wx.removeStorageSync.html)     | [wx.removeStorage](https://developers.weixin.qq.com/miniprogram/dev/api/storage/wx.removeStorage.html) 的同步版本   |
| [wx.removeStorage](https://developers.weixin.qq.com/miniprogram/dev/api/storage/wx.removeStorage.html)             | 从本地缓存中移除指定 key                                                                                                 |
| [wx.getStorageSync](https://developers.weixin.qq.com/miniprogram/dev/api/storage/wx.getStorageSync.html)           | 从本地缓存中同步获取指定 key 的内容                                                                                           |
| [wx.getStorageInfoSync](https://developers.weixin.qq.com/miniprogram/dev/api/storage/wx.getStorageInfoSync.html)   | [wx.getStorageInfo](https://developers.weixin.qq.com/miniprogram/dev/api/storage/wx.getStorageInfo.html) 的同步版本 |
| [wx.getStorageInfo](https://developers.weixin.qq.com/miniprogram/dev/api/storage/wx.getStorageInfo.html)           | 异步获取当前storage的相关信息                                                                                             |
| [wx.getStorage](https://developers.weixin.qq.com/miniprogram/dev/api/storage/wx.getStorage.html)                   | 从本地缓存中异步获取指定 key 的内容                                                                                           |
| [wx.createBufferURL](https://developers.weixin.qq.com/miniprogram/dev/api/storage/wx.createBufferURL.html)         | 根据传入的 buffer 创建一个唯一的 URL 存在内存中                                                                                 |
| [wx.clearStorageSync](https://developers.weixin.qq.com/miniprogram/dev/api/storage/wx.clearStorageSync.html)       | [wx.clearStorage](https://developers.weixin.qq.com/miniprogram/dev/api/storage/wx.clearStorage.html) 的同步版本     |
| [wx.clearStorage](https://developers.weixin.qq.com/miniprogram/dev/api/storage/wx.clearStorage.html)               | 清理本地数据缓存                                                                                                       |
| [wx.batchSetStorageSync](https://developers.weixin.qq.com/miniprogram/dev/api/storage/wx.batchSetStorageSync.html) | 将数据批量存储在本地缓存中指定的 key 中                                                                                         |
| [wx.batchSetStorage](https://developers.weixin.qq.com/miniprogram/dev/api/storage/wx.batchSetStorage.html)         | 将数据批量存储在本地缓存中指定的 key 中                                                                                         |
| [wx.batchGetStorageSync](https://developers.weixin.qq.com/miniprogram/dev/api/storage/wx.batchGetStorageSync.html) | 从本地缓存中同步批量获取指定 key 的内容                                                                                         |
| [wx.batchGetStorage](https://developers.weixin.qq.com/miniprogram/dev/api/storage/wx.batchGetStorage.html)         | 从本地缓存中异步批量获取指定 key 的内容                                                                                         |

### 数据预拉取和周期性更新
| API                                                                                                                                           | 功能                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| [  wx.setBackgroundFetchToken](https://developers.weixin.qq.com/miniprogram/dev/api/storage/background-fetch/wx.setBackgroundFetchToken.html) | 设置自定义登录态，在周期性拉取数据时带上，便于第三方服务器验证请求合法性 |
| [wx.onBackgroundFetchData](https://developers.weixin.qq.com/miniprogram/dev/api/storage/background-fetch/wx.onBackgroundFetchData.html)       | 监听收到 backgroundFetch 数据事件            |
| [wx.getBackgroundFetchToken](https://developers.weixin.qq.com/miniprogram/dev/api/storage/background-fetch/wx.getBackgroundFetchToken.html)   | 获取设置过的自定义登录态                         |
| [wx.getBackgroundFetchData](https://developers.weixin.qq.com/miniprogram/dev/api/storage/background-fetch/wx.getBackgroundFetchData.html)     | 拉取 backgroundFetch 客户端缓存数据           |
### 缓存管理器

| API                                                                                                                           | 功能      |
| ----------------------------------------------------------------------------------------------------------------------------- | ------- |
| [wx.createCacheManager](https://developers.weixin.qq.com/miniprogram/dev/api/storage/cachemanager/wx.createCacheManager.html) | 创建缓存管理器 |
| [CacheManager](https://developers.weixin.qq.com/miniprogram/dev/api/storage/cachemanager/CacheManager.html)                   | 缓存管理器   |
## 数据分析



| API                                                                                                              | 功能                  |
| ---------------------------------------------------------------------------------------------------------------- | ------------------- |
| [wx.reportMonitor](https://developers.weixin.qq.com/miniprogram/dev/api/data-analysis/wx.reportMonitor.html)     | 自定义业务数据监控上报接口       |
| [wx.reportEvent](https://developers.weixin.qq.com/miniprogram/dev/api/data-analysis/wx.reportEvent.html)         | 事件上报                |
| [wx.reportAnalytics](https://developers.weixin.qq.com/miniprogram/dev/api/data-analysis/wx.reportAnalytics.html) | 自定义分析数据上报接口         |
| [wx.getExptInfoSync](https://developers.weixin.qq.com/miniprogram/dev/api/data-analysis/wx.getExptInfoSync.html) | 给定实验参数数组，获取对应的实验参数值 |
| [wx.getCommonConfig](https://developers.weixin.qq.com/miniprogram/dev/api/data-analysis/wx.getCommonConfig.html) | 给定实验参数数组，获取对应的实验参数值 |



## 画布



| API                                                                                                                   | 功能                                                                                                                                        |
| --------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| [wx.createOffscreenCanvas](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/wx.createOffscreenCanvas.html) | 创建离屏 canvas 实例                                                                                                                            |
| [wx.createCanvasContext](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/wx.createCanvasContext.html)     | 创建 canvas 的绘图上下文 [CanvasContext](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.html) 对象                       |
| [wx.canvasToTempFilePath](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/wx.canvasToTempFilePath.html)   | 把当前画布指定区域的内容导出生成指定大小的图片                                                                                                                   |
| [wx.canvasPutImageData](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/wx.canvasPutImageData.html)       | 将像素数据绘制到画布                                                                                                                                |
| [wx.canvasGetImageData](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/wx.canvasGetImageData.html)       | 获取 canvas 区域隐含的像素数据                                                                                                                       |
| [Canvas](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/Canvas.html)                                     | Canvas 实例，可通过 [SelectorQuery](https://developers.weixin.qq.com/miniprogram/dev/api/wxml/SelectorQuery.html) 获取                            |
| [CanvasGradient](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasGradient.html)                     | 渐变对象                                                                                                                                      |
| [Color](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/Color.html)                                       | 颜色                                                                                                                                        |
| [Image](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/Image.html)                                       | 图片对象                                                                                                                                      |
| [ImageData](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/ImageData.html)                               | ImageData 对象                                                                                                                              |
| [OffscreenCanvas](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/OffscreenCanvas.html)                   | 离屏 canvas 实例，可通过 [wx.createOffscreenCanvas](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/wx.createOffscreenCanvas.html) 创建 |
| [Path2D](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/Path2D.html)                                     | Canvas 2D API 的接口 Path2D 用来声明路径，此路径稍后会被CanvasRenderingContext2D 对象使用                                                                      |
| [RenderingContext](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/RenderingContext.html)                 | Canvas 绘图上下文                                                                                                                              |



## 媒体
### 地图
| API                                                                                                            | 功能                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [wx.createMapContext](https://developers.weixin.qq.com/miniprogram/dev/api/media/map/wx.createMapContext.html) | 创建 [map](https://developers.weixin.qq.com/miniprogram/dev/component/map.html) 上下文 [MapContext](https://developers.weixin.qq.com/miniprogram/dev/api/media/map/MapContext.html) 对象 |
| [MapContext](https://developers.weixin.qq.com/miniprogram/dev/api/media/map/MapContext.html)                   | MapContext 实例，可通过 [wx.createMapContext](https://developers.weixin.qq.com/miniprogram/dev/api/media/map/wx.createMapContext.html) 获取                                               |
### 图片
| API                                                                                                                          | 功能               |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| [wx.saveImageToPhotosAlbum](https://developers.weixin.qq.com/miniprogram/dev/api/media/image/wx.saveImageToPhotosAlbum.html) | 保存图片到系统相册        |
| [wx.previewMedia](https://developers.weixin.qq.com/miniprogram/dev/api/media/image/wx.previewMedia.html)                     | 预览图片和视频          |
| [wx.previewImage](https://developers.weixin.qq.com/miniprogram/dev/api/media/image/wx.previewImage.html)                     | 在新页面中全屏预览图片      |
| [wx.getImageInfo](https://developers.weixin.qq.com/miniprogram/dev/api/media/image/wx.getImageInfo.html)                     | 获取图片信息           |
| [wx.editImage](https://developers.weixin.qq.com/miniprogram/dev/api/media/image/wx.editImage.html)                           | 编辑图片接口           |
| [wx.cropImage](https://developers.weixin.qq.com/miniprogram/dev/api/media/image/wx.cropImage.html)                           | 裁剪图片接口           |
| [wx.compressImage](https://developers.weixin.qq.com/miniprogram/dev/api/media/image/wx.compressImage.html)                   | 压缩图片接口，可选压缩质量    |
| [wx.chooseMessageFile](https://developers.weixin.qq.com/miniprogram/dev/api/media/image/wx.chooseMessageFile.html)           | 从客户端会话选择文件       |
| [wx.chooseImage](https://developers.weixin.qq.com/miniprogram/dev/api/media/image/wx.chooseImage.html)                       | 从本地相册选择图片或使用相机拍照 |
### 视频

| API                                                                                                                          | 功能                                                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [wx.saveVideoToPhotosAlbum](https://developers.weixin.qq.com/miniprogram/dev/api/media/video/wx.saveVideoToPhotosAlbum.html) | 保存视频到系统相册                                                                                                                                                                                   |
| [wx.openVideoEditor](https://developers.weixin.qq.com/miniprogram/dev/api/media/video/wx.openVideoEditor.html)               | 打开视频编辑器                                                                                                                                                                                     |
| [wx.getVideoInfo](https://developers.weixin.qq.com/miniprogram/dev/api/media/video/wx.getVideoInfo.html)                     | 获取视频详细信息                                                                                                                                                                                    |
| [wx.createVideoContext](https://developers.weixin.qq.com/miniprogram/dev/api/media/video/wx.createVideoContext.html)         | 创建 [video](https://developers.weixin.qq.com/miniprogram/dev/component/video.html) 上下文 [VideoContext](https://developers.weixin.qq.com/miniprogram/dev/api/media/video/VideoContext.html) 对象 |
| [wx.compressVideo](https://developers.weixin.qq.com/miniprogram/dev/api/media/video/wx.compressVideo.html)                   | 压缩视频接口                                                                                                                                                                                      |
| [wx.chooseVideo](https://developers.weixin.qq.com/miniprogram/dev/api/media/video/wx.chooseVideo.html)                       | 拍摄视频或从手机相册中选视频                                                                                                                                                                              |
| [wx.chooseMedia](https://developers.weixin.qq.com/miniprogram/dev/api/media/video/wx.chooseMedia.html)                       | 拍摄或从手机相册中选择图片或视频                                                                                                                                                                            |
| [wx.checkDeviceSupportHevc](https://developers.weixin.qq.com/miniprogram/dev/api/media/video/wx.checkDeviceSupportHevc.html) | 查询设备是否支持 H.265 编码                                                                                                                                                                           |
| [VideoContext](https://developers.weixin.qq.com/miniprogram/dev/api/media/video/VideoContext.html)                           | VideoContext 实例，可通过 [wx.createVideoContext](https://developers.weixin.qq.com/miniprogram/dev/api/media/video/wx.createVideoContext.html) 获取                                                 |
|                                                                                                                              |                                                                                                                                                                                             |

### 音频
| API                                                                                                                              | 功能                                                                                                                                                                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [wx.stopVoice](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/wx.stopVoice.html)                               | 结束播放语音                                                                                                                                                                                                                                                                                                                              |
| [wx.setInnerAudioOption](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/wx.setInnerAudioOption.html)           | 设置 [InnerAudioContext](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/InnerAudioContext.html) 的播放选项                                                                                                                                                                                                               |
| [wx.playVoice](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/wx.playVoice.html)                               | 开始播放语音                                                                                                                                                                                                                                                                                                                              |
| [wx.pauseVoice](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/wx.pauseVoice.html)                             | 暂停正在播放的语音                                                                                                                                                                                                                                                                                                                           |
| [wx.getAvailableAudioSources](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/wx.getAvailableAudioSources.html) | 获取当前支持的音频输入源                                                                                                                                                                                                                                                                                                                        |
| [wx.createWebAudioContext](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/wx.createWebAudioContext.html)       | 创建 WebAudio 上下文                                                                                                                                                                                                                                                                                                                     |
| [wx.createMediaAudioPlayer](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/wx.createMediaAudioPlayer.html)     | 创建媒体音频播放器对象 [MediaAudioPlayer](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/MediaAudioPlayer.html) 对象，可用于播放视频解码器 [VideoDecoder](https://developers.weixin.qq.com/miniprogram/dev/api/media/video-decoder/VideoDecoder.html) 输出的音频                                                                               |
| [wx.createInnerAudioContext](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/wx.createInnerAudioContext.html)   | 创建内部 [audio](https://developers.weixin.qq.com/miniprogram/dev/component/audio.html) 上下文 [InnerAudioContext](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/InnerAudioContext.html) 对象                                                                                                                             |
| [wx.createAudioContext](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/wx.createAudioContext.html)             | 创建 [audio](https://developers.weixin.qq.com/miniprogram/dev/component/audio.html) 上下文 [AudioContext](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/AudioContext.html) 对象                                                                                                                                         |
| [AudioBuffer](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/AudioBuffer.html)                                 | AudioBuffer接口表示存在内存里的一段短小的音频资源，利用[WebAudioContext.decodeAudioData](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/WebAudioContext.decodeAudioData.html)方法从一个音频文件构建，或者利用 [WebAudioContext.createBuffer](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/WebAudioContext.createBuffer.html)从原始数据构建 |
| [AudioContext](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/AudioContext.html)                               | [AudioContext](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/AudioContext.html) 实例，可通过 [wx.createAudioContext](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/wx.createAudioContext.html) 获取                                                                                                   |
| [AudioListener](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/AudioListener.html)                             | 空间音频监听器，代表在一个音频场景内唯一的位置和方向信息                                                                                                                                                                                                                                                                                                        |
| [AudioParam](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/AudioParam.html)                                   | AudioParam 接口代表音频相关的参数，通常是 AudioNode（例如 GainNode.gain）的参数                                                                                                                                                                                                                                                                           |
| [BufferSourceNode](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/BufferSourceNode.html)                       | 音频源节点，通过 [WebAudioContext.createBufferSource](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/WebAudioContext.createBufferSource.html)方法获得                                                                                                                                                                         |
| [InnerAudioContext](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/InnerAudioContext.html)                     | InnerAudioContext 实例，可通过 [wx.createInnerAudioContext](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/wx.createInnerAudioContext.html)接口获取实例                                                                                                                                                                       |
| [MediaAudioPlayer](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/MediaAudioPlayer.html)                       | MediaAudioPlayer 实例，可通过 [wx.createMediaAudioPlayer](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/wx.createMediaAudioPlayer.html)接口获取实例                                                                                                                                                                          |
| [WebAudioContext](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/WebAudioContext.html)                         | WebAudioContext 实例，通过[wx.createWebAudioContext](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/wx.createWebAudioContext.html) 接口获取该实例                                                                                                                                                                             |
| [WebAudioContextNode](https://developers.weixin.qq.com/miniprogram/dev/api/media/audio/WebAudioContextNode.html)                 | 一类音频处理模块，不同的Node具备不同的功能，如GainNode(音量调整)等                                                                                                                                                                                                                                                                                            |

### 背景音频
| API                                                                                                                                                   | 功能                                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [wx.stopBackgroundAudio](https://developers.weixin.qq.com/miniprogram/dev/api/media/background-audio/wx.stopBackgroundAudio.html)                     | 停止播放音乐                                                                                                                                                                         |
| [wx.seekBackgroundAudio](https://developers.weixin.qq.com/miniprogram/dev/api/media/background-audio/wx.seekBackgroundAudio.html)                     | 控制音乐播放进度                                                                                                                                                                       |
| [wx.playBackgroundAudio](https://developers.weixin.qq.com/miniprogram/dev/api/media/background-audio/wx.playBackgroundAudio.html)                     | 使用后台播放器播放音乐                                                                                                                                                                    |
| [wx.pauseBackgroundAudio](https://developers.weixin.qq.com/miniprogram/dev/api/media/background-audio/wx.pauseBackgroundAudio.html)                   | 暂停播放音乐                                                                                                                                                                         |
| [wx.onBackgroundAudioStop](https://developers.weixin.qq.com/miniprogram/dev/api/media/background-audio/wx.onBackgroundAudioStop.html)                 | 监听音乐停止事件                                                                                                                                                                       |
| [wx.onBackgroundAudioPlay](https://developers.weixin.qq.com/miniprogram/dev/api/media/background-audio/wx.onBackgroundAudioPlay.html)                 | 监听音乐播放事件                                                                                                                                                                       |
| [wx.onBackgroundAudioPause](https://developers.weixin.qq.com/miniprogram/dev/api/media/background-audio/wx.onBackgroundAudioPause.html)               | 监听音乐暂停事件                                                                                                                                                                       |
| [wx.getBackgroundAudioPlayerState](https://developers.weixin.qq.com/miniprogram/dev/api/media/background-audio/wx.getBackgroundAudioPlayerState.html) | 获取后台音乐播放状态                                                                                                                                                                     |
| [wx.getBackgroundAudioManager](https://developers.weixin.qq.com/miniprogram/dev/api/media/background-audio/wx.getBackgroundAudioManager.html)         | 获取**全局唯一**的背景音频管理器                                                                                                                                                             |
| [BackgroundAudioManager](https://developers.weixin.qq.com/miniprogram/dev/api/media/background-audio/BackgroundAudioManager.html)                     | BackgroundAudioManager 实例，可通过 [wx.getBackgroundAudioManager](https://developers.weixin.qq.com/miniprogram/dev/api/media/background-audio/wx.getBackgroundAudioManager.html) 获取 |

### 实时音频
| API                                                                                                                           | 功能                                                                                                                                                                                                               |
| ----------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [wx.createLivePusherContext](https://developers.weixin.qq.com/miniprogram/dev/api/media/live/wx.createLivePusherContext.html) | 创建 [live-pusher](https://developers.weixin.qq.com/miniprogram/dev/component/live-pusher.html) 上下文 [LivePusherContext](https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePusherContext.html) 对象 |
| [wx.createLivePlayerContext](https://developers.weixin.qq.com/miniprogram/dev/api/media/live/wx.createLivePlayerContext.html) | 创建 [live-player](https://developers.weixin.qq.com/miniprogram/dev/component/live-player.html) 上下文 [LivePlayerContext](https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePlayerContext.html) 对象 |
| [LivePlayerContext](https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePlayerContext.html)                   | `LivePlayerContext` 实例，可通过 [wx.createLivePlayerContext](https://developers.weixin.qq.com/miniprogram/dev/api/media/live/wx.createLivePlayerContext.html) 获取                                                      |
| [LivePusherContext](https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePusherContext.html)                   | LivePusherContext 实例，可通过 [wx.createLivePusherContext](https://developers.weixin.qq.com/miniprogram/dev/api/media/live/wx.createLivePusherContext.html)获取                                                         |
### 录音
| API                                                                                                                     | 功能                               |
| ----------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| [wx.stopRecord](https://developers.weixin.qq.com/miniprogram/dev/api/media/recorder/wx.stopRecord.html)                 | 停止录音                             |
| [wx.startRecord](https://developers.weixin.qq.com/miniprogram/dev/api/media/recorder/wx.startRecord.html)               | 开始录音                             |
| [wx.getRecorderManager](https://developers.weixin.qq.com/miniprogram/dev/api/media/recorder/wx.getRecorderManager.html) | 获取**全局唯一**的录音管理器 RecorderManager |
| [RecorderManager](https://developers.weixin.qq.com/miniprogram/dev/api/media/recorder/RecorderManager.html)             | 全局唯一的录音管理器                       |

### 相机
| API                                                                                                                     | 功能                                                                                                                                                                                               |
| ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [wx.createCameraContext](https://developers.weixin.qq.com/miniprogram/dev/api/media/camera/wx.createCameraContext.html) | 创建 [camera](https://developers.weixin.qq.com/miniprogram/dev/component/camera.html) 上下文 [CameraContext](https://developers.weixin.qq.com/miniprogram/dev/api/media/camera/CameraContext.html) 对象 |
| [CameraContext](https://developers.weixin.qq.com/miniprogram/dev/api/media/camera/CameraContext.html)                   | CameraContext 实例，可通过 [wx.createCameraContext](https://developers.weixin.qq.com/miniprogram/dev/api/media/camera/wx.createCameraContext.html) 获取                                                  |
| [CameraFrameListener](https://developers.weixin.qq.com/miniprogram/dev/api/media/camera/CameraFrameListener.html)       | CameraContext.onCameraFrame() 返回的监听器                                                                                                                                                             |

### 富文本
| API                                                                                                   | 功能                                                                                                                                      |
| ----------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| [EditorContext](https://developers.weixin.qq.com/miniprogram/dev/api/media/editor/EditorContext.html) | EditorContext 实例，可通过 [wx.createSelectorQuery](https://developers.weixin.qq.com/miniprogram/dev/api/wxml/wx.createSelectorQuery.html) 获取 |
### 音视频合成
| API                                                                                                                                 | 功能                                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [wx.createMediaContainer](https://developers.weixin.qq.com/miniprogram/dev/api/media/video-processing/wx.createMediaContainer.html) | 创建音视频处理容器，最终可将容器中的轨道合成一个视频                                                                                                                                   |
| [MediaContainer](https://developers.weixin.qq.com/miniprogram/dev/api/media/video-processing/MediaContainer.html)                   | 可通过 [wx.createMediaContainer](https://developers.weixin.qq.com/miniprogram/dev/api/media/video-processing/wx.createMediaContainer.html) 创建                   |
| [MediaTrack](https://developers.weixin.qq.com/miniprogram/dev/api/media/video-processing/MediaTrack.html)                           | 可通过 [MediaContainer.extractDataSource](https://developers.weixin.qq.com/miniprogram/dev/api/media/video-processing/MediaContainer.extractDataSource.html) 返回 |
### 实时语音
| API                                                                                                                                 | 功能                                                                                                                     |
| ----------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| [wx.updateVoIPChatMuteConfig](https://developers.weixin.qq.com/miniprogram/dev/api/media/voip/wx.updateVoIPChatMuteConfig.html)     | 更新实时语音静音设置                                                                                                             |
| [wx.subscribeVoIPVideoMembers](https://developers.weixin.qq.com/miniprogram/dev/api/media/voip/wx.subscribeVoIPVideoMembers.html)   | 订阅视频画面成员                                                                                                               |
| [wx.setEnable1v1Chat](https://developers.weixin.qq.com/miniprogram/dev/api/media/voip/wx.setEnable1v1Chat.html)                     | 开启双人通话                                                                                                                 |
| [wx.onVoIPVideoMembersChanged](https://developers.weixin.qq.com/miniprogram/dev/api/media/voip/wx.onVoIPVideoMembersChanged.html)   | 监听实时语音通话成员视频状态变化事件                                                                                                     |
| [wx.onVoIPChatStateChanged](https://developers.weixin.qq.com/miniprogram/dev/api/media/voip/wx.onVoIPChatStateChanged.html)         | 监听房间状态变化事件                                                                                                             |
| [wx.onVoIPChatSpeakersChanged](https://developers.weixin.qq.com/miniprogram/dev/api/media/voip/wx.onVoIPChatSpeakersChanged.html)   | 监听实时语音通话成员通话状态变化事件                                                                                                     |
| [wx.onVoIPChatMembersChanged](https://developers.weixin.qq.com/miniprogram/dev/api/media/voip/wx.onVoIPChatMembersChanged.html)     | 监听实时语音通话成员在线状态变化事件                                                                                                     |
| [wx.onVoIPChatInterrupted](https://developers.weixin.qq.com/miniprogram/dev/api/media/voip/wx.onVoIPChatInterrupted.html)           | 监听被动断开实时语音通话事件                                                                                                         |
| [wx.offVoIPVideoMembersChanged](https://developers.weixin.qq.com/miniprogram/dev/api/media/voip/wx.offVoIPVideoMembersChanged.html) | 移除实时语音通话成员视频状态变化事件的监听函数                                                                                                |
| [wx.offVoIPChatStateChanged](https://developers.weixin.qq.com/miniprogram/dev/api/media/voip/wx.offVoIPChatStateChanged.html)       | 移除房间状态变化事件的监听函数                                                                                                        |
| [wx.offVoIPChatSpeakersChanged](https://developers.weixin.qq.com/miniprogram/dev/api/media/voip/wx.offVoIPChatSpeakersChanged.html) | 移除实时语音通话成员通话状态变化事件的监听函数                                                                                                |
| [wx.offVoIPChatMembersChanged](https://developers.weixin.qq.com/miniprogram/dev/api/media/voip/wx.offVoIPChatMembersChanged.html)   | 移除实时语音通话成员在线状态变化事件的监听函数                                                                                                |
| [wx.offVoIPChatInterrupted](https://developers.weixin.qq.com/miniprogram/dev/api/media/voip/wx.offVoIPChatInterrupted.html)         | 移除被动断开实时语音通话事件的监听函数                                                                                                    |
| [wx.joinVoIPChat](https://developers.weixin.qq.com/miniprogram/dev/api/media/voip/wx.joinVoIPChat.html)                             | 加入 (创建) 实时语音通话，更多信息可见 [实时语音指南](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/voip-chat.html) |
| [wx.join1v1Chat](https://developers.weixin.qq.com/miniprogram/dev/api/media/voip/wx.join1v1Chat.html)                               | 加入（创建）双人通话                                                                                                             |
| [wx.exitVoIPChat](https://developers.weixin.qq.com/miniprogram/dev/api/media/voip/wx.exitVoIPChat.html)                             | 退出（销毁）实时语音通话                                                                                                           |
### 画面录制器
| API                                                                                                                             | 功能                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| [wx.createMediaRecorder](https://developers.weixin.qq.com/miniprogram/dev/api/media/media-recorder/wx.createMediaRecorder.html) | 创建 WebGL 画面录制器，可逐帧录制在 WebGL 上渲染的画面并导出视频文件                                                                                              |
| [MediaRecorder](https://developers.weixin.qq.com/miniprogram/dev/api/media/media-recorder/MediaRecorder.html)                   | 可通过 [wx.createMediaRecorder](https://developers.weixin.qq.com/miniprogram/dev/api/media/media-recorder/wx.createMediaRecorder.html) 创建 |

### 视频解码器
| API                                                                                                                          | 功能                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| [wx.createVideoDecoder](https://developers.weixin.qq.com/miniprogram/dev/api/media/video-decoder/wx.createVideoDecoder.html) | 创建视频解码器，可逐帧获取解码后的数据                                                                                                                 |
| [VideoDecoder](https://developers.weixin.qq.com/miniprogram/dev/api/media/video-decoder/VideoDecoder.html)                   | 可通过 [wx.createVideoDecoder](https://developers.weixin.qq.com/miniprogram/dev/api/media/video-decoder/wx.createVideoDecoder.html) 创建 |

## 位置

| API                                                                                                                                     | 功能                                                                                                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [wx.stopLocationUpdate](https://developers.weixin.qq.com/miniprogram/dev/api/location/wx.stopLocationUpdate.html)                       | 关闭监听实时位置变化，前后台都停止消息接收                                                                                                                                                                                                                                                          |
| [wx.startLocationUpdateBackground](https://developers.weixin.qq.com/miniprogram/dev/api/location/wx.startLocationUpdateBackground.html) | 开启小程序在前后台时均可接收位置消息，后台包括离开小程序后继续使用微信（微信仍在前台）、离开微信（微信在后台）两个场景，需引导用户开启[授权](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/authorize.html#后台定位)                                                                                                           |
| [wx.startLocationUpdate](https://developers.weixin.qq.com/miniprogram/dev/api/location/wx.startLocationUpdate.html)                     | 开启小程序进入前台时接收位置消息                                                                                                                                                                                                                                                               |
| [wx.openLocation](https://developers.weixin.qq.com/miniprogram/dev/api/location/wx.openLocation.html)                                   | 使用微信内置地图查看位置                                                                                                                                                                                                                                                                   |
| [wx.onLocationChangeError](https://developers.weixin.qq.com/miniprogram/dev/api/location/wx.onLocationChangeError.html)                 | 监听持续定位接口返回失败时触发                                                                                                                                                                                                                                                                |
| [wx.onLocationChange](https://developers.weixin.qq.com/miniprogram/dev/api/location/wx.onLocationChange.html)                           | 监听实时地理位置变化事件，需结合 [wx.startLocationUpdateBackground](https://developers.weixin.qq.com/miniprogram/dev/api/location/wx.startLocationUpdateBackground.html)、[wx.startLocationUpdate](https://developers.weixin.qq.com/miniprogram/dev/api/location/wx.startLocationUpdate.html)使用 |
| [wx.offLocationChangeError](https://developers.weixin.qq.com/miniprogram/dev/api/location/wx.offLocationChangeError.html)               | 移除持续定位接口返回失败时触发                                                                                                                                                                                                                                                                |
| [wx.offLocationChange](https://developers.weixin.qq.com/miniprogram/dev/api/location/wx.offLocationChange.html)                         | 移除实时地理位置变化事件的监听函数                                                                                                                                                                                                                                                              |
| [wx.getLocation](https://developers.weixin.qq.com/miniprogram/dev/api/location/wx.getLocation.html)                                     | 获取当前的地理位置、速度                                                                                                                                                                                                                                                                   |
| [wx.getFuzzyLocation](https://developers.weixin.qq.com/miniprogram/dev/api/location/wx.getFuzzyLocation.html)                           | 获取当前的模糊地理位置                                                                                                                                                                                                                                                                    |
| [wx.choosePoi](https://developers.weixin.qq.com/miniprogram/dev/api/location/wx.choosePoi.html)                                         | 打开POI列表选择位置，支持模糊定位（精确到市）和精确定位混选                                                                                                                                                                                                                                                |
| [wx.chooseLocation](https://developers.weixin.qq.com/miniprogram/dev/api/location/wx.chooseLocation.html)                               | 打开地图选择位置                                                                                                                                                                                                                                                                       |



## 文件



| API                                                                                                               | 功能                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| [wx.saveFileToDisk](https://developers.weixin.qq.com/miniprogram/dev/api/file/wx.saveFileToDisk.html)             | 保存文件系统的文件到用户磁盘，仅在 PC 端支持                                                                                                       |
| [wx.openDocument](https://developers.weixin.qq.com/miniprogram/dev/api/file/wx.openDocument.html)                 | 新开页面打开文档                                                                                                                       |
| [wx.getFileSystemManager](https://developers.weixin.qq.com/miniprogram/dev/api/file/wx.getFileSystemManager.html) | 获取全局唯一的文件管理器                                                                                                                   |
| [FileStats](https://developers.weixin.qq.com/miniprogram/dev/api/file/FileStats.html)                             | 每个 FileStats 对象包含 path 和 Stats                                                                                                 |
| [FileSystemManager](https://developers.weixin.qq.com/miniprogram/dev/api/file/FileSystemManager.html)             | 文件管理器，可通过 [wx.getFileSystemManager](https://developers.weixin.qq.com/miniprogram/dev/api/file/wx.getFileSystemManager.html) 获取 |
| [ReadResult](https://developers.weixin.qq.com/miniprogram/dev/api/file/ReadResult.html)                           | 文件读取结果                                                                                                                         |
| [Stats](https://developers.weixin.qq.com/miniprogram/dev/api/file/Stats.html)                                     | 描述文件状态的对象                                                                                                                      |
| [WriteResult](https://developers.weixin.qq.com/miniprogram/dev/api/file/WriteResult.html)                         | 文件写入结果                                                                                                                         |



## 开放接口

### 登录
| API                                                                                                         | 功能                                      |
| ----------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| [wx.pluginLogin](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/login/wx.pluginLogin.html)   | **该接口仅在小程序插件中可调用**，调用接口获得插件用户标志凭证（code） |
| [wx.login](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/login/wx.login.html)               | 调用接口获取登录凭证（code）                        |
| [wx.checkSession](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/login/wx.checkSession.html) | 检查登录态 session_key 是否过期                  |
### 账号信息
| API                                                                                                                            | 功能       |
| ------------------------------------------------------------------------------------------------------------------------------ | -------- |
| [wx.getAccountInfoSync](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/account-info/wx.getAccountInfoSync.html) | 获取当前账号信息 |
### 用户信息
| API                                                                                                                 | 功能     |
| ------------------------------------------------------------------------------------------------------------------- | ------ |
| [wx.getUserProfile](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/user-info/wx.getUserProfile.html) | 获取用户信息 |
| [wx.getUserInfo](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/user-info/wx.getUserInfo.html)       | 获取用户信息 |
| [UserInfo](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/user-info/UserInfo.html)                   | 用户信息   |
### 授权
| API                                                                                                                                     | 功能                                                                                                                              |
| --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| [  wx.authorizeForMiniProgram](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/authorize/wx.authorizeForMiniProgram.html) | **仅小程序插件中能调用该接口**，用法同 [wx.authorize](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/authorize/wx.authorize.html) |
| [wx.authorize](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/authorize/wx.authorize.html)                               | 提前向用户发起授权请求                                                                                                                     |
### 设置
| API                                                                                                                     | 功能                                                                                                        |
| ----------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| [wx.openSetting](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/setting/wx.openSetting.html)             | 调起客户端小程序设置界面，返回用户设置的操作结果                                                                                  |
| [wx.getSetting](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/setting/wx.getSetting.html)               | 获取用户的当前设置                                                                                                 |
| [AuthSetting](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/setting/AuthSetting.html)                   | 用户授权设置信息，详情参考[权限](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/authorize.html) |
| [SubscriptionsSetting](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/setting/SubscriptionsSetting.html) | 订阅消息设置                                                                                                    |
### 收货地址
| API                                                                                                               | 功能       |
| ----------------------------------------------------------------------------------------------------------------- | -------- |
| [  wx.chooseAddress](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/address/wx.chooseAddress.html) | 获取用户收货地址 |
### 卡卷
| API                                                                                                | 功能         |
| -------------------------------------------------------------------------------------------------- | ---------- |
| [wx.openCard](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/card/wx.openCard.html) | 查看微信卡包中的卡券 |
| [wx.addCard](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/card/wx.addCard.html)   | 批量添加卡券     |
### 发票
| API                                                                                                                       | 功能        |
| ------------------------------------------------------------------------------------------------------------------------- | --------- |
| [wx.chooseInvoiceTitle](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/invoice/wx.chooseInvoiceTitle.html) | 选择用户的发票抬头 |
| [wx.chooseInvoice](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/invoice/wx.chooseInvoice.html)           | 选择用户已有的发票 |
### 生物认证
| API                                                                                                                                                   | 功能                   |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| [ wx.startSoterAuthentication](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/soter/wx.startSoterAuthentication.html)                  | 开始 SOTER 生物认证        |
| [wx.checkIsSupportSoterAuthentication](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/soter/wx.checkIsSupportSoterAuthentication.html) | 获取本机支持的 SOTER 生物认证方式 |
| [wx.checkIsSoterEnrolledInDevice](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/soter/wx.checkIsSoterEnrolledInDevice.html)           | 获取设备内是否录入如指纹等生物信息的接口 |
### 微信运动
| API                                                                                                         | 功能               |
| ----------------------------------------------------------------------------------------------------------- | ---------------- |
| [wx.shareToWeRun](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/werun/wx.shareToWeRun.html) | 分享数据到微信运动        |
| [wx.getWeRunData](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/werun/wx.getWeRunData.html) | 获取用户过去三十一天微信运动步数 |
### 订阅消息
| API                                                                                                                                                       | 功能                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| [wx.requestSubscribeMessage](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/subscribe-message/wx.requestSubscribeMessage.html)             | 调起客户端小程序订阅消息界面，返回用户订阅消息的操作结果             |
| [wx.requestSubscribeDeviceMessage](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/subscribe-message/wx.requestSubscribeDeviceMessage.html) | 订阅设备消息接口，调用后弹出授权框，用户同意后会允许开发者给用户发送订阅模版消息 |
### 微信红包
| API                                                                                                                  | 功能          |
| -------------------------------------------------------------------------------------------------------------------- | ----------- |
| [wx.showRedPackage](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/redpackage/wx.showRedPackage.html) | 拉取h5领取红包封面页 |
### 微信小店
| API                                                                                                                           | 功能           |
| ----------------------------------------------------------------------------------------------------------------------------- | ------------ |
| [wx.openStoreOrderDetail](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/store/wx.openStoreOrderDetail.html)   | 打开微信小店订单详情页  |
| [wx.openStoreCouponDetail](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/store/wx.openStoreCouponDetail.html) | 打开微信小店优惠券详情页 |
### 收藏
| API                                                                                                                           | 功能   |
| ----------------------------------------------------------------------------------------------------------------------------- | ---- |
| [wx.addVideoToFavorites](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/favorites/wx.addVideoToFavorites.html) | 收藏视频 |
| [wx.addFileToFavorites](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/favorites/wx.addFileToFavorites.html)   | 收藏文件 |
### 用工关系
| API                                                                                                                                                           | 功能                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| [wx.requestSubscribeEmployeeMessage](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/employee-relation/wx.requestSubscribeEmployeeMessage.html) | 在用户已绑定与该小程序的[用工关系](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/laboruse/intro.html)后，可拉起用户关系消息订阅列表      |
| [wx.checkEmployeeRelation](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/employee-relation/wx.checkEmployeeRelation.html)                     | 检查小程序[用工关系](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/laboruse/intro.html)功能和用户之间的绑定关系                |
| [wx.bindEmployeeRelation](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/employee-relation/wx.bindEmployeeRelation.html)                       | 拉起小程序[用工关系](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/laboruse/intro.html)功能绑定弹窗，用户允许后可同步拉起用户关系消息订阅列表 |
### 我的小程序
| API                                                                                                                                                | 功能                 |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| [wx.checkIsAddedToMyMiniProgram](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/my-miniprogram/wx.checkIsAddedToMyMiniProgram.html) | 检查小程序是否被添加至 「我的小程序 |
### 车牌
| API                                                                                                                             | 功能    |
| ------------------------------------------------------------------------------------------------------------------------------- | ----- |
| [wx.chooseLicensePlate](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/license-plate/wx.chooseLicensePlate.html) | 选择车牌号 |
### 视频号
| API                                                                                                                                      | 功能                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| [wx.reserveChannelsLive](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/channels/wx.reserveChannelsLive.html)             | 预约视频号直播                                                                             |
| [wx.openChannelsUserProfile](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/channels/wx.openChannelsUserProfile.html)     | 打开视频号主页                                                                             |
| [wx.openChannelsLive](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/channels/wx.openChannelsLive.html)                   | 打开视频号直播                                                                             |
| [wx.openChannelsEvent](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/channels/wx.openChannelsEvent.html)                 | 打开视频号活动页                                                                            |
| [wx.openChannelsActivity](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/channels/wx.openChannelsActivity.html)           | 打开视频号视频                                                                             |
| [wx.getChannelsShareKey](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/channels/wx.getChannelsShareKey.html)             | 获取视频号直播卡片/视频卡片的分享来源，仅当卡片携带了分享信息、同时用户已授权该小程序获取视频号分享信息且启动场景值为 1177、1184、1195、1208 时可用 |
| [wx.getChannelsLiveNoticeInfo](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/channels/wx.getChannelsLiveNoticeInfo.html) | 获取视频号直播预告信息                                                                         |
| [wx.getChannelsLiveInfo](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/channels/wx.getChannelsLiveInfo.html)             | 获取视频号直播信息                                                                           |

### 音视频通话
| API                                                                                                                         | 功能                    |
| --------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| [wx.requestDeviceVoIP](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/device-voip/wx.requestDeviceVoIP.html) | 请求用户授权与设备（组）间进行音视频通话  |
| [wx.getDeviceVoIPList](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/device-voip/wx.getDeviceVoIPList.html) | 查询当前用户授权的音视频通话设备（组）信息 |
### 微信群
| API                                                                                                                   | 功能                |
| --------------------------------------------------------------------------------------------------------------------- | ----------------- |
| [wx.getGroupEnterInfo](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/group/wx.getGroupEnterInfo.html) | 获取微信群聊场景下的小程序启动信息 |

### 隐私信息授权
| API                                                                                                                                       | 功能                 |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| [wx.requirePrivacyAuthorize](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/privacy/wx.requirePrivacyAuthorize.html)       | 模拟隐私接口调用，并触发隐私弹窗逻辑 |
| [wx.openPrivacyContract](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/privacy/wx.openPrivacyContract.html)               | 跳转至隐私协议页面          |
| [wx.onNeedPrivacyAuthorization](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/privacy/wx.onNeedPrivacyAuthorization.html) | 监听隐私接口需要用户授权事件     |
| [wx.getPrivacySetting](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/privacy/wx.getPrivacySetting.html)                   | 查询隐私授权情况           |
### 微信客服
| API                                                                                                                                      | 功能                   |
| ---------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| [wx.openCustomerServiceChat](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/service-chat/wx.openCustomerServiceChat.html) | 打开微信客服，页面产生点击事件后才可调用 |
### 微信表情
| API                                                                                                                                      | 功能                   |
| ---------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| [wx.openCustomerServiceChat](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/service-chat/wx.openCustomerServiceChat.html) | 打开微信客服，页面产生点击事件后才可调用 |



## 设备

### 蓝牙-通用
| API                                                                                                                                               | 功能                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| [wx.stopBluetoothDevicesDiscovery](https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth/wx.stopBluetoothDevicesDiscovery.html)   | 停止搜寻附近的蓝牙外围设备         |
| [wx.startBluetoothDevicesDiscovery](https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth/wx.startBluetoothDevicesDiscovery.html) | 开始搜寻附近的蓝牙外围设备         |
| [wx.openBluetoothAdapter](https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth/wx.openBluetoothAdapter.html)                     | 初始化蓝牙模块               |
| [wx.onBluetoothDeviceFound](https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth/wx.onBluetoothDeviceFound.html)                 | 监听搜索到新设备的事件           |
| [wx.onBluetoothAdapterStateChange](https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth/wx.onBluetoothAdapterStateChange.html)   | 监听蓝牙适配器状态变化事件         |
| [wx.offBluetoothDeviceFound](https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth/wx.offBluetoothDeviceFound.html)               | 移除搜索到新设备的事件的全部监听函数    |
| [wx.offBluetoothAdapterStateChange](https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth/wx.offBluetoothAdapterStateChange.html) | 移除蓝牙适配器状态变化事件的全部监听函数  |
| [wx.makeBluetoothPair](https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth/wx.makeBluetoothPair.html)                           | 蓝牙配对接口，仅安卓支持          |
| [wx.isBluetoothDevicePaired](https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth/wx.isBluetoothDevicePaired.html)               | 查询蓝牙设备是否配对，仅安卓支持      |
| [wx.getConnectedBluetoothDevices](https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth/wx.getConnectedBluetoothDevices.html)     | 根据主服务 UUID 获取已连接的蓝牙设备 |
| [wx.getBluetoothDevices](https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth/wx.getBluetoothDevices.html)                       | 获取在蓝牙模块生效期间所有搜索到的蓝牙设备 |
| [wx.getBluetoothAdapterState](https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth/wx.getBluetoothAdapterState.html)             | 获取本机蓝牙适配器状态           |
| [wx.closeBluetoothAdapter](https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth/wx.closeBluetoothAdapter.html)                   | 关闭蓝牙模块                |

### 蓝牙-低功耗中心设备
| API                                                                                                                                                           | 功能                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| [wx.writeBLECharacteristicValue](https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-ble/wx.writeBLECharacteristicValue.html)               | 向蓝牙低功耗设备特征值中写入二进制数据                                        |
| [wx.setBLEMTU](https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-ble/wx.setBLEMTU.html)                                                   | 协商设置蓝牙低功耗的最大传输单元 (Maximum Transmission Unit, MTU)          |
| [wx.readBLECharacteristicValue](https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-ble/wx.readBLECharacteristicValue.html)                 | 读取蓝牙低功耗设备特征值的二进制数据                                         |
| [wx.onBLEMTUChange](https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-ble/wx.onBLEMTUChange.html)                                         | 监听蓝牙低功耗的最大传输单元变化事件（仅安卓触发）                                  |
| [wx.onBLEConnectionStateChange](https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-ble/wx.onBLEConnectionStateChange.html)                 | 监听蓝牙低功耗连接状态改变事件                                            |
| [wx.onBLECharacteristicValueChange](https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-ble/wx.onBLECharacteristicValueChange.html)         | 监听蓝牙低功耗设备的特征值变化事件                                          |
| [wx.offBLEMTUChange](https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-ble/wx.offBLEMTUChange.html)                                       | 移除蓝牙低功耗的最大传输单元变化事件的监听函数                                    |
| [wx.offBLEConnectionStateChange](https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-ble/wx.offBLEConnectionStateChange.html)               | 移除蓝牙低功耗连接状态改变事件的监听函数                                       |
| [wx.offBLECharacteristicValueChange](https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-ble/wx.offBLECharacteristicValueChange.html)       | 移除蓝牙低功耗设备的特征值变化事件的全部监听函数                                   |
| [wx.notifyBLECharacteristicValueChange](https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-ble/wx.notifyBLECharacteristicValueChange.html) | 启用蓝牙低功耗设备特征值变化时的 notify 功能，订阅特征                            |
| [wx.getBLEMTU](https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-ble/wx.getBLEMTU.html)                                                   | 获取蓝牙低功耗的最大传输单元                                             |
| [wx.getBLEDeviceServices](https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-ble/wx.getBLEDeviceServices.html)                             | 获取蓝牙低功耗设备所有服务 (service)                                    |
| [wx.getBLEDeviceRSSI](https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-ble/wx.getBLEDeviceRSSI.html)                                     | 获取蓝牙低功耗设备的信号强度 (Received Signal Strength Indication, RSSI) |
| [wx.getBLEDeviceCharacteristics](https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-ble/wx.getBLEDeviceCharacteristics.html)               | 获取蓝牙低功耗设备某个服务中所有特征 (characteristic)                        |
| [wx.createBLEConnection](https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-ble/wx.createBLEConnection.html)                               | 连接蓝牙低功耗设备                                                  |
| [wx.closeBLEConnection](https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-ble/wx.closeBLEConnection.html)                                 | 断开与蓝牙低功耗设备的连接                                              |

### 蓝牙-低功耗外围设备
| API                                                                                                                                                                          | 功能                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| [wx.onBLEPeripheralConnectionStateChanged](https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-peripheral/wx.onBLEPeripheralConnectionStateChanged.html)   | 监听当前外围设备被连接或断开连接事件        |
| [wx.offBLEPeripheralConnectionStateChanged](https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-peripheral/wx.offBLEPeripheralConnectionStateChanged.html) | 移除当前外围设备被连接或断开连接事件的监听函数   |
| [wx.createBLEPeripheralServer](https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-peripheral/wx.createBLEPeripheralServer.html)                           | 建立本地作为蓝牙低功耗外围设备的服务端，可创建多个 |
| [BLEPeripheralServer](https://developers.weixin.qq.com/miniprogram/dev/api/device/bluetooth-peripheral/BLEPeripheralServer.html)                                             | 外围设备的服务端                  |

### 蓝牙-信标（Beacon）
| API                                                                                                                             | 功能                          |
| ------------------------------------------------------------------------------------------------------------------------------- | --------------------------- |
| [wx.stopBeaconDiscovery](https://developers.weixin.qq.com/miniprogram/dev/api/device/ibeacon/wx.stopBeaconDiscovery.html)       | 停止搜索附近的 Beacon 设备           |
| [wx.startBeaconDiscovery](https://developers.weixin.qq.com/miniprogram/dev/api/device/ibeacon/wx.startBeaconDiscovery.html)     | 开始搜索附近的 Beacon 设备           |
| [wx.onBeaconUpdate](https://developers.weixin.qq.com/miniprogram/dev/api/device/ibeacon/wx.onBeaconUpdate.html)                 | 监听 Beacon 设备更新事件，仅能注册一个监听   |
| [wx.onBeaconServiceChange](https://developers.weixin.qq.com/miniprogram/dev/api/device/ibeacon/wx.onBeaconServiceChange.html)   | 监听 Beacon 服务状态变化事件，仅能注册一个监听 |
| [wx.offBeaconUpdate](https://developers.weixin.qq.com/miniprogram/dev/api/device/ibeacon/wx.offBeaconUpdate.html)               | 移除 Beacon 设备更新事件的全部监听函数     |
| [wx.offBeaconServiceChange](https://developers.weixin.qq.com/miniprogram/dev/api/device/ibeacon/wx.offBeaconServiceChange.html) | 移除 Beacon 服务状态变化事件的全部监听函数   |
| [wx.getBeacons](https://developers.weixin.qq.com/miniprogram/dev/api/device/ibeacon/wx.getBeacons.html)                         | 获取所有已搜索到的 Beacon 设备         |
| [BeaconInfo](https://developers.weixin.qq.com/miniprogram/dev/api/device/ibeacon/BeaconInfo.html)                               | Beacon 设备                   |

### NFC读写
| API                                                                                                                                             | 功能                                         |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| [wx.removeSecureElementPass](https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/wx.removeSecureElementPass.html)                   | 删除设备中的某一张卡                                 |
| [wx.getSecureElementPasses](https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/wx.getSecureElementPasses.html)                     | 获取设备中的所有卡信息                                |
| [wx.getNFCAdapter](https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/wx.getNFCAdapter.html)                                       | 获取 NFC 实例                                  |
| [wx.canAddSecureElementPass](https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/wx.canAddSecureElementPass.html)                   | 判断设备是否支持添加该支付卡                             |
| [wx.addPaymentPassGetCertificateData](https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/wx.addPaymentPassGetCertificateData.html) | 拉起ApplePay添加卡流程，从PassKit获取证书、nonce与nonce签名 |
| [wx.addPaymentPassFinish](https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/wx.addPaymentPassFinish.html)                         | 通知客户端开卡成功                                  |
| [IsoDep](https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/IsoDep.html)                                                           | IsoDep 标签                                  |
| [MifareClassic](https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/MifareClassic.html)                                             | MifareClassic 标签                           |
| [MifareUltralight](https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/MifareUltralight.html)                                       | MifareUltralight 标签                        |
| [Ndef](https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/Ndef.html)                                                               | Ndef 标签                                    |
| [NfcA](https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NfcA.html)                                                               | NfcA 标签                                    |


#### NFCAdapter

| API                                                                                                                                   | 功能                                              |
| ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| [NFCAdapter.getIsoDep](https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NFCAdapter.getIsoDep.html)                     | 获取IsoDep实例，实例支持ISO-DEP (ISO 14443-4)标准的读写       |
| [NFCAdapter.getMifareClassic](https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NFCAdapter.getMifareClassic.html)       | 获取MifareClassic实例，实例支持MIFARE Classic标签的读写       |
| [NFCAdapter.getMifareUltralight](https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NFCAdapter.getMifareUltralight.html) | 获取MifareUltralight实例，实例支持MIFARE Ultralight标签的读写 |
| [NFCAdapter.getNdef](https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NFCAdapter.getNdef.html)                         | 获取Ndef实例，实例支持对NDEF格式的NFC标签上的NDEF数据的读写           |
| [NFCAdapter.getNfcA](https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NFCAdapter.getNfcA.html)                         | 获取NfcA实例，实例支持NFC-A (ISO 14443-3A)标准的读写          |
| [NFCAdapter.getNfcB](https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NFCAdapter.getNfcB.html)                         | 获取NfcB实例，实例支持NFC-B (ISO 14443-3B)标准的读写          |
| [NFCAdapter.getNfcF](https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NFCAdapter.getNfcF.html)                         | 获取NfcF实例，实例支持NFC-F (JIS 6319-4)标准的读写            |
| [NFCAdapter.getNfcV](https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NFCAdapter.getNfcV.html)                         | 获取NfcV实例，实例支持NFC-V (ISO 15693)标准的读写             |
| [NFCAdapter.offDiscovered](https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NFCAdapter.offDiscovered.html)             | 移除 NFC Tag的监听函数                                 |
| [NFCAdapter.onDiscovered](https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NFCAdapter.onDiscovered.html)               | 监听 NFC Tag                                      |
| [NFCAdapter.startDiscovery](https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NFCAdapter.startDiscovery.html)           |                                                 |
| [NFCAdapter.stopDiscovery](https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NFCAdapter.stopDiscovery.html)             |                                                 |
| [NfcB](https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NfcB.html)                                                     | NfcB 标签                                         |
| [NfcF](https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NfcF.html)                                                     | NfcF 标签                                         |
| [NfcV](https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc/NfcV.html)                                                     | NfcV 标签                                         |
### WIFI
| API                                                                                                                                            | 功能                       |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| [wx.stopWifi](https://developers.weixin.qq.com/miniprogram/dev/api/device/wifi/wx.stopWifi.html)                                               | 关闭 Wi-Fi 模块              |
| [wx.startWifi](https://developers.weixin.qq.com/miniprogram/dev/api/device/wifi/wx.startWifi.html)                                             | 初始化 Wi-Fi 模块             |
| [wx.setWifiList](https://developers.weixin.qq.com/miniprogram/dev/api/device/wifi/wx.setWifiList.html)                                         | 设置 `wifiList` 中 AP 的相关信息 |
| [wx.onWifiConnectedWithPartialInfo](https://developers.weixin.qq.com/miniprogram/dev/api/device/wifi/wx.onWifiConnectedWithPartialInfo.html)   | 监听连接上 Wi-Fi 的事件          |
| [wx.onWifiConnected](https://developers.weixin.qq.com/miniprogram/dev/api/device/wifi/wx.onWifiConnected.html)                                 | 监听连接上 Wi-Fi 的事件          |
| [wx.onGetWifiList](https://developers.weixin.qq.com/miniprogram/dev/api/device/wifi/wx.onGetWifiList.html)                                     | 监听获取到 Wi-Fi 列表数据事件       |
| [wx.offWifiConnectedWithPartialInfo](https://developers.weixin.qq.com/miniprogram/dev/api/device/wifi/wx.offWifiConnectedWithPartialInfo.html) | 移除连接上 Wi-Fi 的事件的监听函数     |
| [wx.offWifiConnected](https://developers.weixin.qq.com/miniprogram/dev/api/device/wifi/wx.offWifiConnected.html)                               | 移除连接上 Wi-Fi 的事件的监听函数     |
| [wx.offGetWifiList](https://developers.weixin.qq.com/miniprogram/dev/api/device/wifi/wx.offGetWifiList.html)                                   | 移除获取到 Wi-Fi 列表数据事件的监听函数  |
| [wx.getWifiList](https://developers.weixin.qq.com/miniprogram/dev/api/device/wifi/wx.getWifiList.html)                                         | 请求获取 Wi-Fi 列表            |
| [wx.getConnectedWifi](https://developers.weixin.qq.com/miniprogram/dev/api/device/wifi/wx.getConnectedWifi.html)                               | 获取已连接中的 Wi-Fi 信息         |
| [wx.connectWifi](https://developers.weixin.qq.com/miniprogram/dev/api/device/wifi/wx.connectWifi.html)                                         | 连接 Wi-Fi                 |
| [WifiInfo](https://developers.weixin.qq.com/miniprogram/dev/api/device/wifi/WifiInfo.html)                                                     | Wifi 信息                  |

### 日历
| API                                                                                                                              | 功能          |
| -------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [wx.addPhoneRepeatCalendar](https://developers.weixin.qq.com/miniprogram/dev/api/device/calendar/wx.addPhoneRepeatCalendar.html) | 向系统日历添加重复事件 |
| [wx.addPhoneCalendar](https://developers.weixin.qq.com/miniprogram/dev/api/device/calendar/wx.addPhoneCalendar.html)             | 向系统日历添加事件   |
### 联系人
| API                                                                                                               | 功能            |
| ----------------------------------------------------------------------------------------------------------------- | ------------- |
| [wx.chooseContact](https://developers.weixin.qq.com/miniprogram/dev/api/device/contact/wx.chooseContact.html)     | 拉起手机通讯录，选择联系人 |
| [wx.addPhoneContact](https://developers.weixin.qq.com/miniprogram/dev/api/device/contact/wx.addPhoneContact.html) | 添加手机通讯录联系人    |
### 无障碍
| API                                                                                                                                       | 功能            |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| [wx.checkIsOpenAccessibility](https://developers.weixin.qq.com/miniprogram/dev/api/device/accessibility/wx.checkIsOpenAccessibility.html) | 检测是否开启视觉无障碍功能 |
### 电量
| API                                                                                                                         | 功能                                                                                                                    |
| --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| [wx.onBatteryInfoChange](https://developers.weixin.qq.com/miniprogram/dev/api/device/battery/wx.onBatteryInfoChange.html)   | 监听电池信息变化事件，目前只支持监听省电模式的切换                                                                                             |
| [wx.offBatteryInfoChange](https://developers.weixin.qq.com/miniprogram/dev/api/device/battery/wx.offBatteryInfoChange.html) | 移除电池信息变化事件的监听函数                                                                                                       |
| [wx.getBatteryInfoSync](https://developers.weixin.qq.com/miniprogram/dev/api/device/battery/wx.getBatteryInfoSync.html)     | [wx.getBatteryInfo](https://developers.weixin.qq.com/miniprogram/dev/api/device/battery/wx.getBatteryInfo.html) 的同步版本 |
| [wx.getBatteryInfo](https://developers.weixin.qq.com/miniprogram/dev/api/device/battery/wx.getBatteryInfo.html)             | 获取设备电池信息                                                                                                              |
### 剪贴板
| API                                                                                                                   | 功能         |
| --------------------------------------------------------------------------------------------------------------------- | ---------- |
| [wx.setClipboardData](https://developers.weixin.qq.com/miniprogram/dev/api/device/clipboard/wx.setClipboardData.html) | 设置系统剪贴板的内容 |
| [wx.getClipboardData](https://developers.weixin.qq.com/miniprogram/dev/api/device/clipboard/wx.getClipboardData.html) | 获取系统剪贴板的内容 |
### NFC主机卡模拟
| API                                                                                                             | 功能                   |
| --------------------------------------------------------------------------------------------------------------- | -------------------- |
| [wx.stopHCE](https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc-hce/wx.stopHCE.html)               | 关闭 NFC 模块            |
| [wx.startHCE](https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc-hce/wx.startHCE.html)             | 初始化 NFC 模块           |
| [wx.sendHCEMessage](https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc-hce/wx.sendHCEMessage.html) | 发送 NFC 消息            |
| [wx.onHCEMessage](https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc-hce/wx.onHCEMessage.html)     | 监听接收 NFC 设备消息事件      |
| [wx.offHCEMessage](https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc-hce/wx.offHCEMessage.html)   | 移除接收 NFC 设备消息事件的监听函数 |
| [wx.getHCEState](https://developers.weixin.qq.com/miniprogram/dev/api/device/nfc-hce/wx.getHCEState.html)       | 判断当前设备是否支持 HCE 能力    |

### 网络
| API                                                                                                                             | 功能              |
| ------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| [wx.onNetworkWeakChange](https://developers.weixin.qq.com/miniprogram/dev/api/device/network/wx.onNetworkWeakChange.html)       | 监听弱网状态变化事件      |
| [wx.onNetworkStatusChange](https://developers.weixin.qq.com/miniprogram/dev/api/device/network/wx.onNetworkStatusChange.html)   | 监听网络状态变化事件      |
| [wx.offNetworkWeakChange](https://developers.weixin.qq.com/miniprogram/dev/api/device/network/wx.offNetworkWeakChange.html)     | 移除弱网状态变化事件的监听函数 |
| [wx.offNetworkStatusChange](https://developers.weixin.qq.com/miniprogram/dev/api/device/network/wx.offNetworkStatusChange.html) | 移除网络状态变化事件的监听函数 |
| [wx.getNetworkType](https://developers.weixin.qq.com/miniprogram/dev/api/device/network/wx.getNetworkType.html)                 | 获取网络类型          |
| [wx.getLocalIPAddress](https://developers.weixin.qq.com/miniprogram/dev/api/device/network/wx.getLocalIPAddress.html)           | 获取局域网IP地址       |
### 加密
| API                                                                                                              | 功能         |
| ---------------------------------------------------------------------------------------------------------------- | ---------- |
| [wx.getRandomValues](https://developers.weixin.qq.com/miniprogram/dev/api/device/crypto/wx.getRandomValues.html) | 获取密码学安全随机数 |
### 屏幕
| API                                                                                                                                            | 功能                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| [wx.setVisualEffectOnCapture](https://developers.weixin.qq.com/miniprogram/dev/api/device/screen/wx.setVisualEffectOnCapture.html)             | 设置截屏/录屏时屏幕表现                        |
| [wx.setScreenBrightness](https://developers.weixin.qq.com/miniprogram/dev/api/device/screen/wx.setScreenBrightness.html)                       | 设置屏幕亮度                              |
| [wx.setKeepScreenOn](https://developers.weixin.qq.com/miniprogram/dev/api/device/screen/wx.setKeepScreenOn.html)                               | 设置是否保持常亮状态                          |
| [wx.onUserCaptureScreen](https://developers.weixin.qq.com/miniprogram/dev/api/device/screen/wx.onUserCaptureScreen.html)                       | 监听用户主动截屏事件                          |
| [wx.onScreenRecordingStateChanged](https://developers.weixin.qq.com/miniprogram/dev/api/device/screen/wx.onScreenRecordingStateChanged.html)   | 监听用户录屏事件                            |
| [wx.onGeneratePoster](https://developers.weixin.qq.com/miniprogram/dev/api/device/screen/wx.onGeneratePoster.html)                             | 监听用户截屏之后需要开发者生成自定义海报事件，在点击转发截图按钮时触发 |
| [wx.offUserCaptureScreen](https://developers.weixin.qq.com/miniprogram/dev/api/device/screen/wx.offUserCaptureScreen.html)                     | 用户主动截屏事件                            |
| [wx.offScreenRecordingStateChanged](https://developers.weixin.qq.com/miniprogram/dev/api/device/screen/wx.offScreenRecordingStateChanged.html) | 移除用户录屏事件的监听函数                       |
| [wx.offGeneratePoster](https://developers.weixin.qq.com/miniprogram/dev/api/device/screen/wx.offGeneratePoster.html)                           | 用户截屏之后需要开发者生成自定义海报事件                |
| [wx.getScreenRecordingState](https://developers.weixin.qq.com/miniprogram/dev/api/device/screen/wx.getScreenRecordingState.html)               | 查询用户是否在录屏                           |
| [wx.getScreenBrightness](https://developers.weixin.qq.com/miniprogram/dev/api/device/screen/wx.getScreenBrightness.html)                       | 获取屏幕亮度                              |
### 键盘
| API                                                                                                                                | 功能                                      |
| ---------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| [wx.onKeyUp](https://developers.weixin.qq.com/miniprogram/dev/api/device/keyboard/wx.onKeyUp.html)                                 | 监听小程序全局键盘按键弹起事件                         |
| [wx.onKeyDown](https://developers.weixin.qq.com/miniprogram/dev/api/device/keyboard/wx.onKeyDown.html)                             | 监听小程序全局键盘按键按下事件                         |
| [wx.onKeyboardHeightChange](https://developers.weixin.qq.com/miniprogram/dev/api/device/keyboard/wx.onKeyboardHeightChange.html)   | 监听键盘高度变化事件                              |
| [wx.offKeyUp](https://developers.weixin.qq.com/miniprogram/dev/api/device/keyboard/wx.offKeyUp.html)                               | 移除小程序全局键盘按键弹起事件的监听函数                    |
| [wx.offKeyDown](https://developers.weixin.qq.com/miniprogram/dev/api/device/keyboard/wx.offKeyDown.html)                           | 移除小程序全局键盘按键按下事件的监听函数                    |
| [wx.offKeyboardHeightChange](https://developers.weixin.qq.com/miniprogram/dev/api/device/keyboard/wx.offKeyboardHeightChange.html) | 移除键盘高度变化事件的监听函数                         |
| [wx.hideKeyboard](https://developers.weixin.qq.com/miniprogram/dev/api/device/keyboard/wx.hideKeyboard.html)                       | 在input、textarea等focus拉起键盘之后，手动调用此接口收起键盘 |
| [wx.getSelectedTextRange](https://developers.weixin.qq.com/miniprogram/dev/api/device/keyboard/wx.getSelectedTextRange.html)       | 在input、textarea等focus之后，获取输入框的光标位置      |
### 电话
| API                                                                                                         | 功能   |
| ----------------------------------------------------------------------------------------------------------- | ---- |
| [wx.makePhoneCall](https://developers.weixin.qq.com/miniprogram/dev/api/device/phone/wx.makePhoneCall.html) | 拨打电话 |
### 加速计
| API                                                                                                                                   | 功能             |
| ------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| [wx.stopAccelerometer](https://developers.weixin.qq.com/miniprogram/dev/api/device/accelerometer/wx.stopAccelerometer.html)           | 停止监听加速度数据      |
| [wx.startAccelerometer](https://developers.weixin.qq.com/miniprogram/dev/api/device/accelerometer/wx.startAccelerometer.html)         | 开始监听加速度数据      |
| [wx.onAccelerometerChange](https://developers.weixin.qq.com/miniprogram/dev/api/device/accelerometer/wx.onAccelerometerChange.html)   | 监听加速度数据事件      |
| [wx.offAccelerometerChange](https://developers.weixin.qq.com/miniprogram/dev/api/device/accelerometer/wx.offAccelerometerChange.html) | 移除加速度数据事件的监听函数 |
### 罗盘
| API                                                                                                                 | 功能              |
| ------------------------------------------------------------------------------------------------------------------- | --------------- |
| [wx.stopCompass](https://developers.weixin.qq.com/miniprogram/dev/api/device/compass/wx.stopCompass.html)           | 停止监听罗盘数据        |
| [wx.startCompass](https://developers.weixin.qq.com/miniprogram/dev/api/device/compass/wx.startCompass.html)         | 开始监听罗盘数据        |
| [wx.onCompassChange](https://developers.weixin.qq.com/miniprogram/dev/api/device/compass/wx.onCompassChange.html)   | 监听罗盘数据变化事件      |
| [wx.offCompassChange](https://developers.weixin.qq.com/miniprogram/dev/api/device/compass/wx.offCompassChange.html) | 移除罗盘数据变化事件的监听函数 |
### 设备方向
| API                                                                                                                                    | 功能              |
| -------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| [wx.stopDeviceMotionListening](https://developers.weixin.qq.com/miniprogram/dev/api/device/motion/wx.stopDeviceMotionListening.html)   | 停止监听设备方向的变化     |
| [wx.startDeviceMotionListening](https://developers.weixin.qq.com/miniprogram/dev/api/device/motion/wx.startDeviceMotionListening.html) | 开始监听设备方向的变化     |
| [wx.onDeviceMotionChange](https://developers.weixin.qq.com/miniprogram/dev/api/device/motion/wx.onDeviceMotionChange.html)             | 监听设备方向变化事件      |
| [wx.offDeviceMotionChange](https://developers.weixin.qq.com/miniprogram/dev/api/device/motion/wx.offDeviceMotionChange.html)           | 移除设备方向变化事件的监听函数 |
### 陀螺仪
| API                                                                                                                       | 功能               |
| ------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| [wx.stopGyroscope](https://developers.weixin.qq.com/miniprogram/dev/api/device/gyroscope/wx.stopGyroscope.html)           | 停止监听陀螺仪数据        |
| [wx.startGyroscope](https://developers.weixin.qq.com/miniprogram/dev/api/device/gyroscope/wx.startGyroscope.html)         | 开始监听陀螺仪数据        |
| [wx.onGyroscopeChange](https://developers.weixin.qq.com/miniprogram/dev/api/device/gyroscope/wx.onGyroscopeChange.html)   | 监听陀螺仪数据变化事件      |
| [wx.offGyroscopeChange](https://developers.weixin.qq.com/miniprogram/dev/api/device/gyroscope/wx.offGyroscopeChange.html) | 移除陀螺仪数据变化事件的监听函数 |

### 内存
| API                                                                                                                | 功能              |
| ------------------------------------------------------------------------------------------------------------------ | --------------- |
| [wx.onMemoryWarning](https://developers.weixin.qq.com/miniprogram/dev/api/device/memory/wx.onMemoryWarning.html)   | 监听内存不足告警事件      |
| [wx.offMemoryWarning](https://developers.weixin.qq.com/miniprogram/dev/api/device/memory/wx.offMemoryWarning.html) | 移除内存不足告警事件的监听函数 |
### 扫码
| API                                                                                              | 功能            |
| ------------------------------------------------------------------------------------------------ | ------------- |
| [wx.scanCode](https://developers.weixin.qq.com/miniprogram/dev/api/device/scan/wx.scanCode.html) | 调起客户端扫码界面进行扫码 |
### 短信
| API                                                                                           | 功能         |
| --------------------------------------------------------------------------------------------- | ---------- |
| [wx.sendSms](https://developers.weixin.qq.com/miniprogram/dev/api/device/sms/wx.sendSms.html) | 拉起手机发送短信界面 |
### 振动
| API                                                                                                         | 功能                   |
| ----------------------------------------------------------------------------------------------------------- | -------------------- |
| [wx.vibrateShort](https://developers.weixin.qq.com/miniprogram/dev/api/device/vibrate/wx.vibrateShort.html) | 使手机发生较短时间的振动（15 ms）  |
| [wx.vibrateLong](https://developers.weixin.qq.com/miniprogram/dev/api/device/vibrate/wx.vibrateLong.html)   | 使手机发生较长时间的振动（400 ms) |

## AI

### AI推理
| API                                                                                                                           | 功能                                                                                                                                                    |
| ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| [wx.getInferenceEnvInfo](https://developers.weixin.qq.com/miniprogram/dev/api/ai/inference/wx.getInferenceEnvInfo.html)       | 获取通用AI推理引擎版本                                                                                                                                          |
| [wx.createInferenceSession](https://developers.weixin.qq.com/miniprogram/dev/api/ai/inference/wx.createInferenceSession.html) | 创建 AI 推理 Session                                                                                                                                      |
| [InferenceSession](https://developers.weixin.qq.com/miniprogram/dev/api/ai/inference/InferenceSession.html)                   | 推理 Session 实例，通过[wx.createInferenceSession](https://developers.weixin.qq.com/miniprogram/dev/api/ai/inference/wx.createInferenceSession.html) 接口获取该实例 |
| [Tensor](https://developers.weixin.qq.com/miniprogram/dev/api/ai/inference/Tensor.html)                                       | Tensor                                                                                                                                                |
| [Tensors](https://developers.weixin.qq.com/miniprogram/dev/api/ai/inference/Tensors.html)                                     | Tensors 是 key-value 形式的对象，对象的 key 会作为 input/output name，对象的 value 则是 Tensor                                                                           |

### 视觉算法

| API                                                                                                             | 功能                   |
| --------------------------------------------------------------------------------------------------------------- | -------------------- |
| [wx.isVKSupport](https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/wx.isVKSupport.html)         | 判断支持版本               |
| [wx.createVKSession](https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/wx.createVKSession.html) | 创建 vision kit 会话对象   |
| [VKBodyAnchor](https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKBodyAnchor.html)             | 人体 anchor            |
| [VKCamera](https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKCamera.html)                     | 相机对象                 |
| [VKDepthAnchor](https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKDepthAnchor.html)           | depth anchor         |
| [VKFaceAnchor](https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKFaceAnchor.html)             | 人脸 anchor            |
| [VKFrame](https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKFrame.html)                       | vision kit 会话对象      |
| [VKHandAnchor](https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKHandAnchor.html)             | 手势 anchor            |
| [VKMarkerAnchor](https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKMarkerAnchor.html)         | marker anchor        |
| [VKOCRAnchor](https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKOCRAnchor.html)               | OCR anchor           |
| [VKOSDAnchor](https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKOSDAnchor.html)               | OSD anchor           |
| [VKPlaneAnchor](https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKPlaneAnchor.html)           | 平面 anchor，只有 v2 版本支持 |
| [VKSession](https://developers.weixin.qq.com/miniprogram/dev/api/ai/visionkit/VKSession.html)                   | vision kit 会话对象      |
### 人脸检测
| API                                                                                                      | 功能                                                    |
| -------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| [wx.stopFaceDetect](https://developers.weixin.qq.com/miniprogram/dev/api/ai/face/wx.stopFaceDetect.html) | 停止人脸检测                                                |
| [wx.initFaceDetect](https://developers.weixin.qq.com/miniprogram/dev/api/ai/face/wx.initFaceDetect.html) | 初始化人脸检测                                               |
| [wx.faceDetect](https://developers.weixin.qq.com/miniprogram/dev/api/ai/face/wx.faceDetect.html)         | 人脸检测，使用前需要通过 wx.initFaceDetect 进行一次初始化，推荐使用相机接口返回的帧数据 |
## Worker

| API                                                                                                 | 功能                                                                                                                                                       |
| --------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [wx.createWorker](https://developers.weixin.qq.com/miniprogram/dev/api/worker/wx.createWorker.html) | 创建一个 Worker 线程                                                                                                                                           |
| [Worker](https://developers.weixin.qq.com/miniprogram/dev/api/worker/Worker.html)                   | Worker 实例，主线程中可通过 [wx.createWorker](https://developers.weixin.qq.com/miniprogram/dev/api/worker/wx.createWorker.html) 接口获取，worker 线程中可通过全局变量 `worker` 获取 |


## WXML

| API                                                                                                                           | 功能                                                                |
| ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| [wx.createSelectorQuery](https://developers.weixin.qq.com/miniprogram/dev/api/wxml/wx.createSelectorQuery.html)               | 返回一个 SelectorQuery 对象实例                                           |
| [wx.createIntersectionObserver](https://developers.weixin.qq.com/miniprogram/dev/api/wxml/wx.createIntersectionObserver.html) | 创建并返回一个 IntersectionObserver 对象实例                                 |
| [IntersectionObserver](https://developers.weixin.qq.com/miniprogram/dev/api/wxml/IntersectionObserver.html)                   | IntersectionObserver 对象，用于推断某些节点是否可以被用户看见、有多大比例可以被用户看见            |
| [MediaQueryObserver](https://developers.weixin.qq.com/miniprogram/dev/api/wxml/MediaQueryObserver.html)                       | MediaQueryObserver 对象，用于监听页面 media query 状态的变化，如界面的长宽是不是在某个指定的范围内 |
| [NodesRef](https://developers.weixin.qq.com/miniprogram/dev/api/wxml/NodesRef.html)                                           | 用于获取 WXML 节点信息的对象                                                 |
| [SelectorQuery](https://developers.weixin.qq.com/miniprogram/dev/api/wxml/SelectorQuery.html)                                 | 查询节点信息的对象                                                         |

## 第三方平台



| API                                                                                                      | 功能                                                                                                     |
| -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| [wx.getExtConfigSync](https://developers.weixin.qq.com/miniprogram/dev/api/ext/wx.getExtConfigSync.html) | [wx.getExtConfig](https://developers.weixin.qq.com/miniprogram/dev/api/ext/wx.getExtConfig.html) 的同步版本 |
| [wx.getExtConfig](https://developers.weixin.qq.com/miniprogram/dev/api/ext/wx.getExtConfig.html)         | 获取[第三方平台](https://developers.weixin.qq.com/miniprogram/dev/devtools/ext.html)自定义的数据字段                  |



## 广告

| API                                                                                                               | 功能           |
| ----------------------------------------------------------------------------------------------------------------- | ------------ |
| [wx.getShowSplashAdStatus](https://developers.weixin.qq.com/miniprogram/dev/api/ad/wx.getShowSplashAdStatus.html) | 获取封面广告组件展示状态 |
| [wx.createRewardedVideoAd](https://developers.weixin.qq.com/miniprogram/dev/api/ad/wx.createRewardedVideoAd.html) | 创建激励视频广告组件   |
| [wx.createInterstitialAd](https://developers.weixin.qq.com/miniprogram/dev/api/ad/wx.createInterstitialAd.html)   | 创建插屏广告组件     |
| [InterstitialAd](https://developers.weixin.qq.com/miniprogram/dev/api/ad/InterstitialAd.html)                     | 插屏广告组件       |
| [RewardedVideoAd](https://developers.weixin.qq.com/miniprogram/dev/api/ad/RewardedVideoAd.html)                   | 激励视频广告组件     |




## Skyline

| API                                                                                                              | 功能                                                                                                                                                                                                                                         |
| ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [DraggableSheetContext](https://developers.weixin.qq.com/miniprogram/dev/api/skyline/DraggableSheetContext.html) | DraggableSheet 实例，可通过 [wx.createSelectorQuery](https://developers.weixin.qq.com/miniprogram/dev/api/wxml/wx.createSelectorQuery.html) 的 [NodesRef.node](https://developers.weixin.qq.com/miniprogram/dev/api/wxml/NodesRef.node.html) 方法获取 |
| [OpenContainer](https://developers.weixin.qq.com/miniprogram/dev/api/skyline/OpenContainer.html)                 | OpenContainer 实例，可通过 [SelectorQuery](https://developers.weixin.qq.com/miniprogram/dev/api/wxml/SelectorQuery.html) 获取                                                                                                                      |
| [Snapshot](https://developers.weixin.qq.com/miniprogram/dev/api/skyline/Snapshot.html)                           | Snapshot 实例，可通过 [SelectorQuery](https://developers.weixin.qq.com/miniprogram/dev/api/wxml/SelectorQuery.html) 获取                                                                                                                           |
