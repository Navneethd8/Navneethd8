"""Hand-stylized ASCII bust portrait for Navneeth (Andrew6rant layout, original art)."""

from __future__ import annotations

# Original 25×48 bust — same panel density as Andrew6rant, not his face.
# From navneeth_dhamotharan.jpeg: short hair, rectangular glasses,
# closed smile, quilted puffer, diagonal strap.
HANDCRAFTED_BUST: list[str] = [
    "             ,;;,,,,;;,                         ",
    "          ,g@@@@@@@@@@gy,                       ",
    "        g@@@@@@@@@@@@@@@$k                      ",
    "       $@@@@@@@@@@@@@@@@@@$                     ",
    "      $$@@@@B@@@@@@@@B@@@@$$                    ",
    "     @$&$F   ''''''''   F$&$@                   ",
    "    @@@@F  .============.  F@@@@                ",
    "    @@@$L |   .      .    | L$@@@               ",
    "   ]@@@@L |               | L@@@@]              ",
    "    %$@@@  '============='  @@@$%               ",
    "    ]@@@@@   ,,,,,,,,,,.   @@@@@]               ",
    "     $$@M$    \\_______/    $M@$$                ",
    "      &$L      |||||||      L$&                 ",
    "       lL     |||||||||     Ll                  ",
    "       ' |   |||||||||||   | '                  ",
    "        ''  '|+++++++++|  ''                    ",
    "          |     ,#,      |                      ",
    "          '   |||||||    '                      ",
    "            !  #||||#   !                       ",
    "             '!,||||,!'                         ",
    "           ||l&$$$$$$&l||                       ",
    "        |  |||lll$$lll|||  |                    ",
    "   ,;y@       ||||||||||       @y;,             ",
    ",g$@$$$@       ||||||||       @$$$@g,           ",
    "$$$$$$$$@  |    ||||||    |  @$$$$$$$$          ",
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
