"""Instagram collage builders for the MY TYPE OUTFIT series.

Templates:
  1. hero_poster  - one outfit, bold title header, 9:16 (reel cover / single post)
  2. grid_collage - 4 outfits in a 2x2 grid, 1:1 (feed post)
  3. outfit_card  - one outfit + outfit name, 4:5 (carousel slide)

Tested 2026-10-10 with PIL. Needs: pillow.
"""
from PIL import Image, ImageDraw, ImageFont, ImageOps
import os

WHITE = (255, 255, 255)
INK = (15, 15, 15)
GREY = (120, 120, 120)
DIVIDER = (225, 220, 212)

_FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
_FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def _font(bold, size):
    try:
        return ImageFont.truetype(_FONT_BOLD if bold else _FONT_REG, size)
    except OSError:
        return ImageFont.load_default()


def _fit(img_path, w, h):
    im = Image.open(img_path).convert("RGB")
    return ImageOps.fit(im, (w, h), Image.LANCZOS)


def _header(card, title, subtitle, W):
    d = ImageDraw.Draw(card)
    hf, sf = _font(True, 72), _font(True, 34)
    hb = d.textbbox((0, 0), title, font=hf)
    d.text(((W - (hb[2] - hb[0])) / 2, 56), title, fill=INK, font=hf)
    if subtitle:
        sb = d.textbbox((0, 0), subtitle, font=sf)
        d.text(((W - (sb[2] - sb[0])) / 2, 150), subtitle, fill=GREY, font=sf)
    return 235 if subtitle else 170


def hero_poster(img_path, out_path, title="MY TYPE OUTFIT", subtitle=""):
    """Single outfit poster, 1080x1920 (9:16)."""
    W, H = 1080, 1920
    card = Image.new("RGB", (W, H), WHITE)
    y = _header(card, title, subtitle, W)
    body_h = H - y - 60
    card.paste(_fit(img_path, W - 120, body_h), (60, y))
    card.save(out_path, quality=92)
    return out_path


def outfit_card(img_path, out_path, title="MY TYPE OUTFIT", subtitle=""):
    """Single outfit card, 1080x1350 (4:5) — carousel slide."""
    W, H = 1080, 1350
    card = Image.new("RGB", (W, H), WHITE)
    y = _header(card, title, subtitle, W)
    body_h = H - y - 40
    card.paste(_fit(img_path, W - 120, body_h), (60, y))
    card.save(out_path, quality=92)
    return out_path


def grid_collage(img_paths, out_path, title="MY TYPE OUTFIT", cols=2):
    """2x2 grid of outfits, 1080x1080 (1:1). Pass exactly 4 image paths."""
    assert len(img_paths) == 4, "grid_collage needs exactly 4 images"
    W = H = 1080
    cell = W // cols
    grid = Image.new("RGB", (W, H), WHITE)
    for i, p in enumerate(img_paths):
        grid.paste(_fit(p, cell - 8, cell - 8), ((i % cols) * cell + 4, (i // cols) * cell + 4))
    d = ImageDraw.Draw(grid)
    d.line([(cell, 0), (cell, H)], fill=DIVIDER, width=3)
    d.line([(0, cell), (W, cell)], fill=DIVIDER, width=3)
    # title strip at bottom
    strip_h = 110
    strip = Image.new("RGB", (W, strip_h), WHITE)
    d2 = ImageDraw.Draw(strip)
    f = _font(True, 54)
    bb = d2.textbbox((0, 0), title, font=f)
    d2.text(((W - (bb[2] - bb[0])) / 2, 28), title, fill=INK, font=f)
    final = Image.new("RGB", (W, H + strip_h), WHITE)
    final.paste(grid, (0, 0))
    final.paste(strip, (0, H))
    final.save(out_path, quality=92)
    return out_path


if __name__ == "__main__":
    print("collage.py loaded — hero_poster, outfit_card, grid_collage ready.")
