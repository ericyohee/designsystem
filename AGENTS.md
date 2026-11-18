# Geniotek 视觉系统：给 AI 的工作说明

这个仓库是 Geniotek 的品牌标准。你产出任何带 Geniotek 品牌的内容前，按下面的顺序读取。

## 读取顺序

1. [core/brand.md](core/brand.md)：通用规则。
2. [core/tokens.json](core/tokens.json)：颜色和字体的唯一数值来源。
3. 与任务对应的一份场景规范：

| 任务 | 文件 |
| --- | --- |
| 网页、Framer 页面 | [scenarios/web.md](scenarios/web.md) |
| 社交媒体图文 | [scenarios/social.md](scenarios/social.md) |
| 广告素材、落地页 | [scenarios/ads.md](scenarios/ads.md) |
| 内部软件界面 | [scenarios/internal-software.md](scenarios/internal-software.md) |
| 视频、动效 | [scenarios/video.md](scenarios/video.md) |

任务不属于以上任何一类时，只用 `core/` 里的规则，并告诉用户这个场景还没有专门规范。

## 必须遵守

- 颜色和字体只用 `core/tokens.json` 里的值。需要清单里没有的值时，先问用户，不要自己新增。
- `status` 为 `candidate` 的值可以使用，但要在交付时说明用了哪些候选值。
- `core/brand.md` 里“还没批准”的内容不能当作标准，也不能写成已定稿。
- 标志只用 `assets/geniotek-primary-logo.svg`。
- 不编造数据、工厂能力、认证或测试结果。示例数据要标明是示例。
- 场景规范里标着“尚未定义”的内容，不要自行补全成规则；按通用规则做，并把你做的选择列给用户确认。

## 交付前自查

- 每个颜色都能说出它的职责吗？
- 正文大小的白字有没有放在 `brand` 色上？（不允许）
- Display 字体是否只用在简短的品牌主张上？
- Mono 字体是否只用在真实的技术数值和编号上？
- 关键信息在窄屏或放大后是否仍然完整？

## 修改这个仓库

- 标准值只改 `core/tokens.json`，然后运行 `python3 scripts/build_tokens.py`。不要手改 `tokens.css` 和 `tokens.md`。
- `index.html` 和 `studies/` 是研究记录。新的研究结论要在通过后写入 `core/` 或 `scenarios/`，否则它不算标准。
