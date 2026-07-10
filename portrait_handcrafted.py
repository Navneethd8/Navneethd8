"""Hand-stylized ASCII bust portrait (Andrew6rant style)."""

from __future__ import annotations

# Stylized bust based on navneeth_dhamotharan.jpeg:
# rectangular glasses, short dark hair, gentle smile, puffer jacket, shoulder strap.
HANDCRAFTED_BUST: list[str] = [
    "            ,;;,, ,;|L|,~,,                   ",
    "         ,l@@@@@@l&$$$$@|,w$$@gy,             ",
    "        $@@@@@@@@@@$@@@@@@@@$$MW$k             ",
    "       $$@@@@@@B@@@@@@@@@@@@@$@$$g,$           ",
    "     g@llM**'''||%@@@@@$@@$@@@@@@@L$&         ",
    "    @$&$F     .---------.    ''T%M$@@@@@@@@    ",
    "   @@@@F     |  o    o   |       ']@@@@@@$$    ",
    "   @@@$L     |     __    |        |$@@@$$l$    ",
    "  ]@@@@L      '-----------'     ,l@$$$$$$$$@    ",
    "   %$@@@$}   ,#|||||||||#,',@@@@l@g@ggg|l$&    ",
    "   ]@@@@@'\"*==============*' ]Wl|||''\"'$]@@@    ",
    "    $$@M$       [#||#]          ]gg,,,.r'$@     ",
    "     &$L        |||||||        ,,,'T''`  $$     ",
    "      lL         ||||||          `-   l\"'      ",
    "      ' |       /||||||||\\        \"|L| L `     ",
    "       ''      '|++++++++=****\"\"*||` L|       ",
    "         |              ,,          |||F       ",
    "         '            ||||||||||  ||l$         ",
    "           !       '#\\            |l&L        ",
    "            '!,    #||\\       |||,||@M|L       ",
    "             ||l&$@$$@$$$@$MT|||              ",
    "         |    |||lll$$llll|||||L               ",
    "    ,;y@        ||||||l||@|||||l               ",
    "                  |||||||||||||               ",
]


def build_handcrafted_bust(
    canvas_width: int = 48,
    canvas_height: int = 24,
) -> list[str]:
    lines = [line.ljust(canvas_width)[:canvas_width] for line in HANDCRAFTED_BUST]
    while len(lines) < canvas_height:
        lines.append(" " * canvas_width)
    return lines[:canvas_height]
