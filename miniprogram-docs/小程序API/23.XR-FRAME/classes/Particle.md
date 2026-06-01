# Class: Particle

> 官方文档：[Class: Particle](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/classes/Particle.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Classes / Particle
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / Particle

## Hierarchy

- `BasicParticle` ↳ **`Particle`**

## Table of contents

### Constructors

- [constructor](Particle.md)

### Events

- [onAdd](Particle.md)
- [onRelease](Particle.md)
- [onRemove](Particle.md)
- [onTick](Particle.md)
- [onUpdate](Particle.md)

### Properties

- [priority](Particle.md)
- [schema](Particle.md)
- [subEmitters](Particle.md)
- [EVENTS](Particle.md)

### Accessors

- [billboardMode](Particle.md)
- [data](Particle.md)
- [el](Particle.md)
- [emitterPosition](Particle.md)
- [id](Particle.md)
- [material](Particle.md)
- [particleEmitter](Particle.md)
- [scene](Particle.md)
- [spriteChangeSpeed](Particle.md)
- [useBillboard](Particle.md)
- [useRampGradients](Particle.md)
- [useRandomSpriteCellIndex](Particle.md)
- [useSpriteCellLoop](Particle.md)
- [useSpriteSheet](Particle.md)
- [version](Particle.md)

### Methods

- [addAlphaGradient](Particle.md)
- [addColorGradient](Particle.md)
- [addColorRemapGradient](Particle.md)
- [addDragGradient](Particle.md)
- [addLimitSpeedGradient](Particle.md)
- [addRampGradient](Particle.md)
- [addSizeGradient](Particle.md)
- [addSpeedScaleGradient](Particle.md)
- [clone](Particle.md)
- [createBoxEmitter](Particle.md)
- [createPointEmitter](Particle.md)
- [createSphereEmitter](Particle.md)
- [createSubEmitter](Particle.md)
- [getData](Particle.md)
- [initParticle](Particle.md)
- [resetParticle](Particle.md)
- [setData](Particle.md)
- [setDataOne](Particle.md)
- [start](Particle.md)
- [stop](Particle.md)

## Constructors

### constructor

• **new Particle**()

#### Inherited from

BasicParticle.constructor

## Events

### onAdd

• **onAdd**:


### onRelease

• **onRelease**:


### onRemove

• **onRemove**:


### onTick

• **onTick**:


### onUpdate

• **onUpdate**:

## Properties

### priority

• `Readonly` **priority**: `number` = `300`

#### Overrides

BasicParticle.priority


### schema

• `Readonly` **schema**: [`IComponentSchema`](../interfaces/IComponentSchema.md)

详见[ParticleSchema](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html#ParticleSchema)。

#### Inherited from

BasicParticle.schema


### subEmitters

• **subEmitters**: `any` = `null`


### EVENTS

▪ `Static` **EVENTS**: `string`[]

#### Overrides

BasicParticle.EVENTS

## Accessors

### billboardMode

• `get` **billboardMode**(): `number`

#### Returns

`number`

• `set` **billboardMode**(`value`): `void`

#### Parameters

| Name | Type |
| --- | --- |
| `value` | `number` |

#### Returns

`void`


### data

• `get` **data**(): [`IParticleData`](../interfaces/IParticleData.md)

#### Returns

[`IParticleData`](../interfaces/IParticleData.md)

• `set` **data**(`value`): `void`

#### Parameters

| Name | Type |
| --- | --- |
| `value` | [`IParticleData`](../interfaces/IParticleData.md) |

#### Returns

`void`


### el

• `get` **el**(): [`Element`](Element.md)

挂载的元素。

#### Returns

[`Element`](Element.md)


### emitterPosition

• `get` **emitterPosition**(): [`Vector3`](Vector3.md)

#### Returns

[`Vector3`](Vector3.md)

• `set` **emitterPosition**(`value`): `void`

#### Parameters

| Name | Type |
| --- | --- |
| `value` | [`Vector3`](Vector3.md) |

#### Returns

`void`


### id

• `get` **id**(): `number`

#### Returns

`number`


### material

• `get` **material**(): [`Material`](Material.md)

#### Returns

[`Material`](Material.md)

• `set` **material**(`value`): `void`

#### Parameters

| Name | Type |
| --- | --- |
| `value` | [`Material`](Material.md) |

#### Returns

`void`


### particleEmitter

• `get` **particleEmitter**(): `BasicShapeEmitter`

#### Returns

`BasicShapeEmitter`


### scene

• `get` **scene**(): [`Scene`](Scene.md)

当前场景。

#### Returns

[`Scene`](Scene.md)


### spriteChangeSpeed

• `get` **spriteChangeSpeed**(): `number`

#### Returns

`number`


### useBillboard

• `get` **useBillboard**(): `boolean`

#### Returns

`boolean`

• `set` **useBillboard**(`value`): `void`

#### Parameters

| Name | Type |
| --- | --- |
| `value` | `boolean` |

#### Returns

`void`


### useRampGradients

• `get` **useRampGradients**(): `boolean`

#### Returns

`boolean`

• `set` **useRampGradients**(`value`): `void`

#### Parameters

| Name | Type |
| --- | --- |
| `value` | `boolean` |

#### Returns

`void`


### useRandomSpriteCellIndex

• `get` **useRandomSpriteCellIndex**(): `boolean`

#### Returns

`boolean`


### useSpriteCellLoop

• `get` **useSpriteCellLoop**(): `boolean`

#### Returns

`boolean`


### useSpriteSheet

• `get` **useSpriteSheet**(): `boolean`

#### Returns

`boolean`

• `set` **useSpriteSheet**(`value`): `void`

#### Parameters

| Name | Type |
| --- | --- |
| `value` | `boolean` |

#### Returns

`void`


### version

• `get` **version**(): `number`

当前版本，每次有数据更新都会增加，可以用作和其他组件合作的依据。

#### Returns

`number`

## Methods

### addAlphaGradient

▸ **addAlphaGradient**(`gradient`, `alpha`, `alpha2?`): `void`

添加粒子运动过程中的透明度变化规则。

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `gradient` | `number` | 指定所处粒子生命周期的阶段 |
| `alpha` | `number` | 指定粒子颜色透明度的左区间[0-1] |
| `alpha2?` | `number` | 指定粒子颜色透明度的右区间[0-1] |

#### Returns

`void`

#### Inherited from

BasicParticle.addAlphaGradient


### addColorGradient

▸ **addColorGradient**(`gradient`, `color1`, `color2?`): `void`

添加粒子运动过程中的颜色变化规则。

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `gradient` | `number` | 指定所处粒子生命周期的阶段 |
| `color1` | [`Vector4`](Vector4.md) | 指定粒子颜色的左区间 |
| `color2?` | [`Vector4`](Vector4.md) | 指定粒子颜色的右区间 |

#### Returns

`void`

#### Inherited from

BasicParticle.addColorGradient


### addColorRemapGradient

▸ **addColorRemapGradient**(`gradient`, `min`, `max?`): `void`

添加粒子运动过程中的透明度变化范围。

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `gradient` | `number` | 指定所处粒子生命周期的阶段 |
| `min` | `number` | 指定粒子透明度值的左区间 |
| `max?` | `number` | 指定粒子透明度值的右区间 |

#### Returns

`void`

#### Inherited from

BasicParticle.addColorRemapGradient


### addDragGradient

▸ **addDragGradient**(`gradient`, `drag`, `drag2?`): `void`

添加粒子运动过程中的阻力规则。

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `gradient` | `number` | 指定所处粒子生命周期的阶段 |
| `drag` | `number` | - |
| `drag2?` | `number` | - |

#### Returns

`void`

#### Inherited from

BasicParticle.addDragGradient


### addLimitSpeedGradient

▸ **addLimitSpeedGradient**(`gradient`, `limitSpeed`, `limitSpeed2?`): `void`

添加粒子运动过程中的速度限制规则。

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `gradient` | `number` | 指定所处粒子生命周期的阶段 |
| `limitSpeed` | `number` | 指定粒子限制速度的左区间 |
| `limitSpeed2?` | `number` | 指定粒子限制速度的右区间 |

#### Returns

`void`

#### Inherited from

BasicParticle.addLimitSpeedGradient


### addRampGradient

▸ **addRampGradient**(`gradient`, `color`): `void`

添加粒子运动过程中的根据透明度影响的颜色变化规则，将通过颜色变化图纹理进行采样。

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `gradient` | `any` | 指定粒子颜色变化图的具体位置，对应具体值应为(1-alpha) |
| `color` | `any` | 指定该位置的颜色 |

#### Returns

`void`

#### Inherited from

BasicParticle.addRampGradient


### addSizeGradient

▸ **addSizeGradient**(`gradient`, `size`, `size2?`): `void`

添加粒子运动过程中的尺寸变化规则。

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `gradient` | `number` | 指定所处粒子生命周期的阶段 |
| `size` | `number` | 指定粒子尺寸的左区间 |
| `size2?` | `number` | 指定粒子尺寸的右区间 |

#### Returns

`void`

#### Inherited from

BasicParticle.addSizeGradient


### addSpeedScaleGradient

▸ **addSpeedScaleGradient**(`gradient`, `speed`, `speed2?`): `void`

添加粒子运动过程中的速度变化规则。

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `gradient` | `number` | 指定所处粒子生命周期的阶段 |
| `speed` | `number` | 指定粒子速度的左区间 |
| `speed2?` | `number` | 指定粒子速度的右区间 |

#### Returns

`void`

#### Inherited from

BasicParticle.addSpeedScaleGradient


### clone

▸ **clone**(): [`Particle`](Particle.md)

获取一个拷贝的粒子系统。

#### Returns

[`Particle`](Particle.md)

#### Inherited from

BasicParticle.clone


### createBoxEmitter

▸ **createBoxEmitter**(`direction1`, `direction2`, `minEmitBox`, `maxEmitBox`): `default`

创建一个箱形发射器。

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `direction1` | [`Vector3`](Vector3.md) | 粒子运动方向左区间 |
| `direction2` | [`Vector3`](Vector3.md) | 粒子运动方向右区间 |
| `minEmitBox` | [`Vector3`](Vector3.md) | 粒子生成位置最小允许坐标 |
| `maxEmitBox` | [`Vector3`](Vector3.md) | 粒子生成位置最大允许坐标 |

#### Returns

`default`

箱形发射器

#### Inherited from

BasicParticle.createBoxEmitter


### createPointEmitter

▸ **createPointEmitter**(`direction1`, `direction2`): `default`

创建一个点发射器。

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `direction1` | [`Vector3`](Vector3.md) | 粒子运动方向左区间 |
| `direction2` | [`Vector3`](Vector3.md) | 粒子运动方向右区间 |

#### Returns

`default`

点发射器

#### Inherited from

BasicParticle.createPointEmitter


### createSphereEmitter

▸ **createSphereEmitter**(`radius`, `radiusRange`, `arc`, `randomizeDirection`): `default`

创建一个球形发射器。

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `radius` | `number` | 球形半径 |
| `radiusRange` | `number` | 球形区域内的覆盖范围[0-1] |
| `arc` | `number` | 粒子在球形内生成的角度区间[0-360] |
| `randomizeDirection` | `number` | 粒子运动方向偏离程度[0-1] |

#### Returns

`default`

球形发射器

#### Inherited from

BasicParticle.createSphereEmitter


### createSubEmitter

▸ **createSubEmitter**(`data`): `SubEmitter`

获取一个粒子子发射器。

#### Parameters

| Name | Type |
| --- | --- |
| `data` | [`IParticleData`](../interfaces/IParticleData.md) |

#### Returns

`SubEmitter`

#### Inherited from

BasicParticle.createSubEmitter


### getData

▸ **getData**<`T`>(`key`): [`IParticleData`](../interfaces/IParticleData.md)[`T`]

获取一个当前值。

#### Type parameters

| Name | Type |
| --- | --- |
| `T` | extends keyof [`IParticleData`](../interfaces/IParticleData.md) |

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `T` |

#### Returns

[`IParticleData`](../interfaces/IParticleData.md)[`T`]

#### Inherited from

BasicParticle.getData


### initParticle

▸ **initParticle**(`data`): `void`

初始化粒子系统的状态。

#### Parameters

| Name | Type |
| --- | --- |
| `data` | [`IParticleData`](../interfaces/IParticleData.md) |

#### Returns

`void`


### resetParticle

▸ **resetParticle**(): `void`

重置粒子系统的状态。

#### Returns

`void`


### setData

▸ **setData**(`data`): `void`

不通过`xml`而是直接设置`data`，注意值的类型需要和`schema`中一致。

#### Parameters

| Name | Type |
| --- | --- |
| `data` | `Partial`<[`IParticleData`](../interfaces/IParticleData.md)> |

#### Returns

`void`

#### Inherited from

BasicParticle.setData


### setDataOne

▸ **setDataOne**<`T`>(`key`, `value`): `void`

设置一个数据。

#### Type parameters

| Name | Type |
| --- | --- |
| `T` | extends keyof [`IParticleData`](../interfaces/IParticleData.md) |

#### Parameters

| Name | Type |
| --- | --- |
| `key` | `T` |
| `value` | [`IParticleData`](../interfaces/IParticleData.md)[`T`] |

#### Returns

`void`

#### Inherited from

BasicParticle.setDataOne


### start

▸ **start**(`delay?`): `void`

粒子系统开始播放。

#### Parameters

| Name | Type | Default value | Description |
| --- | --- | --- | --- |
| `delay` | `number` | `0` | 设定粒子延时几秒后再播放。 |

#### Returns

`void`


### stop

▸ **stop**(): `void`

停止粒子系统与其子发射器的播放。

#### Returns

`void`
