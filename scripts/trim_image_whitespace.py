#!/usr/bin/env python3
"""
Trim outer whitespace from an image.

Supports transparent borders and white/near-white borders.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageChops


def build_mask(img: Image.Image, white_threshold: int, alpha_threshold: int) -> Image.Image:
    rgb = img.convert("RGB")
    r, g, b = rgb.split()

    # Mark pixels as "content" if any RGB channel is sufficiently darker than white.
    r_mask = r.point(lambda v: 255 if v < (255 - white_threshold) else 0)
    g_mask = g.point(lambda v: 255 if v < (255 - white_threshold) else 0)
    b_mask = b.point(lambda v: 255 if v < (255 - white_threshold) else 0)
    non_white_mask = ImageChops.lighter(ImageChops.lighter(r_mask, g_mask), b_mask)

    alpha = img.convert("RGBA").split()[3]
    alpha_min, alpha_max = alpha.getextrema()

    # If the image actually contains transparency, include alpha-based content detection.
    # For fully opaque images, alpha-based masking would mark the full canvas as content.
    if alpha_min < 255 and alpha_max > 0:
        alpha_mask = alpha.point(lambda v: 255 if v > alpha_threshold else 0)
        return ImageChops.lighter(non_white_mask, alpha_mask)

    return non_white_mask


def trim_image(
    input_path: Path,
    output_path: Path,
    white_threshold: int,
    alpha_threshold: int,
    padding: int,
) -> tuple[tuple[int, int], tuple[int, int]]:
    img = Image.open(input_path)
    original_size = img.size
    mask = build_mask(img, white_threshold, alpha_threshold)
    bbox = mask.getbbox()

    if bbox is None:
        # No visible content detected; keep original image.
        output_path.parent.mkdir(parents=True, exist_ok=True)
        img.save(output_path)
        return original_size, original_size

    left, upper, right, lower = bbox
    left = max(0, left - padding)
    upper = max(0, upper - padding)
    right = min(img.width, right + padding)
    lower = min(img.height, lower + padding)

    cropped = img.crop((left, upper, right, lower))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    cropped.save(output_path)
    return original_size, cropped.size


def main() -> None:
    parser = argparse.ArgumentParser(description="Trim whitespace around image content.")
    parser.add_argument("input", type=Path, help="Input image path")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,
        help="Output image path (default: overwrite input)",
    )
    parser.add_argument(
        "--white-threshold",
        type=int,
        default=10,
        help="How close to white a pixel can be before considered whitespace (default: 10)",
    )
    parser.add_argument(
        "--alpha-threshold",
        type=int,
        default=8,
        help="Minimum alpha value considered visible content (default: 8)",
    )
    parser.add_argument(
        "--padding",
        type=int,
        default=0,
        help="Optional padding (in pixels) to keep around trimmed content (default: 0)",
    )
    args = parser.parse_args()

    output = args.output or args.input
    before, after = trim_image(
        args.input,
        output,
        white_threshold=args.white_threshold,
        alpha_threshold=args.alpha_threshold,
        padding=args.padding,
    )
    print(f"trimmed: {args.input} -> {output}")
    print(f"size: {before[0]}x{before[1]} -> {after[0]}x{after[1]}")


if __name__ == "__main__":
    main()
