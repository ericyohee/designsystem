#!/usr/bin/env python3
"""Generate core/tokens.css and core/tokens.md from core/tokens.json.

Usage: python3 scripts/build_tokens.py [--check]
"""
import json
import sys
from pathlib import Path

CORE = Path(__file__).resolve().parent.parent / "core"
HEADER = "由 scripts/build_tokens.py 从 tokens.json 生成，不要手动修改。"


def build_css(tokens):
    lines = [f"/* {HEADER} */", ":root {"]
    for group in ("color", "font"):
        for name, token in tokens[group].items():
            lines.append(f"  --gk-{group}-{name}: {token['value']}; /* {token['status']} */")
    lines.append("}")
    return "\n".join(lines) + "\n"


def build_md(tokens):
    status = tokens["meta"]["status"]
    out = [f"<!-- {HEADER} -->", "", "# Geniotek 标准值清单", ""]
    out += [f"- `{key}`：{text}" for key, text in status.items()]
    out += ["", "## 颜色", "", "| 名称 | 色值 | 状态 | 用在哪 | 不要这样用 |", "| --- | --- | --- | --- | --- |"]
    for name, t in tokens["color"].items():
        out.append(f"| {name} | `{t['value']}` | {t['status']} | {t['use']} | {t['avoid']} |")
    out += ["", "## 字体", "", "| 名称 | 字体 | 字重 | 宽度 | 状态 | 用在哪 | 不要这样用 |", "| --- | --- | --- | --- | --- | --- | --- |"]
    for name, t in tokens["font"].items():
        family = t["value"].split(",")[0].strip('"')
        out.append(f"| {name} | {family} | {t['weight']} | {t['width']} | {t['status']} | {t['use']} | {t['avoid']} |")
    return "\n".join(out) + "\n"


def main():
    tokens = json.loads((CORE / "tokens.json").read_text(encoding="utf-8"))
    outputs = {"tokens.css": build_css(tokens), "tokens.md": build_md(tokens)}
    if "--check" in sys.argv:
        stale = [n for n, text in outputs.items()
                 if not (CORE / n).exists() or (CORE / n).read_text(encoding="utf-8") != text]
        if stale:
            sys.exit(f"过期，需要重新生成: {', '.join(stale)}")
        return
    for name, text in outputs.items():
        (CORE / name).write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
