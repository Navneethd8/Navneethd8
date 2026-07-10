"""Original ASCII bust for Navneeth — Andrew6rant layout, not his art."""

from __future__ import annotations

# 25 × 48 — same panel density as Andrew6rant.
# Distinct from Andrew: denser short hair, glasses as thin brow bars in the
# face void (no o/emoji eyes), soft smile, quilted jacket, diagonal strap.
HANDCRAFTED_BUST: list[str] = [
    "             ,;;;;,,                            ",
    "          ,g@@@@@@@@gy,                         ",
    "        g@@@@@@@@@@@@@@$k                       ",
    "       $@@@@@@@@@@@@@@@@@$                      ",
    "      $$@@@@B@@@@@@@@B@@@@$                     ",
    "     @$&$F    ''''''    F$&$@                   ",
    "    @@@@F   ----  ----   F@@@@                  ",
    "    @@@$L                L$@@@                  ",
    "   ]@@@@L  ,,,,,,,,,,,.  L@@@@]                 ",
    "    %$@@@  '\"*~~~~*\"'   @@@$%                   ",
    "    ]@@@@@   ,,,,,,.    @@@@@]                  ",
    "     $$@M$    \\___/     $M@$$                   ",
    "      &$L     |||||      L$&                    ",
    "       lL    |||||||     Ll                     ",
    "       ' |  |||||||||   | '                     ",
    "        '' '|+++++++|' ''                       ",
    "          |    #\\     |                         ",
    "          '  |||||||  '                         ",
    "            ! #||||# !                          ",
    "             '!,||,!'                           ",
    "           ||l&$$$$&l||                         ",
    "        |  |||ll$$ll|||  |                      ",
    "   ,;y@      ||||||||      @y;,                 ",
    ",g$@$$$@      ||||||      @$$$@g,               ",
    "$$$$$$$$@  |   ||||   |  @$$$$$$$$              ",
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
