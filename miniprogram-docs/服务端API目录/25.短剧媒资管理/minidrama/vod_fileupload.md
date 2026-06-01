# 媒资上传

> 官方文档：[媒资上传](https://developers.weixin.qq.com/miniprogram/dev/server/API/minidrama/vod_fileupload)
> 所属分类：[短剧媒资管理](../短剧媒资管理目录.md)
> 导航路径：短剧媒资管理 / 媒资上传
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

上传时需要注意以下事项：

1. 首次上传要初始化资源，需要一定时间，在初始化期间上传都会返回失败（错误码为 -2），等待一段时间（一般为几分钟）后重试即可。
2. 需按照“剧目名 - 对应剧集数”格式命名文件（如：“我的演艺 - 第1集”）。
3. 视频格式支持：MP4，TS，MOV，MXF，MPG，FLV，WMV，AVI，M4V，F4V，MPEG，3GP，ASF，MKV。如需上传 m3u8 视频，请使用"[拉取上传](https://developers.weixin.qq.com/miniprogram/dev/server/API/minidrama/api_pullupload)"接口。
4. 图片格式支持：JPG、JPEG、PNG、BMP、TIFF、AI、CDR、EPS、TIF。
5. 如果接口返回 HTTP 状态码 502，请检查上传的文件是否超过了特定接口所限制的大小。
