# 服务端 API 签名加密指南

> 官方文档：[服务端 API 签名加密指南](https://developers.weixin.qq.com/miniprogram/dev/server/getting_started/api_signature.html)
> 所属分类：[开发前必读](开发前必读目录.md)
> 导航路径：开发前必读
> 整理日期：2026-06-01
> 本地化说明：正文按官方服务端页面结构转换为 Markdown，保留接口说明、调用方式、请求参数、返回值、错误码、注意事项和示例等开发信息。

微信开放平台的接口通信鉴权体系，使用了数据加密与签名的机制，防止数据泄漏与篡改，且具备不可否认性。开发者可在[小程序管理后台](https://mp.weixin.qq.com) API安全模块，为应用配置密钥与公钥，以此来保障开发者应用和微信开放平台交互的安全性。

## 一、概念解释

### 1.1 服务签名与验签

在请求API的过程中，为了保护数据的安全，开发者在应用中使用自己的私钥生成请求的签名（签名算法支持RSA及SM2），平台会在收到请求后使用应用的公钥进行签名的验证，开发者则使用平台证书中的公钥验证回调的签名，来保证互相请求的真实性和数据的完整性。

名词解释：

- **应用公钥：** 公钥是指应用公钥，开发者通过平台工具生成公钥信息，并保存在API安全配置中，用于平台进行接口调用时的验签。
- **应用私钥：** 私钥是指应用私钥，开发者可以通过平台工具生成私钥信息，用于生成请求的签名，请妥善保管好私钥文件，务必自行保障其安全性。
- **平台证书：** 平台证书是指包含微信开放平台公钥信息的证书，用于开发者验证API回包的平台签名。开发者可在配置应用公钥后在API安全模块下载。


### 1.2 接口内容加密

平台支持对接口的请求内容和响应内容进行 AES256/SM4 加密（资源上传类API暂不支持加密），加密后，在网络上传输的接口报文内容将会由明文内容变为密文内容，可以大幅提升接口内容传输的安全性。
接口数据加密与签名，可以在接口数据泄露的情况下，确保接口内容保密且不被篡改。 开发者应先加密请求数据，然后对密文签名。

## 二、 密钥配置

开发者可根据以下指引，快速完成密钥生成、配置及平台证书获取。

### 2.1 进入配置页

开发者登录[小程序管理后台](https://mp.weixin.qq.com)，可在“开发 - 开发管理 - 开发设置 - API安全”进行API密钥的配置。


点击「开始配置」后，需使用管理员微信扫码验证身份，通过后进入配置页面。


### 2.2 配置接口内容加密密钥

可在API对称密钥处进行配置，点击“随机生成密钥”后，再点击“下载密钥”进行密钥下载（如开发者已准备好密钥，可直接将已准备好的密钥填充进输入框），验证无误后点击“确认”，即可完成对称密钥的配置。


### 2.3 配置应用私钥和公钥

可在API非对称密钥处进行配置，点击“随机生成密钥对”后，再点击“下载私钥”进行私钥下载，请妥善进行保管（如开发者已准备好密钥对，可直接将已准备好的应用公钥填充进输入框），验证无误后点击“确认”，即可完成应用公钥的上传。


### 2.4 获取平台证书

开发者配置完应用公钥后，需下载开放平台证书，用于后续接口回调时的验签操作。在此页面，也可查看对应的API密钥及密钥编号。


在小程序管理后台开启api加密后，开发者需要对原API的请求内容`加密`与`签名`，同时API的回包内容需要开发者`验签`与`解密`。**只有部分 API 支持加解密，具体可参考各 API 文档。**

目前支持以下几种算法，可在MP管理页配置。

**加密算法**：`AES256_GCM`、`SM4_GCM`

**签名算法**：`RSAwithSHA256`、`SM2withSM3`

## 三、API 请求处理

### 3.1 加密请求

#### 3.1.1 参数说明

##### 请求参数

| 参数 | 类型 | 默认值 | 必填 | 备注 |
| --- | --- | --- | --- | --- |
| iv | string |   | 是 | 初始向量，为16字节base64字符串（解码后为12字节随机字符串） |
| data | string |   | 是 | 加密后的密文，使用base64编码 |
| authtag | string |   | 是 | GCM模式输出的认证信息，使用base64编码 |

##### GCM使用的认证数据

GCM分组模式需要设置`额外认证数据（AAD）`对密文进行认证。平台统一使用 `urlpath|appid|timestamp|sn` 格式，字段之间使用竖线符号`|`分隔。

| 参数 | 说明 |
| --- | --- |
| urlpath | 当前请求API的URL路径，包含URL协议信息，不包括URL参数（URL Query） |
| appid | 当前小程序的Appid |
| timestamp | 加密时的时间戳，需要与HTTP请求头`Wechatmp-TimeStamp`的时间戳一致 |
| sn | 使用的对称密钥编号，需要在MP平台密钥管理页面获取 |

##### data明文格式

data明文使用JSON格式，包含原API使用的URL参数与POST参数。需要额外增加三个安全字段_n，_appid，_timestamp，这些字段首字符均为下划线，与参数字段相互独立。

| 参数 | 类型 | 默认值 | 必填 | 备注 |
| --- | --- | --- | --- | --- |
| data | 原字段类型 |   | 是 | 原请求字段，包含URL参数、POST参数，不包含AccessToken |
| _n | string |   | 是 | 随机字符串，推荐使用16-32字节非固定长度随机base64字符串 |
| _appid | string |   | 是 | 当前小程序的Appid |
| _timestamp | number |   | 是 | 加密时的时间戳，需要与HTTP请求头`Wechatmp-TimeStamp`的时间戳一致 |

#### 3.1.2 计算示例

以[风控接口为例](https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/safety-control-capability/riskControl.getUserRiskRank.html)， 对原请求数据加密。

##### AES256_GCM

密钥信息

```json
{
    "Sn": "fa05fe1e5bcc79b81ad5ad4b58acf787",
    "Key": "otUpngOjU+nVQaWJIC3D/yMLV17RKaP6t4Ot9tbnzLY="
}
```

原始数据

```json
{
    "appid": "wxba6223c06417af7b",
    "openid": "oEWzBfmdLqhFS2mTXCo2E4Y9gJAM",
    "scene": 0,
    "client_ip": "127.0.0.1",
}
```

加密后请求

```json
{
    "iv": "fmW/zNxXlytUZBgj",
    "data": "0IDVdrPtSPF/Oe2CTXCV2vVNPbVJdJlP2WaTMQnoYLh5iCrrSNfQFh25EnStDMf0hLlVNBCZQtf9NaV0m4aRA4AAYIO7oR/Ge+4yY4EmZp5EVPB42xjScgMx5X3D4VdLCfynXIUKUtZHZvk1zmLVE3RauzJgiM1BB1CPmwcENo3MTJ0z8Vfkf5tMv54kOXobDLlV5rfqKdAX7gM/rP82DgZdt9vvZX44ipdbHIjJvw83ZXAFtvftdVw2Qd8=",
    "authtag": "5qeM/2vZv+6KtScN94IpMg=="
}
```

##### 加密过程数据

生成12字节随机字符串`iv`

```text
base64_encode(iv) = fmW/zNxXlytUZBgj
```

拼接额外认证数据`aad`

```text
aad = https://api.weixin.qq.com/wxa/getuserriskrank|wxba6223c06417af7b|1635927954|fa05fe1e5bcc79b81ad5ad4b58acf787
```

在原数据内添加安全字段，组成`data`

```json
{
    "_n": "o89QaPVsRu1yppIZzvSZc4",
    "appid": "wxba6223c06417af7b",
    "openid": "oEWzBfmdLqhFS2mTXCo2E4Y9gJAM",
    "scene": 0,
    "client_ip": "127.0.0.1",
    "_appid": "wxba6223c06417af7b",
    "_timestamp": 1635927954
}
```

压缩`data`（可选）

```json
{"_n":"o89QaPVsRu1yppIZzvSZc4","_appid":"wxba6223c06417af7b","_timestamp":1635927954,"appid":"wxba6223c06417af7b","openid":"oEWzBfmdLqhFS2mTXCo2E4Y9gJAM","scene":0,"client_ip":"127.0.0.1"}
```

计算密文`enc_data`与认证信息`authtag`

```text
base64_encode(enc_data) = 0IDVdrPtSPF/Oe2CTXCV2vVNPbVJdJlP2WaTMQnoYLh5iCrrSNfQFh25EnStDMf0hLlVNBCZQtf9NaV0m4aRA4AAYIO7oR/Ge+4yY4EmZp5EVPB42xjScgMx5X3D4VdLCfynXIUKUtZHZvk1zmLVE3RauzJgiM1BB1CPmwcENo3MTJ0z8Vfkf5tMv54kOXobDLlV5rfqKdAX7gM/rP82DgZdt9vvZX44ipdbHIjJvw83ZXAFtvftdVw2Qd8=
base64_encode(authtag) = 5qeM/2vZv+6KtScN94IpMg==
```

##### 示例代码

nodejs

java

java_sm

### 3.2 加密请求签名

开发者需要对API的POST数据签名，由HTTP请求头传递。

#### 3.2.1 参数说明

##### 请求参数

| HEADER名 | 默认值 | 必填 | 备注 |
| --- | --- | --- | --- |
| Wechatmp-Appid |   | 是 | 当前小程序的Appid |
| Wechatmp-TimeStamp |   | 是 | 签名时时间戳 |
| Wechatmp-Signature |   | 是 | 签名数据，使用base64编码 |

##### 签名字段格式

开发者需先拼接待签名串，使用 `urlpath\n appid\n timestamp\n postdata` 格式，字段之间使用换行符`\n`做分隔符。

| 参数 | 说明 |
| --- | --- |
| urlpath | 当前请求API的URL，不包括URL参数（URL Query），需要带HTTP协议头 |
| appid | 当前小程序的Appid |
| timestamp | 签名时的时间戳，即请求头`Wechatmp-TimeStamp`的值 |
| postdata | 当前请求的POST数据 |

> **注意：SM2withSM3签名需要用到的ID为开发者非对称密钥编号。**

#### 3.2.2 计算示例

以[风控接口为例](https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/safety-control-capability/riskControl.getUserRiskRank.html)，对请求数据签名。

##### RSAwithSHA256

> 签名使用PSS填充方式，需要指定salt长度为32。（PSS签名中包含随机因子，因此每次签名结果都会变化）

私钥信息

```json
{
    "Sn": "97845f6ed842ea860df6fdf65941ff56",
    "PrivateKey": "-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEA3FoQOmOl5/CF5hF7ta4EzCy2LaU3Eu2k9DBwQ73J82I53Sx9\nLAgM1DH3IsYohRRx/BESfbdDI2powvr6QYKVIC+4Yavwg7gzhZRxWWmT1HruEADC\nZAgkUCu+9Il/9FPuitPSoIpBd07NqdkkRe82NBOfrKTdhge/5zd457fl7J81Q5VT\nIxO8vvq7FSw7k6Jtv+eOjR6SZOWbbUO7f9r4UuUkXmvdGv21qiqtaO1EMw4tUCEL\nzY73M7NpCH3RorlommYX3P6q0VrkDHrCE0/QMhmHsF+46E+IRcJ3wtEj3p/mO1Vo\nCpEhawC1U728ZUTwWNEii8hPEhcNAZTKaQMaTQIDAQABAoIBAQCXv5p/a5KcyYKc\n75tfgekh5wTLKIVmDqzT0evuauyCJTouO+4z/ZNAKuzEUO0kwPDCo8s1MpkU8boV\n1Ru1M8WZNePnt65aN+ebbaAl8FRzNvltoeg9VXIUmBvYcjzhOVAE4V2jW7M8A9QU\nzUpyswuED6OeFKfOHtYk2In2IipAqhfbyc6gn7uZSWTQsoO6hGBRQ7Ejx+vgwrbx\nZKVZ7UXbPHD0lOEPraA3PH/QUeUKpNwK2NXQoBxWcR283/HxFSAjjSSsGSBKsCnw\nDN55P2FQ0HNi5YrwUNT9190NIXSeygaRy1b+D+yBfm+yE7/qXwHLZCHsjO+2tMSS\n3KGjllTBAoGBAP9FPeYNKZuu5jt9RpZwXCc9E7Iz7bmM7zws6dun6dQH0xVVWFVm\niGIu07eqyB8HNagXseFzoXLV5EQx+3DaB0bAH+ZEpHGJJpAWSLusigssFUFuTvTF\nw+rC5hxOfidMa6+93SU5pWeJb0zJF8PRDaJ3UmwlwpYubF17sT4PD6p9AoGBANz7\nRlhRSFvggJjhEMpek3OIYWrrlRNO2MVcP7i/fGNTHhrw7OHcNGRof54QZ2Y0baL7\n1vHNokbK2mnT+cQXY/gXMmcE/eV4xyRGYiIL9nBdrkLerc43EYPv+evDvgyji6+y\n4np5cKqHrS8F+YzATk82Jt9HgdI2MvfbJTkSbmgRAoGAHNPL9rPb1An/VA6Ery6H\nKaM7Gy/EE+U3ixsjWbvvqxMrIkieDh7jHftdy2sM6Hwe8hmi6+vr+pTvD0h5tbfZ\nhILj11Q/Idc0NKdflVoZyMM0r0vuvLOsuVFDPUUb+AIoUxNk6vREmpmpqQk4ltN/\n763779yfyef6MuBqFrEKut0CgYB9FfsuuOv1nfINF7EybDCZAETsiee7ozEPHnWv\ndSzK6FytMV1VSBmcEI7UgUKWVu0MifOUsiq+WcsihmvmNLtQzoioSeoSP7ix7ulT\njmP0HQMsNPI7PW67uVZFv2pPqy/Bx8dtPlqpHN3KNV6Z7q0lJ2j/kHGK9UUKidDb\nKnS2kQKBgHZ0cYzwh9YnmfXx9mimF57aQQ8aFc9yaeD5/3G2+a/FZcHtYzUdHQ7P\nPS35blD17/NnhunHhuqakbgarH/LIFMHITCVuGQT4xS34kFVjFVhiT3cHfWyBbJ6\nGbQuzzFxz/UKDDKf3/ON41k8UP20Gdvmv/+c6qQjKPayME81elus\n-----END RSA PRIVATE KEY-----"
}
```

原始请求

> 原postdata总长度324，末尾无回车符`\n`

```http
POST /wxa/getuserriskrank?access_token=ACCESS_TOKEN HTTP/1.1
Host: api.weixin.qq.com
...
Content-Length: 324

{"iv":"fmW/zNxXlytUZBgj","data":"0IDVdrPtSPF/Oe2CTXCV2vVNPbVJdJlP2WaTMQnoYLh5iCrrSNfQFh25EnStDMf0hLlVNBCZQtf9NaV0m4aRA4AAYIO7oR/Ge+4yY4EmZp5EVPB42xjScgMx5X3D4VdLCfynXIUKUtZHZvk1zmLVE3RauzJgiM1BB1CPmwcENo3MTJ0z8Vfkf5tMv54kOXobDLlV5rfqKdAX7gM/rP82DgZdt9vvZX44ipdbHIjJvw83ZXAFtvftdVw2Qd8=","authtag":"5qeM/2vZv+6KtScN94IpMg=="}
```

签名后请求

```http
POST /wxa/getuserriskrank?access_token=ACCESS_TOKEN HTTP/1.1
Host: api.weixin.qq.com
...
Content-Length: 324
Wechatmp-Appid: wxba6223c06417af7b
Wechatmp-TimeStamp: 1635927954
Wechatmp-Signature: wcSSWHZunjz9VKl9q+If9deiyECXDAELfAJNZ4+5T+NhFr8zfhkwdQtlgQ7nN5xs99R57La9UjBTRBGge2KYyshWtw7HIMPAqWNsnpHvx0b2f7s6Bt7OpfOQLlIfNgepgTVmUwrqW8/7A12szj7tCe/bRFilwnaX6N0w4duHlfL7ic7IIZXouvy9dLRAa5GtEk1eD/LPWRiKh0SvJ3znPY/pSiQW9zSkXVdj9UGGM8qcKLzPGJ7gSmt3ZOPkFapk9wqFmhJwQj//xN5+hUlr2UiNPMNSHve5Y2ADLsNHqk5t7RfAZ8nW9/8lzhVt4t+toy1FeehxCGIC8qgmjIl1hg==

{"iv":"fmW/zNxXlytUZBgj","data":"0IDVdrPtSPF/Oe2CTXCV2vVNPbVJdJlP2WaTMQnoYLh5iCrrSNfQFh25EnStDMf0hLlVNBCZQtf9NaV0m4aRA4AAYIO7oR/Ge+4yY4EmZp5EVPB42xjScgMx5X3D4VdLCfynXIUKUtZHZvk1zmLVE3RauzJgiM1BB1CPmwcENo3MTJ0z8Vfkf5tMv54kOXobDLlV5rfqKdAX7gM/rP82DgZdt9vvZX44ipdbHIjJvw83ZXAFtvftdVw2Qd8=","authtag":"5qeM/2vZv+6KtScN94IpMg=="}
```

签名过程数据

拼接待签名串`M`，末尾无额外回车符`\n`

```text
https://api.weixin.qq.com/wxa/getuserriskrank
wxba6223c06417af7b
1635927954
{"iv":"fmW/zNxXlytUZBgj","data":"0IDVdrPtSPF/Oe2CTXCV2vVNPbVJdJlP2WaTMQnoYLh5iCrrSNfQFh25EnStDMf0hLlVNBCZQtf9NaV0m4aRA4AAYIO7oR/Ge+4yY4EmZp5EVPB42xjScgMx5X3D4VdLCfynXIUKUtZHZvk1zmLVE3RauzJgiM1BB1CPmwcENo3MTJ0z8Vfkf5tMv54kOXobDLlV5rfqKdAX7gM/rP82DgZdt9vvZX44ipdbHIjJvw83ZXAFtvftdVw2Qd8=","authtag":"5qeM/2vZv+6KtScN94IpMg=="}
```

使用PSS填充方式计算签名`S`

```text
base64_encode(S) = wcSSWHZunjz9VKl9q+If9deiyECXDAELfAJNZ4+5T+NhFr8zfhkwdQtlgQ7nN5xs99R57La9UjBTRBGge2KYyshWtw7HIMPAqWNsnpHvx0b2f7s6Bt7OpfOQLlIfNgepgTVmUwrqW8/7A12szj7tCe/bRFilwnaX6N0w4duHlfL7ic7IIZXouvy9dLRAa5GtEk1eD/LPWRiKh0SvJ3znPY/pSiQW9zSkXVdj9UGGM8qcKLzPGJ7gSmt3ZOPkFapk9wqFmhJwQj//xN5+hUlr2UiNPMNSHve5Y2ADLsNHqk5t7RfAZ8nW9/8lzhVt4t+toy1FeehxCGIC8qgmjIl1hg==
```

##### 示例代码

nodejs

java

java_sm

## 四、API响应处理

API响应数据需要验签与解密。

响应内的签名算法为RSAwithSHA256，验签需要使用MP`平台证书`验证，可在MP管理页下载最新`平台证书`。

响应内的加密算法、密钥与请求时一致。

### 4.1 验签

由于平台证书存在有效期，平台证书可能过期。在平台证书更换周期内，平台会同时带上最新证书与即将过期证书的签名结果。开发者需要根据已下载的平台`证书编号`找到对应的签名来验证。

> 若发现使用的平台证书编号与响应内的Wechatmp-Serial-Deprecated字段匹配（即当前证书即将过期），请尽快更新MP平台证书。

#### 4.1.1 参数说明

请求参数

| HEADER名 | 默认值 | 必填 | 备注 |
| --- | --- | --- | --- |
| Wechatmp-Appid |   | 是 | 当前小程序的Appid |
| Wechatmp-TimeStamp |   | 是 | 签名时时间戳 |
| Wechatmp-Serial |   | 是 | 平台证书编号，在MP管理页面获取，**非证书内序列号** |
| Wechatmp-Signature |   | 是 | 平台证书签名数据，使用base64编码 |
| Wechatmp-Serial-Deprecated |   | 否 | 即将失效的平台证书编号，**非证书内序列号**，仅在证书更换周期内出现 |
| Wechatmp-Signature-Deprecated |   | 否 | 即将失效的平台证书签名数据，仅在证书更换周期内出现，使用base64编码 |

签名字段格式

开发者需先拼接待签名串，使用 `urlpath\n appid\n timestamp\n respdata` 格式，字段之间使用换行符`\n`做分隔符。

| 参数 | 说明 |
| --- | --- |
| urlpath | 当前请求API的URL，不包括URL参数（URL Query），需要带HTTP协议头 |
| appid | 当前小程序的Appid |
| timestamp | 签名时的时间戳，即响应头`Wechatmp-TimeStamp`的值 |
| respdata | 当前响应的数据 |

> 注意：SM2withSM3验签需要用到的ID为平台证书编号

#### 4.1.2 代码示例

以[风控接口为例](https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/safety-control-capability/riskControl.getUserRiskRank.html)，对服务端回包内容验签。

##### RSAwithSHA256

> 响应的签名也使用PSS填充方式，一般不需要指定salt长度。

证书信息

> 所有参与签名的编号都在MP密钥管理页面获取，非证书内置序列号

```json
{
    "Sn": "79ba700ea147819f640941bceb38b1d1",
    "Certificate": "-----BEGIN CERTIFICATE-----\nMIID0jCCArqgAwIBAgIUeE+Yy7vM/o+eHHsfM+1bGJJEZTQwDQYJKoZIhvcNAQEL\nBQAwXjELMAkGA1UEBhMCQ04xEzARBgNVBAoTClRlbnBheS5jb20xHTAbBgNVBAsT\nFFRlbnBheS5jb20gQ0EgQ2VudGVyMRswGQYDVQQDExJUZW5wYXkuY29tIFJvb3Qg\nQ0EwHhcNMjIwOTA1MDgzOTIyWhcNMjcwOTA0MDgzOTIyWjBkMRswGQYDVQQDDBJ3\neGQ5MzBlYTVkNWEyNThmNGYxFTATBgNVBAoMDFRlbmNlbnQgSW5jLjEOMAwGA1UE\nCwwFV3hnTXAxCzAJBgNVBAYMAkNOMREwDwYDVQQHDAhTaGVuWmhlbjCCASIwDQYJ\nKoZIhvcNAQEBBQADggEPADCCAQoCggEBAM5D9qlkCmk1kr3FpF0e9pc3kGsvz5RA\n0/YRny9xPKIyV2UVMDZvRQ+mDHsiQQFE6etg457KFYSxTDKtItbdl6hJQVGeAvg0\nmqPYE9SkHRGTfL/AnXRbKBG2GC2OcaPSAprsLOersjay2me+9pF8VHybV8aox78A\nNsU75G/OO3V1iEE0s5Pmglqk8DEiw9gB/dGJzsNfXwzvyJyiUP9ZujYexyjsS+/Z\nGdSOUkqL/th+16yHj8alcdyga6YGfWEDyWkt/i/B28cwx4nzwk8xgrurifPaLuMk\n0+9wJQLCfAn/f7zyHrC8PcD1XvvRt9VBNMBASXs3710ODyyVf2lkMgkCAwEAAaOB\ngTB/MAkGA1UdEwQCMAAwCwYDVR0PBAQDAgTwMGUGA1UdHwReMFwwWqBYoFaGVGh0\ndHA6Ly9ldmNhLml0cnVzLmNvbS5jbi9wdWJsaWMvaXRydXNjcmw/Q0E9MUJENDIy\nMEU1MERCQzA0QjA2QUQzOTc1NDk4NDZDMDFDM0U4RUJEMjANBgkqhkiG9w0BAQsF\nAAOCAQEAL2MK9tYu+ljLVBlSbfEeaKyF07TN+G31Ya5NBzeS1ZCx4joUEIyACWmG\nfUkKNKiKV+EMzxeEhKRso1Qif3E7Ipl+PQBoQw6OSR/jFHciYurnGR9CLkL03Zo1\nqw1Xetv9OipsvlpA0SOWc207e/XpGdm8C7FMXM6bzvVp8I/STTjC1vqjIZu9WavI\nRgGM4jyAPz2XogUq0BNijef8BXbbav9fAsXjHSwn5BQv4iLms3fiLm/eoyQ6dZ2R\noTudrlcyr1bG4vwETLmHF+3yfVp9dpvJ+lyfiviwDwyfa8t2WlJm27DuF4vWoxir\nmjgj9tDutIFqxLIovLyg3uiAYtSQ/Q==\n-----END CERTIFICATE-----"
}
```

原始响应

> 响应数据总长度292，末尾无回车符`\n`

```http
HTTP/1.1 200 OK
...
Content-Length: 292
Wechatmp-Appid: wxba6223c06417af7b
Wechatmp-TimeStamp: 1635927956
Wechatmp-Serial: 79ba700ea147819f640941bceb38b1d1
Wechatmp-Signature: Ht0VfQkkEweJ4hU266C14Aj64H9AXfkwNi5zxUZETCvR2svU1ZYdosDhFX/voLj1TyszqKsVxAlENGt7PPZZ8RQX7jnA4SKhiPUhW4LTbyTenisHJ+ohSfDjYnXavjQsBHspFS+BlPHuSSJ2xyQzw1+HuC6nid09ZL4FnGSYo4OI5MJrSb9xLzIVZMIDuUQchGKi/KaB1KzxECLEZcfjqbAgmxC7qOmuBLyO1WkHYDM95NJrHJWba5xv4wrwPru9yYTJSNRnlM+zrW5w9pOubC4Jtj3szTAEuOz9AcqUmgaAvMLNAIa8hfODLRe3n/cu4SgYlN/ZkNRU4QXVNbPGMg==
Wechatmp-Serial-Deprecated: 2171af9cdf1d7404423852e7e183d852
Wechatmp-Signature-Deprecated: ZP1OODikAOePc+YJUMLxunF6xV05kextO/T1fy5lWv/CwV6OCsPBRM2xRRCi+B4lYXbbfYDdjzCz5BIAWEwIdjMlg/IHcJVHhRNAlKt5A3zvzfaJa5IJQel7xuUEXk/B6KVyEb41PbzrptjUGqWyTFMrjxQ4ThJfCuYocnUng7OuDU95enMqK2hZpO8o7kFW638BAwKDSiFNEwEJDWYkLz0kEw7ma3keezm4YHYKfJmjChK39tmZld7Rw/yrV1U9RiL/DO5ayP9VmrQkT/vYrPKyqI4/xKrIaTq44jFYTPIJKdU2OnLt6kjqwp2hvCzMuJdjRcrvzhWJ2A8xZ5hI2w==

{"iv":"r2WDQt56rEAmMuoR","data":"HExs66Ik3el+iM4IpeQ7SMEN934FRLFYOd3EmeaIrpP4EPTHckoco6O+PaoRZRa3lqaPRZT7r52f7LUok6gLxc6cdR8C4vpIIfh4xfLC4L7FNy9GbuMK1hcoi8b7gkWJcwZMkuCFNEDmqn3T49oWzAQOrY4LZnnnykv6oUJotdAsnKvmoJkLK7hRh7M2B1d2UnTnRuoIyarXc5Iojwoghx4BOvnV","authtag":"z2BFD8QctKXTuBlhICGOjQ=="}
```

验签过程数据

拼接待签名串`M`，末尾无额外回车符`\n`

```text
https://api.weixin.qq.com/wxa/getuserriskrank
wxba6223c06417af7b
1635927956
{"iv":"r2WDQt56rEAmMuoR","data":"HExs66Ik3el+iM4IpeQ7SMEN934FRLFYOd3EmeaIrpP4EPTHckoco6O+PaoRZRa3lqaPRZT7r52f7LUok6gLxc6cdR8C4vpIIfh4xfLC4L7FNy9GbuMK1hcoi8b7gkWJcwZMkuCFNEDmqn3T49oWzAQOrY4LZnnnykv6oUJotdAsnKvmoJkLK7hRh7M2B1d2UnTnRuoIyarXc5Iojwoghx4BOvnV","authtag":"z2BFD8QctKXTuBlhICGOjQ=="}
```

计算签名串`M`原始哈希值`H0`

```text
hex(H0) = f797cafd9e323df336fb427569fbe67e20d5bc96dd68a3f54d66b54e6e08bb27
```

根据`平台证书编号`获取签名数据，并使用验签接口校验签名

```text
base64_encode(S) = Ht0VfQkkEweJ4hU266C14Aj64H9AXfkwNi5zxUZETCvR2svU1ZYdosDhFX/voLj1TyszqKsVxAlENGt7PPZZ8RQX7jnA4SKhiPUhW4LTbyTenisHJ+ohSfDjYnXavjQsBHspFS+BlPHuSSJ2xyQzw1+HuC6nid09ZL4FnGSYo4OI5MJrSb9xLzIVZMIDuUQchGKi/KaB1KzxECLEZcfjqbAgmxC7qOmuBLyO1WkHYDM95NJrHJWba5xv4wrwPru9yYTJSNRnlM+zrW5w9pOubC4Jtj3szTAEuOz9AcqUmgaAvMLNAIa8hfODLRe3n/cu4SgYlN/ZkNRU4QXVNbPGMg==
```

##### 示例代码

nodejs

java

java_sm

### 4.2 解密

响应数据的加密算法、格式与请求时一致，可参考请求加密。

#### 4.2.1 示例

以[风控接口为例](https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/safety-control-capability/riskControl.getUserRiskRank.html)， 对原请求数据加密。

##### AES256_GCM

密钥信息

```json
{
    "Sn": "fa05fe1e5bcc79b81ad5ad4b58acf787",
    "Key": "otUpngOjU+nVQaWJIC3D/yMLV17RKaP6t4Ot9tbnzLY="
}
```

响应密文数据

```json
{
    "iv": "r2WDQt56rEAmMuoR",
    "data": "HExs66Ik3el+iM4IpeQ7SMEN934FRLFYOd3EmeaIrpP4EPTHckoco6O+PaoRZRa3lqaPRZT7r52f7LUok6gLxc6cdR8C4vpIIfh4xfLC4L7FNy9GbuMK1hcoi8b7gkWJcwZMkuCFNEDmqn3T49oWzAQOrY4LZnnnykv6oUJotdAsnKvmoJkLK7hRh7M2B1d2UnTnRuoIyarXc5Iojwoghx4BOvnV",
    "authtag": "z2BFD8QctKXTuBlhICGOjQ=="
}
```

解密后数据

```json
{
    "_n": "ShYZpqdVgY+yQVAxNSWhYg",
    "_appid": "wxba6223c06417af7b",
    "_timestamp": 1635927956,
    "errcode": 0,
    "errmsg": "getuserriskrank succ",
    "risk_rank": 0,
    "unoin_id": 2258658297
}
```

原响应数据

```json
{
    "errcode": 0,
    "errmsg": "getuserriskrank succ",
    "risk_rank": 0,
    "unoin_id": 2258658297
}
```

##### 示例代码

nodejs

java

java_sm

## 五、错误码

| 错误码 | 错误码取值 | 解决方案 |
| --- | --- | --- |
| 40230 | API_Missing_Wechatmp_Serial | 缺少Wechatmp_Serial |
| 40231 | API_Missing_Wechatmp_Timestamp | 缺少Wechatmp_Timestamp |
| 40232 | API_Missing_Wechatmp_Signature | 缺少Wechatmp_Signature |
| 40233 | API_Missing_Wechatmp_Appid | 缺少Wechatmp_Appid |
| 40234 | API_Invalid_Signature | 签名错误 |
| 40235 | API_Invalid_Encrypt | 错误的加密 |
| 40236 | API_Invalid_Wechatmp_Appid | 无效的Wechatmp_Appid |
| 40237 | API_Invalid_Wechatmp_Appidmatch | Wechatmp_Appid和Token不匹配 |
| 40238 | API_NoExist_DevSecretSym | 开发者未设置对称密钥 |
| 40239 | API_NoExist_DevSecretAsym | 开发者未设置公钥 |
| 40240 | API_Expired_Wechatmp_Timestamp | 超时的数据 |
