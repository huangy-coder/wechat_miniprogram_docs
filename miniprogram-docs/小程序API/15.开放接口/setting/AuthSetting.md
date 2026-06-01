# AuthSetting

> 官方文档：[AuthSetting](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/setting/AuthSetting.html)
> 所属分类：[开放接口](../开放接口目录.md)
> 导航路径：开放接口 / 设置 / AuthSetting
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

用户授权设置信息，详情参考[权限](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/authorize.html)

## 属性

### boolean scope.userInfo

是否授权用户信息，对应接口 [wx.getUserInfo](../user-info/wx.getUserInfo.md)

### boolean scope.userLocation

是否授权精确地理位置，对应接口 [wx.getLocation](../../13.位置/wx.getLocation.md), [wx.chooseLocation](../../13.位置/wx.chooseLocation.md)

### boolean scope.userFuzzyLocation

是否授权模糊地理位置，对应接口 [wx.getFuzzyLocation](../../13.位置/wx.getFuzzyLocation.md)

### boolean scope.address

是否授权通讯地址，已取消此项授权，会默认返回true

### boolean scope.invoiceTitle

是否授权发票抬头，已取消此项授权，会默认返回true

### boolean scope.invoice

是否授权获取发票，已取消此项授权，会默认返回true

### boolean scope.werun

是否授权微信运动步数，对应接口 [wx.getWeRunData](../werun/wx.getWeRunData.md)

### boolean scope.record

是否授权录音功能，对应接口 [wx.getRecorderManager](../../12.媒体/recorder/wx.getRecorderManager.md)

### boolean scope.writePhotosAlbum

是否授权保存到相册 [wx.saveImageToPhotosAlbum](../../12.媒体/image/wx.saveImageToPhotosAlbum.md), [wx.saveVideoToPhotosAlbum](../../12.媒体/video/wx.saveVideoToPhotosAlbum.md)

### boolean scope.camera

是否授权摄像头，对应[[camera](https://developers.weixin.qq.com/miniprogram/dev/component/camera.html)]((camera)) 组件

### boolean scope.bluetooth

是否授权蓝牙，对应接口 [wx.openBluetoothAdapter](../../16.设备/bluetooth/wx.openBluetoothAdapter.md)、[wx.createBLEPeripheralServer](../../16.设备/bluetooth-peripheral/wx.createBLEPeripheralServer.md)

### boolean scope.addPhoneContact

是否添加通讯录联系人，对应接口 [wx.addPhoneContact](../../16.设备/contact/wx.addPhoneContact.md)

### boolean scope.addPhoneCalendar

是否授权系统日历，对应接口 [wx.addPhoneRepeatCalendar](../../16.设备/calendar/wx.addPhoneRepeatCalendar.md)、[wx.addPhoneCalendar](../../16.设备/calendar/wx.addPhoneCalendar.md)
