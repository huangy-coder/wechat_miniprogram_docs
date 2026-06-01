# Class: Rigidbody

> 官方文档：[Class: Rigidbody](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/Rigidbody.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / Rigidbody
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / Rigidbody

刚体组件。

让物体在物理系统中成为一个有质量的刚体。只有添加了这个组件之后，物体才有可能在物理系统的*物理模拟*阶段发生位移和旋转。

## Hierarchy

- [`Component`](Component.md)<[`IRigidbodyData`](../interfaces/IRigidbodyData.md)> ↳ **`Rigidbody`**

## Table of contents

### Events

- [onAdd](Rigidbody.md)
- [onRelease](Rigidbody.md)
- [onRemove](Rigidbody.md)
- [onTick](Rigidbody.md)
- [onUpdate](Rigidbody.md)

### Properties

- [priority](Rigidbody.md)
- [schema](Rigidbody.md)
- [EVENTS](Rigidbody.md)

### Accessors

- [angularDamping](Rigidbody.md)
- [angularVelocity](Rigidbody.md)
- [centerOfMass](Rigidbody.md)
- [collisionDetectionMode](Rigidbody.md)
- [detectCollisions](Rigidbody.md)
- [el](Rigidbody.md)
- [freezeRotation](Rigidbody.md)
- [inertiaTensor](Rigidbody.md)
- [isKinematic](Rigidbody.md)
- [linearDamping](Rigidbody.md)
- [mass](Rigidbody.md)
- [maxAngularVelocity](Rigidbody.md)
- [maxDepenetrationVelocity](Rigidbody.md)
- [position](Rigidbody.md)
- [positionConstraints](Rigidbody.md)
- [rotation](Rigidbody.md)
- [rotationConstraints](Rigidbody.md)
- [scene](Rigidbody.md)
- [sleepThreshold](Rigidbody.md)
- [solverIterations](Rigidbody.md)
- [solverVelocityIterations](Rigidbody.md)
- [useGravity](Rigidbody.md)
- [velocity](Rigidbody.md)
- [version](Rigidbody.md)

### Methods

- [AddExplosionForce](Rigidbody.md)
- [AddForceAtPosition](Rigidbody.md)
- [addForce](Rigidbody.md)
- [addRelativeForce](Rigidbody.md)
- [addRelativeTorque](Rigidbody.md)
- [addTorque](Rigidbody.md)
- [applyData](Rigidbody.md)
- [closestPointOnBounds](Rigidbody.md)
- [disable](Rigidbody.md)
- [enable](Rigidbody.md)
- [getData](Rigidbody.md)
- [getPointVelocity](Rigidbody.md)
- [getRelativePointVelocity](Rigidbody.md)
- [getWorldCenterOfMass](Rigidbody.md)
- [isSleeping](Rigidbody.md)
- [movePosition](Rigidbody.md)
- [moveRotation](Rigidbody.md)
- [resetCenterOfMass](Rigidbody.md)
- [resetInertiaTensor](Rigidbody.md)
- [setData](Rigidbody.md)
- [setDataOne](Rigidbody.md)
- [setDensity](Rigidbody.md)
- [sleep](Rigidbody.md)
- [wakeUp](Rigidbody.md)

## Events

### onAdd

▸ **onAdd**(`parent`, `data`): `void`

所挂载的`element`被挂载到场景时触发的回调。

#### Parameters

| Name | Type |
| --- | --- |
| `parent` | [`Element`](Element.md) |
| `data` | [`IRigidbodyData`](../interfaces/IRigidbodyData.md) |

#### Returns

`void`

#### Inherited from

[Component](Component.md).[onAdd](Component.md)


### onRelease

▸ **onRelease**(`data`): `void`

从被挂载的`element`上被移除，或是`element`被销毁时，触发的回调。
一般用于释放持有的资源。

#### Parameters

| Name | Type |
| --- | --- |
| `data` | [`IRigidbodyData`](../interfaces/IRigidbodyData.md) |

#### Returns

`void`

#### Inherited from

[Component](Component.md).[onRelease](Component.md)


### onRemove

▸ **onRemove**(`parent`, `data`): `void`

所挂载的`element`从父节点`parent`被移除时，或者自己从`element`上被移除时，触发的回调。
一般用于消除功能的运作。
**如果一个组件的元素直接被销毁了，那这个组件就不会经历onRemove而是直接进入onRelease。**

#### Parameters

| Name | Type |
| --- | --- |
| `parent` | [`Element`](Element.md) |
| `data` | [`IRigidbodyData`](../interfaces/IRigidbodyData.md) |

#### Returns

`void`

#### Inherited from

[Component](Component.md).[onRemove](Component.md)


### onTick

▸ **onTick**(`dateTime`, `data`): `void`

渲染每帧触发的回调。

#### Parameters

| Name | Type |
| --- | --- |
| `dateTime` | `number` |
| `data` | [`IRigidbodyData`](../interfaces/IRigidbodyData.md) |

#### Returns

`void`

#### Inherited from

[Component](Component.md).[onTick](Component.md)


### onUpdate

▸ **onUpdate**(`data`, `preData`): `void`

数据更新时触发的回调。

#### Parameters

| Name | Type |
| --- | --- |
| `data` | [`IRigidbodyData`](../interfaces/IRigidbodyData.md) |
| `preData` | [`IRigidbodyData`](../interfaces/IRigidbodyData.md) |

#### Returns

`void`

#### Inherited from

[Component](Component.md).[onUpdate](Component.md)

## Properties

### priority

• `Readonly` **priority**: `number` = `401`

自定义组件的更新优先级。

#### Overrides

[Component](Component.md).[priority](Component.md)


### schema

• `Readonly` **schema**: [`IComponentSchema`](../interfaces/IComponentSchema.md)

自定义组件的`schema`。

#### Overrides

[Component](Component.md).[schema](Component.md)


### EVENTS

▪ `Static` **EVENTS**: `string`[] = `[]`

#### Inherited from

[Component](Component.md).[EVENTS](Component.md)

## Accessors

### angularDamping

• `get` **angularDamping**(): `number`

角速度阻尼。
影响物体的[角速度](Rigidbody.md)。

**`limit`** angularDamping >= 0

**`default`** 0.05

#### Returns

`number`

• `set` **angularDamping**(`v`): `void`

角速度阻尼。
影响物体的[角速度](Rigidbody.md)。

#### Parameters

| Name | Type |
| --- | --- |
| `v` | `number` |

#### Returns

`void`


### angularVelocity

• `get` **angularVelocity**(): [`Vector3`](Vector3.md)

刚体的角速度。

#### Returns

[`Vector3`](Vector3.md)

• `set` **angularVelocity**(`v`): `void`

刚体的角速度。

#### Parameters

| Name | Type |
| --- | --- |
| `v` | [`Vector3`](Vector3.md) |

#### Returns

`void`


### centerOfMass

• `get` **centerOfMass**(): [`Vector3`](Vector3.md)

刚体的质心相对于LocalTransform的偏移量。
如果不手动设置这一项，会自动根据刚体附着的轮廓来计算质心。

**`see`** [resetCenterOfMass](Rigidbody.md)

#### Returns

[`Vector3`](Vector3.md)

• `set` **centerOfMass**(`v`): `void`

刚体的质心相对于LocalTransform的偏移量。
如果不手动设置这一项，会自动根据刚体附着的轮廓来计算质心。

#### Parameters

| Name | Type |
| --- | --- |
| `v` | [`Vector3`](Vector3.md) |

#### Returns

`void`


### collisionDetectionMode

• `get` **collisionDetectionMode**(): `CollisionDetectionMode`

设置刚体的碰撞检测模式。
详见{@link CollisionDetectionMode}。

**`default`** {@link CollisionDetectionMode.Discrete}

#### Returns

`CollisionDetectionMode`

• `set` **collisionDetectionMode**(`v`): `void`

设置刚体的碰撞检测模式。
详见{@link CollisionDetectionMode}。

#### Parameters

| Name | Type |
| --- | --- |
| `v` | `CollisionDetectionMode` |

#### Returns

`void`


### detectCollisions

• `get` **detectCollisions**(): `boolean`

**`unimplemented`**

**`default`** true

#### Returns

`boolean`

• `set` **detectCollisions**(`v`): `void`

#### Parameters

| Name | Type |
| --- | --- |
| `v` | `boolean` |

#### Returns

`void`


### el

• `get` **el**(): [`Element`](Element.md)

挂载的元素。

#### Returns

[`Element`](Element.md)


### freezeRotation

• `get` **freezeRotation**(): `boolean`

是否允许*物理模拟*过程中对刚体进行旋转。

**`default`** true

#### Returns

`boolean`

• `set` **freezeRotation**(`v`): `void`

是否允许*物理模拟*过程中对刚体进行旋转。

#### Parameters

| Name | Type |
| --- | --- |
| `v` | `boolean` |

#### Returns

`void`


### inertiaTensor

• `get` **inertiaTensor**(): `number`

刚体的转动惯量。
如果不手动设置的话，会自动根据刚体上附着的轮廓计算得出。

**`see`** [resetInertiaTensor](Rigidbody.md)

#### Returns

`number`

• `set` **inertiaTensor**(`v`): `void`

刚体的转动惯量。
如果不手动设置的话，会自动根据刚体上附着的轮廓计算得出。

#### Parameters

| Name | Type |
| --- | --- |
| `v` | `number` |

#### Returns

`void`


### isKinematic

• `get` **isKinematic**(): `boolean`

是否为*运动学(Kinematic)* 刚体。
设置为*运动学*刚体后，除非手动调用[movePosition](Rigidbody.md)，否则物体不会在*物理模拟*阶段发生位移或旋转。可以理解为，刚体的行为完全在用户的控制之下。

**`default`** false

#### Returns

`boolean`

• `set` **isKinematic**(`v`): `void`

是否为*运动学(Kinematic)* 刚体。
设置为*运动学*刚体后，除非手动调用[movePosition](Rigidbody.md)，否则物体不会在*物理模拟*阶段发生位移或旋转。可以理解为，刚体的行为完全在用户的控制之下。

#### Parameters

| Name | Type |
| --- | --- |
| `v` | `boolean` |

#### Returns

`void`


### linearDamping

• `get` **linearDamping**(): `number`

线性阻尼。
影响物体的[线性速度](Rigidbody.md)。

**`limit`** linearDamping >= 0

**`default`** 0

#### Returns

`number`

• `set` **linearDamping**(`v`): `void`

线性阻尼。
影响物体的[线性速度](Rigidbody.md)。

#### Parameters

| Name | Type |
| --- | --- |
| `v` | `number` |

#### Returns

`void`


### mass

• `get` **mass**(): `number`

刚体的质量。

**`limit`** mass > 0

**`default`** 1

#### Returns

`number`

• `set` **mass**(`v`): `void`

刚体的质量。

#### Parameters

| Name | Type |
| --- | --- |
| `v` | `number` |

#### Returns

`void`


### maxAngularVelocity

• `get` **maxAngularVelocity**(): `number`

最大角速度（弧度）。

**`default`** 7

#### Returns

`number`

• `set` **maxAngularVelocity**(`v`): `void`

最大角速度（弧度）。

#### Parameters

| Name | Type |
| --- | --- |
| `v` | `number` |

#### Returns

`void`


### maxDepenetrationVelocity

• `get` **maxDepenetrationVelocity**(): `number`

最大分离速度。
*物理模拟*解决碰撞（相交）的过程中，最大能允许的分离速度。

**`default`** Infinity

#### Returns

`number`

• `set` **maxDepenetrationVelocity**(`v`): `void`

最大分离速度。
*物理模拟*解决碰撞（相交）的过程中，最大能允许的分离速度。

#### Parameters

| Name | Type |
| --- | --- |
| `v` | `number` |

#### Returns

`void`


### position

• `get` **position**(): [`Vector3`](Vector3.md)

直接获取或修改刚体在*物理系统*中的位置。
物理系统中的位置是独立于Transform组件的。

**如果你不清楚修改这一项的后果，请不要手动修改它。修改[Transform.position](Transform.md)来代替。*

#### Returns

[`Vector3`](Vector3.md)

• `set` **position**(`v`): `void`

直接获取或修改刚体在*物理系统*中的位置。
物理系统中的位置是独立于Transform组件的。

**如果你不清楚修改这一项的后果，请不要手动修改它。修改[Transform.position](Transform.md)来代替。*

#### Parameters

| Name | Type |
| --- | --- |
| `v` | [`Vector3`](Vector3.md) |

#### Returns

`void`


### positionConstraints

• `get` **positionConstraints**(): `boolean`[]

限制物体的位移（X轴，Y轴，Z轴）。

**`default`** [false, false, false]

#### Returns

`boolean`[]

• `set` **positionConstraints**(`v`): `void`

限制物体的位移（X轴，Y轴，Z轴）。

#### Parameters

| Name | Type |
| --- | --- |
| `v` | `boolean`[] |

#### Returns

`void`


### rotation

• `get` **rotation**(): [`Quaternion`](Quaternion.md)

直接获取或修改刚体在*物理系统*中的旋转（以四元数表示）。
物理系统中的旋转是独立于节点系统中的Transform的，详见{@link //TODO}。

**如果你不清楚修改这一项的后果，请不要手动修改它。修改{@link Transform3D.euler}或{@link Transform3D.quaternion}来代替。*

#### Returns

[`Quaternion`](Quaternion.md)

• `set` **rotation**(`v`): `void`

直接获取或修改刚体在*物理系统*中的旋转（以四元数表示）。
物理系统中的旋转是独立于节点系统中的Transform的，详见{@link //TODO}。

**如果你不清楚修改这一项的后果，请不要手动修改它。修改{@link Transform3D.euler}或{@link Transform3D.quaternion}来代替。*

#### Parameters

| Name | Type |
| --- | --- |
| `v` | [`Quaternion`](Quaternion.md) |

#### Returns

`void`


### rotationConstraints

• `get` **rotationConstraints**(): `boolean`[]

限制物体的旋转（X轴，Y轴，Z轴）。

**`default`** [false, false, false]

#### Returns

`boolean`[]

• `set` **rotationConstraints**(`v`): `void`

限制物体的旋转（X轴，Y轴，Z轴）。

#### Parameters

| Name | Type |
| --- | --- |
| `v` | `boolean`[] |

#### Returns

`void`


### scene

• `get` **scene**(): [`Scene`](Scene.md)

当前场景。

#### Returns

[`Scene`](Scene.md)


### sleepThreshold

• `get` **sleepThreshold**(): `number`

设置刚体进入休眠的动能阈值。

**`default`** 0.005

#### Returns

`number`

• `set` **sleepThreshold**(`v`): `void`

设置刚体进入休眠的动能阈值。

#### Parameters

| Name | Type |
| --- | --- |
| `v` | `number` |

#### Returns

`void`


### solverIterations

• `get` **solverIterations**(): `number`

设置*物理模拟*过程中解决碰撞的迭代次数。
更高的迭代次数，会消耗更多性能，产生更自然的物理碰撞效果。
如果发现静息状态的刚体（比如说放在地面上），会发生抖动，可以考虑提高这项数值。

**`limit`** solverIterations > 0

**`default`** 6

#### Returns

`number`

• `set` **solverIterations**(`v`): `void`

设置*物理模拟*过程中解决碰撞的迭代次数。
更高的迭代次数，会消耗更多性能，产生更自然的物理碰撞效果。
如果发现静息状态的刚体（比如说放在地面上），会发生抖动，可以考虑提高这项数值。

#### Parameters

| Name | Type |
| --- | --- |
| `v` | `number` |

#### Returns

`void`


### solverVelocityIterations

• `get` **solverVelocityIterations**(): `number`

设置*物理模拟*过程中计算碰撞后速度的迭代次数。
更高的迭代次数，会消耗更多性能，产生更准确的分离速度。

**`limit`** solverVelocityIterations > 0

**`default`** 1

#### Returns

`number`

• `set` **solverVelocityIterations**(`v`): `void`

设置*物理模拟*过程中计算碰撞后速度的迭代次数。
更高的迭代次数，会消耗更多性能，产生更准确的分离速度。

#### Parameters

| Name | Type |
| --- | --- |
| `v` | `number` |

#### Returns

`void`


### useGravity

• `get` **useGravity**(): `boolean`

刚体是否受重力影响。

**`default`** true

#### Returns

`boolean`

• `set` **useGravity**(`v`): `void`

刚体是否受重力影响。

#### Parameters

| Name | Type |
| --- | --- |
| `v` | `boolean` |

#### Returns

`void`


### velocity

• `get` **velocity**(): [`Vector3`](Vector3.md)

刚体的线性速度。

**修改这一项会造成速度突变，一般情况下可以使用[addForce](Rigidbody.md)来代替。*

#### Returns

[`Vector3`](Vector3.md)

• `set` **velocity**(`v`): `void`

刚体的线性速度。

**修改这一项会造成速度突变，一般情况下可以使用[addForce](Rigidbody.md)来代替。*

#### Parameters

| Name | Type |
| --- | --- |
| `v` | [`Vector3`](Vector3.md) |

#### Returns

`void`


### version

• `get` **version**(): `number`

当前版本，每次有数据更新都会增加，可以用作和其他组件合作的依据。

#### Returns

`number`

## Methods

### AddExplosionForce

▸ **AddExplosionForce**(`explosionForce`, `explosionPosition`, `explosionRadius`, `upwardsModifier`, `mode`): `void`

生成一次模拟爆炸的力。
爆炸范围可以视作一个球状物体，如果球体和刚体产生*相交*，则会在刚体上产生推力。
推力的大小和*相交点*与球心的距离有关，推力的方向从球心指向相交点，推力作用位于*相交点*。

视刚体有无附着的轮廓，分为两种情况：

- 无轮廓（或爆炸球心在刚体轮廓内）
相交的判定使用刚体的质心；相交点也取刚体的质心。
- 有轮廓
相交的判定使用刚体的所有轮廓；相交点取轮廓距离球心最近的那一点。

**`limit`** explosionForce > 0

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `explosionForce` | `number` | 爆炸力的大小。 |
| `explosionPosition` | [`Vector3`](Vector3.md) | 爆炸球体的球心位置。 |
| `explosionRadius` | `number` | 爆炸球体的半径。 |
| `upwardsModifier` | `number` | 使用相对数值来修改推力的*作用位置*的y坐标。 |
| `mode` | `ForceMode` | 力的类型。 |

#### Returns

`void`


### AddForceAtPosition

▸ **AddForceAtPosition**(`force`, `position`, `mode`): `void`

为刚体施加力，会影响刚体的[线性速度](Rigidbody.md)和[角速度](Rigidbody.md)。

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `force` | [`Vector3`](Vector3.md) | 世界坐标下矢量形式的力，作用在position位置上。 |
| `position` | [`Vector3`](Vector3.md) | 力的作用位置。 |
| `mode` | `ForceMode` | 力的类型。 |

#### Returns

`void`


### addForce

▸ **addForce**(`force`, `mode`): `void`

为刚体施加力，会影响刚体的[线性速度](Rigidbody.md)。

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `force` | [`Vector3`](Vector3.md) | 世界坐标下矢量形式的力，作用在物体质心上。 |
| `mode` | `ForceMode` | 力的类型。 |

#### Returns

`void`


### addRelativeForce

▸ **addRelativeForce**(`force`, `mode`): `void`

为刚体施加力，会影响刚体的[线性速度](Rigidbody.md)。

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `force` | [`Vector3`](Vector3.md) | **局部**坐标下矢量形式的力，作用在物体质心上。 |
| `mode` | `ForceMode` | 力的类型。 |

#### Returns

`void`


### addRelativeTorque

▸ **addRelativeTorque**(`torque`, `mode`): `void`

为刚体施加力矩，会影响刚体的[角速度](Rigidbody.md)。

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `torque` | [`Vector3`](Vector3.md) | **局部**坐标下矢量形式的力矩。 |
| `mode` | `ForceMode` | 力矩的类型。 |

#### Returns

`void`


### addTorque

▸ **addTorque**(`torque`, `mode`): `void`

为刚体施加力矩，会影响刚体的[角速度](Rigidbody.md)。

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `torque` | [`Vector3`](Vector3.md) | 世界坐标下矢量形式的力矩。 |
| `mode` | `ForceMode` | 力矩的类型。 |

#### Returns

`void`


### applyData

▸ **applyData**(`data`): `void`

#### Parameters

| Name | Type |
| --- | --- |
| `data` | [`IRigidbodyData`](../interfaces/IRigidbodyData.md) |

#### Returns

`void`


### closestPointOnBounds

▸ **closestPointOnBounds**(`position`): [`Vector3`](Vector3.md)

测试刚体**表面上**距离某点最近的位置。
如果给予的position在刚体内部，会返回position。
如果刚体无附着的轮廓，会返回[Infinity, Infinity, Infinity]。

#### Parameters

| Name | Type |
| --- | --- |
| `position` | [`Vector3`](Vector3.md) |

#### Returns

[`Vector3`](Vector3.md)


### disable

▸ **disable**(): `void`

#### Returns

`void`


### enable

▸ **enable**(): `void`

#### Returns

`void`


### getData

▸ **getData**<`T`>(`key`): [`IRigidbodyData`](../interfaces/IRigidbodyData.md)[`T`]

获取一个当前值。

#### Type parameters

| Name | Type |
| --- | --- |
| `T` | extends keyof [`IRigidbodyData`](../interfaces/IRigidbodyData.md) |

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `T` |

#### Returns

[`IRigidbodyData`](../interfaces/IRigidbodyData.md)[`T`]

#### Inherited from

[Component](Component.md).[getData](Component.md)


### getPointVelocity

▸ **getPointVelocity**(`worldPoint`): [`Vector3`](Vector3.md)

获取刚体内某一点在世界坐标下的速度。

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `worldPoint` | [`Vector3`](Vector3.md) | 世界坐标下的位置（其实在刚体外也可以）。 |

#### Returns

[`Vector3`](Vector3.md)


### getRelativePointVelocity

▸ **getRelativePointVelocity**(`relativePoint`): [`Vector3`](Vector3.md)

获取刚体内某一点在**局部**坐标下的速度。

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `relativePoint` | [`Vector3`](Vector3.md) | **局部**坐标下的位置（其实在刚体外也可以）。 |

#### Returns

[`Vector3`](Vector3.md)


### getWorldCenterOfMass

▸ **getWorldCenterOfMass**(): [`Vector3`](Vector3.md)

#### Returns

[`Vector3`](Vector3.md)

刚体质心在世界坐标中的位置。


### isSleeping

▸ **isSleeping**(): `boolean`

**`see`** [sleep](Rigidbody.md)

#### Returns

`boolean`

刚体是否处于休眠状态。


### movePosition

▸ **movePosition**(`position`): `void`

对于***非**运动学刚体*来说，等于直接修改[position](Rigidbody.md)；
对于*运动学刚体*来说，位置变化会在下一帧生效。可以视作物体在这一帧的*物理模拟*中沿直线路径**移动**到了目的地。

**`see`** [isKinematic](Rigidbody.md)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `position` | [`Vector3`](Vector3.md) | 位移的终点 |

#### Returns

`void`


### moveRotation

▸ **moveRotation**(`rotation`): `void`

**`unimplemented`** 暂未支持，请使用[rotation](Rigidbody.md)属性或{@link Transform3D.quaternion}代替。

#### Parameters

| Name | Type |
| --- | --- |
| `rotation` | [`Quaternion`](Quaternion.md) |

#### Returns

`void`


### resetCenterOfMass

▸ **resetCenterOfMass**(): `void`

手动触发，根据刚体附着的轮廓重新计算刚体的质心。

**`see`** [centerOfMass](Rigidbody.md)

#### Returns

`void`


### resetInertiaTensor

▸ **resetInertiaTensor**(): `void`

手动触发，根据刚体附着的轮廓重新计算刚体的转动惯量。

**`see`** [inertiaTensor](Rigidbody.md)

#### Returns

`void`


### setData

▸ **setData**(`data`): `void`

不通过`xml`而是直接设置`data`，注意值的类型需要和`schema`中一致。

#### Parameters

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`IRigidbodyData`](../interfaces/IRigidbodyData.md)> |

#### Returns

`void`

#### Inherited from

[Component](Component.md).[setData](Component.md)


### setDataOne

▸ **setDataOne**<`T`>(`key`, `value`): `void`

设置一个数据。

#### Type parameters

| Name | Type |
| --- | --- |
| `T` | extends keyof [`IRigidbodyData`](../interfaces/IRigidbodyData.md) |

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | [`IRigidbodyData`](../interfaces/IRigidbodyData.md)[`T`] |

#### Returns

`void`

#### Inherited from

[Component](Component.md).[setDataOne](Component.md)


### setDensity

▸ **setDensity**(`density`): `void`

根据给定的密度和刚体附着的轮廓，来计算刚体的质量。

**`see`** [mass](Rigidbody.md)

#### Parameters

| Name | Type |
| --- | --- |
| `density` | `number` |

#### Returns

`void`


### sleep

▸ **sleep**(): `void`

强迫刚体进入休眠状态（至少一帧），休眠状态详见{@link //todo}。
**如果下一帧发生碰撞则会立刻醒来。*

#### Returns

`void`


### wakeUp

▸ **wakeUp**(): `void`

强制唤醒刚体（离开休眠状态）。

**`see`** [sleep](Rigidbody.md)

#### Returns

`void`
