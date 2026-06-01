# Interface: IRigidbodyData

> 官方文档：[Interface: IRigidbodyData](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IRigidbodyData.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Interfaces / IRigidbodyData
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / IRigidbodyData

## Table of contents

### Properties

- [constraintsMask](IRigidbodyData.md)
- [disabled](IRigidbodyData.md)
- [kinematic](IRigidbodyData.md)
- [mass](IRigidbodyData.md)
- [useGravity](IRigidbodyData.md)

## Properties

### constraintsMask

• `Optional` **constraintsMask**: `number`

限制刚体在某个轴上的位移和旋转。
具体值参考{@link RigidbodyConstraints}


### disabled

• `Optional` **disabled**: `boolean`

是否禁用刚体。

**`default`** false


### kinematic

• `Optional` **kinematic**: `boolean`

是否为*运动学(Kinematic)* 刚体。
设置为*运动学*刚体后，除非手动调用[movePosition](../classes/Rigidbody.md)，否则物体不会在*物理模拟*阶段发生位移或旋转。可以理解为，刚体的行为完全在用户的控制之下。

**`default`** false


### mass

• `Optional` **mass**: `number`

物体的质量。

**`limit`** mass > 0

**`default`** 1


### useGravity

• `Optional` **useGravity**: `boolean`

刚体是否受重力影响。

**`default`** true
