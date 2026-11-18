# Geniotek 视觉系统

Geniotek 品牌标准的总入口。做任何对外或对内的品牌呈现之前，从这里找到对应的规范。

在线预览：<https://ericyohee.github.io/designsystem/>

## 你在做什么？

| 场景 | 先读 | 再读 |
| --- | --- | --- |
| 网页（Framer） | [品牌底座](core/brand.md) | [网页](scenarios/web.md) |
| 社交媒体 | [品牌底座](core/brand.md) | [社交媒体](scenarios/social.md) |
| 广告投放 | [品牌底座](core/brand.md) | [广告](scenarios/ads.md) |
| 内部软件 | [品牌底座](core/brand.md) | [内部软件](scenarios/internal-software.md) |
| 视频 | [品牌底座](core/brand.md) | [视频](scenarios/video.md) |

用 AI 工具（Codex 等）工作时，让它先读 [AGENTS.md](AGENTS.md)。

## 仓库里有什么

| 位置 | 内容 |
| --- | --- |
| `core/tokens.json` | 颜色和字体的唯一数值来源 |
| `core/tokens.md` / `core/tokens.css` | 由上面自动生成的清单（给人看 / 给网页用） |
| `core/brand.md` | 所有场景共用的规则 |
| `scenarios/` | 各场景的规范。网页已有内容；其余四个目前是框架，栏目标着“待定”的还没有规则 |
| `assets/` | 官方标志 |
| `index.html`、`studies/` | 网页方向的研究与试验页，是规范的依据，不是规范本身 |

## 修改标准值

只改 `core/tokens.json`，然后运行：

```bash
python3 scripts/build_tokens.py
```

每个值都有状态：`frozen`（已定稿）、`candidate`（暂用，可能调整）或 `planned`（确定要有，但数值还没定，不能用）。
