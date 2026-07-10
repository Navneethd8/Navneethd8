"""Photo-derived ASCII bust of Navneeth with landmark-guided glasses."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageOps

CANVAS_WIDTH = 48
CANVAS_HEIGHT = 25
PHOTO_CUTOUT = Path(__file__).resolve().parent / "assets" / "navneeth-cutout.png"
TONES = "@$&MGLl;:,. "

# Coordinates are measured from navneeth_dhamotharan.jpeg after detecting the
# face at (248, 316, 220, 220) and eyes at y=404.  Keeping these explicit
# prevents later glyph edits from moving facial features independently.
LANDMARKS = {
    "hair_top": (14, 0),
    "hair_left": (8, 3),
    "hair_right": (31, 4),
    "left_eye": (15, 7),
    "right_eye": (23, 7),
    "nose": (20, 10),
    "mouth": (20, 11),
    "chin": (20, 14),
    "left_shoulder": (2, 24),
    "right_shoulder": (39, 24),
}

OUTLINE_BUST: list[str] = [
    "              _________                         ",
    "           __/         \\__                      ",
    "         _/               \\_                    ",
    "        /                   \\                   ",
    "       |      _________      |                  ",
    "      (|     /         \\     |)                 ",
    "      (|    +----++----+     |)                 ",
    "      (|    | .  || .  |     |)                 ",
    "       |    +----++----+     |                  ",
    "       |          |          |                  ",
    "        \\         |         /                   ",
    "        |        -----      |                   ",
    "         \\                 /                    ",
    "          \\               /                     ",
    "            \\___________/                       ",
    "              |       |                         ",
    "              |   /   |                         ",
    "              |  /    |                         ",
    "          ____| /     |____                     ",
    "       __/|||||/|||||||||||\\__                  ",
    "    __/|||||||||||||||||||||||\\__               ",
    "  _/||||||||||||||||||||||||||||\\_              ",
    " /|||||||||||||||||||||||||||||||||\\             ",
    "/|||||||||||||||||||||||||||||||||||\\            ",
    "||||||||||||||||||||||||||||||||||||||            ",
]

def _fit(lines: list[str], width: int, height: int) -> list[str]:
    fitted = [line.ljust(width)[:width] for line in lines]
    while len(fitted) < height:
        fitted.append(" " * width)
    return fitted[:height]


def build_outline_bust(
    canvas_width: int = CANVAS_WIDTH,
    canvas_height: int = CANVAS_HEIGHT,
) -> list[str]:
    return _fit(OUTLINE_BUST, canvas_width, canvas_height)


def _overlay(line: str, start: int, text: str) -> str:
    chars = list(line)
    chars[start : start + len(text)] = text
    return "".join(chars)


def _photo_density_lines() -> list[str]:
    if not PHOTO_CUTOUT.exists():
        raise FileNotFoundError(f"Missing portrait cutout: {PHOTO_CUTOUT}")

    source = Image.open(PHOTO_CUTOUT).convert("RGBA")
    # Two crops retain more facial samples than squeezing the entire torso into
    # 25 rows.  Their overlap is the high jacket collar visible in the photo.
    head = source.crop((55, 4, 265, 190)).resize(
        (34, 17),
        Image.Resampling.LANCZOS,
    )
    torso = source.crop((0, 155, 320, 325)).resize(
        (37, 8),
        Image.Resampling.LANCZOS,
    )

    sample = Image.new("RGBA", (CANVAS_WIDTH, CANVAS_HEIGHT), (255, 255, 255, 0))
    sample.alpha_composite(head, (4, 0))
    sample.alpha_composite(torso, (0, 17))

    composite = Image.new("RGBA", sample.size, "white")
    composite.alpha_composite(sample)
    gray = ImageOps.autocontrast(ImageOps.grayscale(composite), cutoff=1)
    alpha = sample.getchannel("A")

    lines: list[str] = []
    for y in range(CANVAS_HEIGHT):
        chars: list[str] = []
        for x in range(CANVAS_WIDTH):
            if alpha.getpixel((x, y)) < 32:
                chars.append(" ")
                continue
            value = (gray.getpixel((x, y)) / 255) ** 0.9
            index = min(len(TONES) - 1, int(value * (len(TONES) - 1)))
            chars.append(TONES[index])
        lines.append("".join(chars))

    # The actual glasses are the defining landmark but lose their frame during
    # 34×17 sampling.  Reinforce only that edge, preserving the photographed
    # hair, face shading, jaw, smile, collar, and body.
    lines[7] = _overlay(lines[7], 9, ",&$G|l@&l|--|l@&l|G@@@&")
    lines[8] = _overlay(lines[8], 9, ",&$G'&&$'    '$&&'MM$@@&")
    return lines


def build_handcrafted_bust(
    canvas_width: int = CANVAS_WIDTH,
    canvas_height: int = CANVAS_HEIGHT,
) -> list[str]:
    return _fit(_photo_density_lines(), canvas_width, canvas_height)
