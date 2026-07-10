"""Hand-stylized ASCII bust portrait (Andrew6rant style)."""

from __future__ import annotations

# Full-density 25×48 bust — same composition quality as Andrew6rant.
# Pure abstract shading. No emoji eyes / robot face box.
HANDCRAFTED_BUST: list[str] = [
    "            ;;,, ,;,|g;~,,                      ",
    "         ,g@@@@@@l&$$$@|,w$$@gy,                ",
    "        $@@@@@@@@@@$@@@@@@@@$$MW$k              ",
    "       $$@@@@@@B@@@@@@@@@@@@@$@$$g,$            ",
    "     g@llM**'''||%@@@@@$@@$@@@@@@@L$&           ",
    "   @$&$F         ''T%M$@@@@@@@@@@@$@$@          ",
    "  @@@@F              ']@@@@@@$$@$@@@@           ",
    "  @@@$L               |$@@@$$l$@@@@$F           ",
    " ]@@@@L ,@@$@@@@L  ,l@$$$$$$$$$@@@@@            ",
    "  %$@@@$}',,gg@||@@@@l@g@ggg|l$&$@@$            ",
    "  ]@@@@@'\"*TTTTT'F  ]Wl|||''\"'$]@@@@            ",
    "   $$@M$       ,#    ]gg,,,,,.r'$@$             ",
    "    &$L        ' ,, ,,,'T''`    $$L             ",
    "     lL         T\"||||!   `-    l\"'             ",
    "     ' |        '||l||||\"|L|  L `               ",
    "      ''   '|L++=*****\"\"*\"||` L|                ",
    "        |           ,,      |||F                ",
    "        '         |||||||| ||l$                 ",
    "          !                |l&L                 ",
    "           '!,       |||,||@M|L                 ",
    "            ||l&$@$$@$$$@$MT|||                 ",
    "         |    |||lll$$llll|||||L                ",
    "    ,;y@        ||||||l||@|||||l                ",
    ",g$@$$$@         |||||||||||||||| $g,           ",
    "$$$$$$$$@    |    |||||||||||||| |$$@g          ",
]

CANVAS_WIDTH = 48
CANVAS_HEIGHT = 25


def build_handcrafted_bust(
    canvas_width: int = CANVAS_WIDTH,
    canvas_height: int = CANVAS_HEIGHT,
) -> list[str]:
    lines = [line.ljust(canvas_width)[:canvas_width] for line in HANDCRAFTED_BUST]
    while len(lines) < canvas_height:
        lines.append(" " * canvas_width)
    return lines[:canvas_height]
