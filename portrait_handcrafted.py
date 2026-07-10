"""Hand-stylized ASCII bust portrait (Andrew6rant style)."""

from __future__ import annotations

# 25 lines × 34 cols — fits left panel without overlapping stats at x=390.
# Based on navneeth_dhamotharan.jpeg: glasses, short hair, warm smile, puffer jacket.
HANDCRAFTED_BUST: list[str] = [
    "          ,;,, ,|L|,~,            ",
    "       ,g@@l&$$@|,w$gy,           ",
    "      $@@@@@@@$$$MW$k             ",
    "     $$@@@B@@@@@$$g,$             ",
    "   g@lM*'||%@@$@@@L$&            ",
    "  @$F    .---------.   ''T%M      ",
    " @@F    |  o    o   |      ]@@    ",
    " @L     |    ~~     |       |$@   ",
    " ]L      '-----------'    ,l@$    ",
    "  %$}   *============*  ]Wl||    ",
    "  ]@'\"    .+------+.     \"|L|     ",
    "   M$      [#||#]         ]gg,     ",
    "   &L     -========-     ,,'T      ",
    "    L      |||||||        `-       ",
    "    ' |    |||||||        \"|       ",
    "     ''    +++++++****\"\"*|         ",
    "       |           ,,       |       ",
    "       '         ||||||   ||       ",
    "         !      '#\\         |      ",
    "          '!,  #||\\     ||,|      ",
    "           ||l&$@$$MT|||           ",
    "        |  |||l$ll|||||L           ",
    "   ,;y     ||||l||@|||l            ",
    " ,g$@       |||||||||| $g,          ",
    " $$@     |  |||||||||| |$@         ",
]

CANVAS_WIDTH = 34
CANVAS_HEIGHT = 25


def build_handcrafted_bust(
    canvas_width: int = CANVAS_WIDTH,
    canvas_height: int = CANVAS_HEIGHT,
) -> list[str]:
    lines = [line.ljust(canvas_width)[:canvas_width] for line in HANDCRAFTED_BUST]
    while len(lines) < canvas_height:
        lines.append(" " * canvas_width)
    return lines[:canvas_height]
