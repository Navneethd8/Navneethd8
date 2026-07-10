"""Original ASCII bust for Navneeth — Andrew6rant proportions, not his face."""

from __future__ import annotations

# 25 × 48 — match Andrew's silhouette balance:
# open face void, hair as a rim (not a solid hood), wide shoulders.
# Navneeth cues: short neat hair, glasses as a thin brow bar, soft smile,
# quilted jacket, diagonal strap. No emoji eyes / dash-eye Sith look.
HANDCRAFTED_BUST: list[str] = [
    "            ;;,,  ,;|g;~,,                      ",
    "         ,g@@@@@@l&$$$@|,w$$gy,                 ",
    "        $@@@@@@@@@@$@@@@@@@$$MW$k               ",
    "       $$@@@@@@B@@@@@@@@@@@$@$$g,$              ",
    "     g@llM**'''||%@@@@@$@@$@@@@@@L$&            ",
    "   @$&$F         ''T%M$@@@@@@@@@@$@$@           ",
    "  @@@@F              ']@@@@@@$$@$@@@@           ",
    "  @@@$L     ,------,  |$@@@$$l$@@@@$F           ",
    " ]@@@@L ,@@$ '----'  ,l@$$$$$$$$$@@@@@          ",
    "  %$@@@$}',,gg@||@@@@l@g@ggg|l$&$@@$            ",
    "  ]@@@@@'\"*~~~~~'F  ]Wl|||''\"'$]@@@@            ",
    "   $$@M$       ,#    ]gg,,,,,.r'$@$             ",
    "    &$L        ' ,, ,,,'T''`    $$L             ",
    "     lL         T\"||||!   `-    l\"'             ",
    "     ' |        '||l||||\"|L|  L `               ",
    "      ''   '|L++=*****\"\"*\"||` L|                ",
    "        |           ,,      |||F                ",
    "        '         |||||||| ||l$                 ",
    "          !      '#\\       |l&L                 ",
    "           '!,   #||\\  |||,||@M|L               ",
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
