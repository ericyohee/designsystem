# Geniotek 品牌底座

所有场景共用的规则。具体数值只写在 [tokens.md](./tokens.md)（由 `tokens.json` 生成），这里不重复数值。

## 一句话方向

**Precision without noise.** 用层级、克制和证据来表达工程上的可信，而不是用装饰。

## 四条通用原则

1. **先定内容的任务，再定样式。** 先判断这段内容是品牌主张、标题、正文、说明还是技术数据，再选字体和颜色。
2. **信息要完整。** 放不下时先改排版（换行、加宽、上下堆叠），不要为了塞进固定的框而缩小或截掉关键文字。
3. **只展示真实的东西。** 示例数据必须标明是示例；不暗示未经验证的工厂能力、良率、认证或测试结果。
4. **颜色有职责。** 每用一个颜色，要能说出它在做什么：品牌识别、文字、背景、可点击、状态提示，或数据关系。

## 标志

- 文件：[`assets/geniotek-primary-logo.svg`](../assets/geniotek-primary-logo.svg)，深色版（`ink`）。
- 只使用这个官方文件，不要重新绘制、改比例或用文字拼出来。
- 尚未定义：反白版本、最小尺寸、周围留白、放在品牌紫或图片上的用法。

## 颜色

数值见 [tokens.md](./tokens.md)。

- `brand` 负责“认得出是 Geniotek”，`action` 负责“这里可以点”。两者不互换。
- 正文大小的白字不能放在 `brand` 上，要放在 `action` 或 `ink` 上。
- 状态色（成功、警告、错误、提示）只在有真实含义时使用，并且必须配文字，不能只靠颜色。
- 不要把一个流程的每一步涂成不同颜色。

## 字体

数值见 [tokens.md](./tokens.md)。三种字体各有固定任务：

| 角色 | 字体 | 任务 |
| --- | --- | --- |
| display | Archivo 700 / 宽度 118% | 简短的品牌主张 |
| heading / body / label | IBM Plex Sans | 标题、正文、界面、说明 |
| data | IBM Plex Mono | 公差、编号、需要对齐的技术数值 |

- 长标题、描述性标题用 Sans，不用 Display。
- 中文按 IBM Plex Sans SC → 苹方 → 微软雅黑 的顺序回退。IBM Plex Sans SC 的字形覆盖尚未验证。

## 已通过的版面方向

这些是可以参考的先例，不是必须套用的模板。

| 方向 | 状态 | 在哪看 |
| --- | --- | --- |
| Visible / Invisible（紫与黑的对比分区） | 已通过 | [color-system-study-01](../studies/color-system-study-01.html) |
| Service A：品牌色块 + 阅读区 | 已通过 | [color-service-03-ab](../studies/color-service-03-ab.html) |
| Service B：开放式编辑排版 | 已通过 | [color-service-03-ab](../studies/color-service-03-ab.html) |
| Tolerance band（公差带图形） | 概念通过，视觉待审 | [color-evidence-02](../studies/color-evidence-02.html) |

## 还没批准，不能当作标准使用

- 版式：12 / 16 栏、24px 栏间距、8px 间距单位、固定的左侧索引栏。
- 颜色：辅助中性色的最终值、状态色板、深色模式、颜色面积比例、渐变。
- 字体：网页上的具体字号阶梯（正文 16–18px、行高 1.45–1.65 这个范围已定稿，其余未定）。
- 动效：全部为候选，见 [motion-directors-demo-01](../studies/motion-directors-demo-01.html)。
- 图片与视频素材的风格：尚未开始。
