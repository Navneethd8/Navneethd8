"""ASCII bust — keep Andrew's dense face technique; retune cues for Navneeth."""

from __future__ import annotations

# Technique from Andrew6rant (do not strip this):
#   - dense hair rim + open face void
#   - face is NOT blank: mid-face uses ,@@$ / gg@|| / Wl||| texture
#   - mouth band uses '"*....'F style shading
#   - wide shoulder base
#   - jaw/chin has a tapering border (even when clean-shaven)
#
# Navneeth retunes:
#   - hair: short neat crown, slight right sweep — textured @/$ mix
#   - glasses brow .======. ; eyes .  . on the SAME line, even spacing
#   - smile ~~~~~ instead of TTTTT
#   - clean-shaven chin (open center) but KEEP jaw border outline
#   - bag strap #\\ on torso
#   - from row 5 down: trim 4 trailing content chars
HANDCRAFTED_BUST: list[str] = [
    "             ,g@@@@@$gy,                        ",
    "          ,@@@@@l&$$$@|@@@,                     ",
    "         $@@@@@@@$@@@@@@@$$MW                   ",
    "        $$@@@@B@@@@@@@B@@@@$$g                  ",
    "      g@llM**'''||%@@@@@$@@@@@@                 ",
    "   @$&$F         ''T%M$@@@@@@@@@@@              ",
    "  @@@@F              ']@@@@@@$$@$               ",
    "  @@@$L    .======.   |$@@@$$l$@@               ",
    " ]@@@@L ,@@$  .  .  ,l@$$$$$$$$@                ",
    "  %$@@@$}',,=======@@@@l@g@ggg|l$&              ",
    "  ]@@@@@'\"*~~~~~'F  ]Wl|||''\"'$]                ",
    "   $$@M$              ]gg,,,,,.r                ",
    "    &$L        '          `    $$L              ",
    "     lL         ',,,,,,,'      l\"'              ",
    "     ' |                       L `              ",
    "      ''   '|L--------L|'    L|                 ",
    "        |           ,,                          ",
    "        '         ||||||||                      ",
    "          !      '#\\                           ",
    "           '!,   #||\\  |||,|||                  ",
    "            ||l&$@$$@$$$@$M                     ",
    "         |    |||lll$$llll|||                   ",
    "    ,;y@        ||||||l||@|||                   ",
    ",g$@$$$@         ||||||||||||||||               ",
    "$$$$$$$$@    |    |||||||||||||| |              ",
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
