"""Make hero + thumbnail images for project pages.

Given one or more source image paths, writes two outputs per input into an
``output/`` subdirectory next to the source:

  - ``{name}.png``           at 800 px long edge (hero / project page)
  - ``{name}-thumbnail.png`` at 400 px long edge (projects listing card)

Both outputs are lossless RGBA PNGs.

Usage:
    uv run make_thumbnails.py /path/to/image.png [more.png ...]
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from PIL import Image

HERO_LONG_EDGE = 800
THUMBNAIL_LONG_EDGE = 400


def resize_long_edge(img: Image.Image, target: int) -> Image.Image:
    """Return a copy of ``img`` resized so its longer edge equals ``target`` px.

    The aspect ratio is preserved. If the image is already small enough, an
    unscaled copy is returned.
    """
    w, h = img.size
    if max(w, h) <= target:
        return img.copy()
    new_size = (target, round(h * target / w)) if w >= h else (round(w * target / h), target)
    return img.resize(new_size, Image.LANCZOS)


def make_outputs(src: Path) -> tuple[Path, Path]:
    """Write the hero and thumbnail PNGs for ``src``, return their paths."""
    out_dir = src.parent / "output"
    out_dir.mkdir(exist_ok=True)

    with Image.open(src) as raw:
        img = raw.convert("RGBA")

    hero_path = out_dir / f"{src.stem}.png"
    resize_long_edge(img, HERO_LONG_EDGE).save(hero_path, "PNG", optimize=True)

    thumb_path = out_dir / f"{src.stem}-thumbnail.png"
    resize_long_edge(img, THUMBNAIL_LONG_EDGE).save(thumb_path, "PNG", optimize=True)

    return hero_path, thumb_path


def format_kb(n: int) -> str:
    """Format a byte count as a rounded KB string."""
    return f"{n / 1024:.0f} KB"


def main() -> int:
    """Parse CLI args and process each image."""
    parser = argparse.ArgumentParser(description=__doc__.split("\n", maxsplit=1)[0])
    parser.add_argument("images", nargs="+", type=Path, help="One or more source images.")
    args = parser.parse_args()

    print(f"{'source':<40} {'src':>10} {'800 px':>10} {'400 px':>10}")
    print("-" * 74)

    exit_code = 0
    for src in args.images:
        if not src.is_file():
            print(f"{src!s:<40}  MISSING", file=sys.stderr)
            exit_code = 1
            continue

        hero_path, thumb_path = make_outputs(src)
        print(
            f"{src!s:<40} "
            f"{format_kb(src.stat().st_size):>10} "
            f"{format_kb(hero_path.stat().st_size):>10} "
            f"{format_kb(thumb_path.stat().st_size):>10}",
        )

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
