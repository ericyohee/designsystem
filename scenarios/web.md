# 网页

适用于 geniotekdev.com 及其他网页。当前用 Framer 制作，由 Codex 通过 Framer MCP 操作。

先读 [品牌底座](../core/brand.md)。

## 在 Framer 里

- Framer 的颜色样式和文字样式要与 [tokens.md](../core/tokens.md) 同名同值。页面只用这些样式，不直接填色号。
- 重复出现的版面做成 Framer 组件，新页面优先拼已有组件。
- 改动先在 Framer 分支里做，审过再合并。

## 做一个页面的顺序

1. 先确定读者要完成的阅读任务、内容的主次和希望的下一步动作。不要从“选几栏”开始。
2. 选页面类型：开放式编辑排版、结构化的服务介绍、参考/技术资料，或其他有理由的形式。
3. 确定页面边界和各区域的起点，再在区域内部排局部结构。
4. 确定线条、色块、图片可以延伸到哪里。
5. 确定行宽、间距和各元素的相对轻重。
6. 做出真实的响应式版面，然后在窄屏、更长的文案、浏览器放大 200%、关闭辅助线这四种情况下检查。

## 已定稿

- 三种字体的分工，见 [品牌底座](../core/brand.md)。
- 正文 16–18px，行高 1.45–1.65。
- 关键文字不为适配固定高度而缩小或截断。

## 可参考的版面

见 [品牌底座](../core/brand.md) 的“已通过的版面方向”。

## 候选值（可用于试验，不是标准）

- 12 栏或 16 栏、24px 栏间距、8px 间距单位。
- 标题字号、字距、行高的具体数值。

## 尚未定义

- 组件库、页面区块库、页面结构模板。
- 图片与媒体的规范。
- 动效规范，见 [视频与动效](./video.md)。

## 研究记录

| 主题 | 页面 |
| --- | --- |
| 总览、字体、颜色、版式 | [index.html](../index.html) |
| 颜色体系与对比度检查 | [color-system-study-01](../studies/color-system-study-01.html) |
| 服务流程 A/B 版面 | [color-service-03-ab](../studies/color-service-03-ab.html) |
| 公差带 | [color-evidence-02](../studies/color-evidence-02.html) |
| 文字角色排版 | [semantic-roles-composition-v2](../studies/semantic-roles-composition-v2.html) |
| 编辑排版与信息样式 | [editorial-grid-euc-study-03](../studies/editorial-grid-euc-study-03.html)、[editorial-information-patterns-04](../studies/editorial-information-patterns-04.html) |
| 版式检查工具 | [grid-laboratory-phase-05](../studies/grid-laboratory-phase-05.html) |
| 动效方向 | [motion-directors-demo-01](../studies/motion-directors-demo-01.html) |
