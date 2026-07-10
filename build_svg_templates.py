#!/usr/bin/env python3
"""Build Andrew6rant-style profile SVG: ASCII bust + stats panel."""

from __future__ import annotations

import html
from pathlib import Path

from portrait_handcrafted import build_handcrafted_bust

OUT_DIR = Path(__file__).resolve().parent / "profile-svg"


def ascii_tspans(lines: list[str], x: int = 15, start_y: int = 30, line_height: int = 20) -> str:
    chunks = []
    for index, line in enumerate(lines):
        y = start_y + index * line_height
        chunks.append(f'<tspan x="{x}" y="{y}">{html.escape(line)}</tspan>')
    return "\n".join(chunks)


def stats_block(username: str, mode: str) -> str:
    if mode == "dark":
        fg = "#c9d1d9"
    else:
        fg = "#24292f"

    return f'''<text x="390" y="30" fill="{fg}">
<tspan x="390" y="30">{username}@uw</tspan> -———————————————————————————————————————————-—-
<tspan x="390" y="50" class="cc">. </tspan><tspan class="key">OS</tspan>:<tspan class="cc"> .............................. </tspan><tspan class="value">macOS, Linux</tspan>
<tspan x="390" y="70" class="cc">. </tspan><tspan class="key">School</tspan>:<tspan class="cc"> ........................... </tspan><tspan class="value">UW Seattle</tspan>
<tspan x="390" y="90" class="cc">. </tspan><tspan class="key">Major</tspan>:<tspan class="cc"> .......... </tspan><tspan class="value">Data Science + Economics</tspan>
<tspan x="390" y="110" class="cc">. </tspan><tspan class="key">Graduation</tspan>:<tspan class="cc"> ........................ </tspan><tspan class="value">June 2027</tspan>
<tspan x="390" y="130" class="cc">. </tspan>
<tspan x="390" y="150" class="cc">. </tspan><tspan class="key">Languages</tspan>.<tspan class="key">Programming</tspan>:<tspan class="cc"> ..... </tspan><tspan class="value">Python, Java, JavaScript, SQL, R</tspan>
<tspan x="390" y="170" class="cc">. </tspan><tspan class="key">Languages</tspan>.<tspan class="key">ML</tspan>:<tspan class="cc"> ................. </tspan><tspan class="value">TensorFlow, Scikit-learn, XGBoost</tspan>
<tspan x="390" y="190" class="cc">. </tspan><tspan class="key">Languages</tspan>.<tspan class="key">Web</tspan>:<tspan class="cc"> ................ </tspan><tspan class="value">React, Node.js, Svelte, React Native</tspan>
<tspan x="390" y="210" class="cc">. </tspan>
<tspan x="390" y="230" class="cc">. </tspan><tspan class="key">Focus</tspan>:<tspan class="cc"> ............... </tspan><tspan class="value">ML systems, sports AI, full-stack apps</tspan>
<tspan x="390" y="250" class="cc">. </tspan><tspan class="key">Building</tspan>:<tspan class="cc"> .......................... </tspan><tspan class="value">IsoCourt, Eat Together</tspan>
<tspan x="390" y="290">- Contact</tspan> -——————————————————————————————————————————————-—-
<tspan x="390" y="310" class="cc">. </tspan><tspan class="key">GitHub</tspan>:<tspan class="cc"> ................................ </tspan><tspan class="value">Navneethd8</tspan>
<tspan x="390" y="330" class="cc">. </tspan><tspan class="key">Portfolio</tspan>:<tspan class="cc"> ............................... </tspan><tspan class="value">navneethd8.github.io</tspan>
<tspan x="390" y="350" class="cc">. </tspan><tspan class="key">Location</tspan>:<tspan class="cc"> .............................. </tspan><tspan class="value">Seattle, WA</tspan>
<tspan x="390" y="390" class="cc">. </tspan>
<tspan x="390" y="410">- GitHub Stats</tspan> -—————————————————————————————————————————-—-
<tspan x="390" y="430" class="cc">. </tspan><tspan class="key">Repos</tspan>:<tspan class="cc" id="repo_data_dots"> .... </tspan><tspan class="value" id="repo_data">0</tspan> {{<tspan class="key">Contributed</tspan>: <tspan class="value" id="contrib_data">0</tspan>}} | <tspan class="key">Stars</tspan>:<tspan class="cc" id="star_data_dots"> ........... </tspan><tspan class="value" id="star_data">0</tspan>
<tspan x="390" y="450" class="cc">. </tspan><tspan class="key">Commits</tspan>:<tspan class="cc" id="commit_data_dots"> ................. </tspan><tspan class="value" id="commit_data">0</tspan> | <tspan class="key">Followers</tspan>:<tspan class="cc" id="follower_data_dots"> ....... </tspan><tspan class="value" id="follower_data">0</tspan>
<tspan x="390" y="470" class="cc">. </tspan><tspan class="key">Account Age</tspan>:<tspan class="cc" id="age_data_dots"> .................... </tspan><tspan class="value" id="age_data">0</tspan>
</text>'''


def build_svg(mode: str, ascii_lines: list[str]) -> str:
    if mode == "dark":
        ascii_fill = "#c9d1d9"
        bg = "#0d1117"
        key, value, cc, add, delete = "#ff7b72", "#79c0ff", "#8b949e", "#3fb950", "#f85149"
    else:
        ascii_fill = "#24292f"
        bg = "#f6f8fa"
        key, value, cc, add, delete = "#953800", "#0a3069", "#c2cfde", "#1a7f37", "#cf222e"

    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" font-family="ConsolasFallback,Consolas,Menlo,monospace" width="985px" height="530px" font-size="16px">
<style>
@font-face {{
src: local('Consolas'), local('Consolas Bold');
font-family: 'ConsolasFallback';
font-display: swap;
-webkit-size-adjust: 109%;
size-adjust: 109%;
}}
text, tspan {{ white-space: pre; }}
.key {{ fill: {key}; }}
.value {{ fill: {value}; }}
.cc {{ fill: {cc}; }}
.addColor {{ fill: {add}; }}
.delColor {{ fill: {delete}; }}
</style>
<rect width="985px" height="530px" fill="{bg}" rx="15"/>
<text x="15" y="30" fill="{ascii_fill}" class="ascii">
{ascii_tspans(ascii_lines)}
</text>
{stats_block("navneeth", mode)}
</svg>
'''


def main() -> None:
    lines = build_handcrafted_bust()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "light_mode.svg").write_text(build_svg("light", lines), encoding="utf-8")
    (OUT_DIR / "dark_mode.svg").write_text(build_svg("dark", lines), encoding="utf-8")
    print(f"Wrote templates to {OUT_DIR}")


if __name__ == "__main__":
    main()
