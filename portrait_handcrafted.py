"""ASCII bust — keep Andrew's dense face technique; retune cues for Navneeth."""

from __future__ import annotations

# Technique from Andrew6rant (do not strip this):
#   - dense hair rim + open face void
#   - face is NOT blank: mid-face uses ,@@$ / gg@|| / Wl||| texture
#   - mouth band uses '"*....'F style shading
#   - wide shoulder base
#
# Navneeth retunes only a few face-zone glyphs:
#   - glasses brow .======. woven into line 8 void
#   - lens dots .  . kept inside dense line 9 (not an empty box)
#   - smile ~~~~~ instead of TTTTT on the mouth band
#   - short-hair crown (slightly less wispy top)
#   - bag strap #\\ on torso
HANDCRAFTED_BUST: list[str] = [
    "             ,;;,, ,;||,~,,                     ",
    "         ,g@@@@@@l&$$$@|,w$$@gy,                ",
    "        $@@@@@@@@@@$@@@@@@@@$$MW$k              ",
    "       $$@@@@@@B@@@@@@@@@@@@@$@$$g,$            ",
    "     g@llM**'''||%@@@@@$@@$@@@@@@@L$&           ",
    "   @$&$F         ''T%M$@@@@@@@@@@@$@$@          ",
    "  @@@@F              ']@@@@@@$$@$@@@@           ",
    "  @@@$L    .======.   |$@@@$$l$@@@@$F           ",
    " ]@@@@L ,@@$ .  . L  ,l@$$$$$$$$@@@@@           ",
    "  %$@@@$}',,=======@@@@l@g@ggg|l$&$@@$          ",
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
