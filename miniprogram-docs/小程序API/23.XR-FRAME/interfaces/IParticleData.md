# Interface: IParticleData

> 官方文档：[Interface: IParticleData](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/interfaces/IParticleData.html)
> 所属分类：[XR-FRAME](../XR-FRAME目录.md)
> 导航路径：XR-FRAME / Interfaces / IParticleData
> 整理日期：2026-06-01
> 本地化说明：正文按官方 API 页面结构转换为 Markdown，保留参数、返回值、回调、错误码、版本限制、注意事项和示例等开发信息。

[xr-frame](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/) / [Exports](https://developers.weixin.qq.com/miniprogram/dev/api/xr-frame/modules.html) / IParticleData

[Particle](../classes/Particle.md)组件数据接口。

## Table of contents

### Properties

- [angle](IParticleData.md)
- [angularSpeed](IParticleData.md)
- [atlas](IParticleData.md)
- [atlasFrames](IParticleData.md)
- [atlasLoop](IParticleData.md)
- [atlasRandom](IParticleData.md)
- [atlasSpeed](IParticleData.md)
- [burstCount](IParticleData.md)
- [burstCycle](IParticleData.md)
- [burstInterval](IParticleData.md)
- [burstTime](IParticleData.md)
- [capacity](IParticleData.md)
- [colorChange](IParticleData.md)
- [delay](IParticleData.md)
- [emitRate](IParticleData.md)
- [emitterProps](IParticleData.md)
- [emitterType](IParticleData.md)
- [endColor](IParticleData.md)
- [gravity](IParticleData.md)
- [lifeTime](IParticleData.md)
- [mesh](IParticleData.md)
- [neverCull](IParticleData.md)
- [prewarmCycles](IParticleData.md)
- [renderMode](IParticleData.md)
- [scaleX](IParticleData.md)
- [scaleY](IParticleData.md)
- [size](IParticleData.md)
- [sizeChange](IParticleData.md)
- [speed](IParticleData.md)
- [speedChange](IParticleData.md)
- [speedDampen](IParticleData.md)
- [startColor](IParticleData.md)
- [startColor2](IParticleData.md)
- [states](IParticleData.md)
- [stopDuration](IParticleData.md)
- [texture](IParticleData.md)
- [uniforms](IParticleData.md)

## Properties

### angle

• `Optional` **angle**: `number`[]

初始角度。


### angularSpeed

• `Optional` **angularSpeed**: `number`[]

角速度。


### atlas

• `Optional` **atlas**: [`Atlas`](../classes/Atlas.md)

动画图集信息。


### atlasFrames

• `Optional` **atlasFrames**: `string`[]

指定图集帧名。


### atlasLoop

• `Optional` **atlasLoop**: `boolean`

是否循环播放图集。


### atlasRandom

• `Optional` **atlasRandom**: `boolean`

是否随机播放图集。


### atlasSpeed

• `Optional` **atlasSpeed**: `number`

图集切换速度。


### burstCount

• `Optional` **burstCount**: `number`


### burstCycle

• `Optional` **burstCycle**: `number`


### burstInterval

• `Optional` **burstInterval**: `number`


### burstTime

• `Optional` **burstTime**: `number`


### capacity

• `Optional` **capacity**: `number`

最大粒子数目。


### colorChange

• `Optional` **colorChange**: [`string`, `string`][]


### delay

• `Optional` **delay**: `number`

粒子系统启动延时秒数。


### emitRate

• `Optional` **emitRate**: `number`

每秒粒子发射数。


### emitterProps

• `Optional` **emitterProps**: [`string`, `string`][]

发射器属性配置。


### emitterType

• `Optional` **emitterType**: `string`

发射器类型。


### endColor

• `Optional` **endColor**: `number`[]

粒子结束时颜色。


### gravity

• `Optional` **gravity**: `number`

y轴方向上的每秒位移。


### lifeTime

• `Optional` **lifeTime**: `number`[]

生命周期时长。


### mesh

• `Optional` **mesh**: [`Geometry`](../classes/Geometry.md)

网格信息。


### neverCull

• `Optional` **neverCull**: `boolean`


### prewarmCycles

• `Optional` **prewarmCycles**: `number`

粒子预渲染周期数。


### renderMode

• `Optional` **renderMode**: `string`

渲染模式。


### scaleX

• `Optional` **scaleX**: `number`[]

粒子在x轴方向上的大小尺度。


### scaleY

• `Optional` **scaleY**: `number`[]

粒子在y轴方向上的大小尺度。


### size

• `Optional` **size**: `number`[]

初始大小。


### sizeChange

• `Optional` **sizeChange**: [`string`, `string`][]


### speed

• `Optional` **speed**: `number`[]

速度。


### speedChange

• `Optional` **speedChange**: [`string`, `string`][]


### speedDampen

• `Optional` **speedDampen**: `number`

速度阻尼系数。


### startColor

• `Optional` **startColor**: `number`[]

粒子初始颜色左区间。


### startColor2

• `Optional` **startColor2**: `number`[]

粒子初始颜色右区间。


### states

• `Optional` **states**: [`string`, `string`][]


### stopDuration

• `Optional` **stopDuration**: `number`

粒子系统生命周期时长。


### texture

• `Optional` **texture**: `default`

纹理信息。


### uniforms

• `Optional` **uniforms**: [`string`, `string`][]
