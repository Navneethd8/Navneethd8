"""Photo-derived ASCII bust of Navneeth with landmark-guided glasses."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageFilter, ImageOps

CANVAS_WIDTH = 48
CANVAS_HEIGHT = 25
PHOTO_CUTOUT = Path(__file__).resolve().parent / "assets" / "navneeth-cutout.png"
TONES = " .,:;lLGM&$@"

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

    def sparse_ink(crop: Image.Image, size: tuple[int, int], threshold: int) -> Image.Image:
        rgb = crop.convert("RGB")
        gray = ImageOps.grayscale(rgb)
        ycbcr = rgb.convert("YCbCr")
        alpha = crop.getchannel("A")
        edges = gray.filter(ImageFilter.FIND_EDGES)
        ink = Image.new("L", crop.size)

        values: list[int] = []
        for gray_value, (_, cb, cr), alpha_value, edge_value in zip(
            gray.getdata(),
            ycbcr.getdata(),
            alpha.getdata(),
            edges.getdata(),
        ):
            if alpha_value < 40:
                values.append(0)
                continue
            is_skin = (
                75 < cb < 135
                and 130 < cr < 180
                and gray_value > 45
            )
            darkness = 0 if is_skin else max(0, min(255, (threshold - gray_value) * 3))
            edge_ink = int(edge_value * 0.55)
            values.append(max(darkness, edge_ink))

        ink.putdata(values)
        return ink.resize(size, Image.Resampling.LANCZOS)

    # Give the face 19 rows instead of compressing the entire subject into one
    # sample.  The skin mask leaves face color to the SVG background.
    head = sparse_ink(source.crop((45, 0, 275, 220)), (36, 19), threshold=105)
    torso = sparse_ink(source.crop((0, 155, 320, 325)), (38, 6), threshold=115)
    sample = Image.new("L", (CANVAS_WIDTH, CANVAS_HEIGHT))
    sample.paste(head, (4, 0))
    sample.paste(torso, (0, 19))

    lines: list[str] = []
    for y in range(CANVAS_HEIGHT):
        chars: list[str] = []
        for x in range(CANVAS_WIDTH):
            value = sample.getpixel((x, y))
            if value < 12:
                chars.append(" ")
                continue
            index = min(len(TONES) - 1, int(value / 255 * (len(TONES) - 1)))
            chars.append(TONES[index])
        lines.append("".join(chars))

    # Clarify features without filling the skin region.  The pupils share one
    # literal row, while the frames use organic density instead of box glyphs.
    lines[7] = _overlay(lines[7], 7, ",g@@@L ,l@@L--L@@l, L@@@g,")
    lines[8] = _overlay(lines[8], 8, "'$@@@l    .    .    l@@@$'")
    lines[9] = _overlay(lines[9], 18, ",||,")
    lines[10] = _overlay(lines[10], 19, "||")
    lines[12] = _overlay(lines[12], 15, "',------,'")

    # Preserve the clean outer jaw border while leaving its interior blank.
    for row, left, right in (
        (11, 8, 34),
        (12, 9, 33),
        (13, 10, 32),
        (14, 11, 31),
        (15, 12, 30),
    ):
        chars = list(lines[row])
        chars[left] = "L"
        chars[right] = "L"
        lines[row] = "".join(chars)
    lines[16] = _overlay(lines[16], 14, "'----------'")
    return lines


def build_handcrafted_bust(
    canvas_width: int = CANVAS_WIDTH,
    canvas_height: int = CANVAS_HEIGHT,
) -> list[str]:
    return _fit(_photo_density_lines(), canvas_width, canvas_height)
