"""Hand-stylized ASCII bust portrait (Andrew6rant style)."""

from __future__ import annotations

# Abstract face — no emoji box. Glasses hinted via ,####, brow bar.
# 25 lines × 34 cols. Structure follows Andrew6rant's organic face shading.
HANDCRAFTED_BUST: list[str] = [
    "          ,;;, ,|L|,~,            ",
    "       ,g@@l&$$@|,w$gy,           ",
    "      $@@@@@@@$$$MW$k             ",
    "     $$@@@B@@@@@$$g,$             ",
    "   g@lM*'||%@@$@@@L$&             ",
    "  @$&$F      ''T%M$@@@@@@@         ",
    " @@@@F            ']@@@@@$$@       ",
    " @@@$L    ,####,  |$@@$$l$@       ",
    " ]@@@@L,@@$@@L,l@$$$$$@@@         ",
    "  %$@@@$}',gg@|@@l@g@gg|l$&       ",
    "  ]@@@@@'\"*TTTT'F]Wl|||''\"$]@     ",
    "   $$@M$     ,#   ]gg,,,.r'$@     ",
    "    &$L      ' ,,,'T''`   $$L     ",
    "     lL       T\"||||!  `- l\"'     ",
    "     ' |      '||l||||\"|L| L`     ",
    "      ''  '|L++=*****\"\"*\"|| L|    ",
    "        |          ,,     |||F     ",
    "        '        |||||||| ||l$     ",
    "          !    '#\\         |l&    ",
    "           '!,#||\\    ||,||@M|    ",
    "            ||l&$@$$MT|||         ",
    "        |  |||l$ll|||||L          ",
    "   ,;y    ||||l||@|||l            ",
    " ,g$@      |||||||||| $g,         ",
    " $$@    |  |||||||||| |$@g        ",
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
