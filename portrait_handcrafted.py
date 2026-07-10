"""Hand-stylized ASCII bust portrait (Andrew6rant style)."""

from __future__ import annotations

# 25 lines — matches Andrew6rant SVG layout (y=30..510, 20px line height).
HANDCRAFTED_BUST: list[str] = [
    "        ,;;,, ,;|L|,~,,",
    "     ,l@@@@@@l&$$$$@|,w$$@gy,",
    "    $@@@@@@@@@@$@@@@@@@@$$MW$k",
    "   $$@@@@@@B@@@@@@@@@@@@@$@$$g,$",
    " g@llM**'''||%@@@@@$@@$@@@@@@@L$&",
    " @$&$F     .---------.    ''T%M$@@@@@@@@@",
    " @@@@F     |  o    o   |       ']@@@@@@$$@",
    " @@@$L     |     __    |        |$@@@$$l$@",
    " ]@@@@L      '-----------'     ,l@$$$$$$$$@@",
    " %$@@@$}   ,#|||||||||#,',@@@@l@g@ggg|l$&@",
    " ]@@@@@'\"*==============*' ]Wl|||''\"'$]@@@@",
    "  $$@M$       [#||#]          ]gg,,,.r'$@$",
    "   &$L        |||||||        ,,,'T''`  $$L",
    "    lL         ||||||          `-   l\"'",
    "    ' |       /||||||||\\        \"|L|  L `",
    "     ''      '|++++++++=****\"\"*||` L|",
    "       |              ,,          |||F",
    "       '            ||||||||||  ||l$",
    "         !       '#\\            |l&L",
    "          '!,    #||\\       |||,||@M|L",
    "           ||l&$@$$@$$$@$MT|||",
    "        |    |||lll$$llll|||||L",
    "   ,;y@        ||||||l||@|||||l",
    ",g$@$$$@         |||||||||||||||| $g,",
    "$$$$$$$$@    |    |||||||||||||| |$$@g",
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
