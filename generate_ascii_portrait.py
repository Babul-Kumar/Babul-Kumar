import os
from PIL import Image, ImageEnhance, ImageFilter

# Load processed portrait
img_path = "assets/portrait_processed.jpg"
im = Image.open(img_path).convert("L")

# Resize to terminal grid resolution (e.g. 52 columns x 48 rows)
cols = 48
rows = 44
im_small = im.resize((cols, rows), Image.Resampling.LANCZOS)

# Enhance contrast for sharp terminal character mapping
enhancer = ImageEnhance.Contrast(im_small)
im_contrasted = enhancer.enhance(1.3)

# Character ramps by density
# Palette: space to dense
chars = " .·:+*=%#@"

ascii_lines = []
for y in range(rows):
    line = []
    for x in range(cols):
        pixel = im_contrasted.getpixel((x, y))
        # Non-linear mapping to create natural gaps in dark background
        if pixel < 25:
            char = " "
        elif pixel < 55:
            char = "·" if (x + y) % 3 == 0 else " "
        else:
            idx = int((pixel / 255.0) * (len(chars) - 1))
            char = chars[idx]
        line.append(char)
    ascii_lines.append("".join(line))

print(f"Generated {len(ascii_lines)} lines of {cols} characters.")
for idx, l in enumerate(ascii_lines[::2]):  # print sample lines
    print(f"{idx:02d}: {l[:40]}")
