import base64
import os
from PIL import Image, ImageEnhance

# 1. Process Babul's portrait into ASCII matrix with controlled density
im = Image.open("assets/portrait_processed.jpg").convert("L")

# Grid: 40 columns x 36 rows for optimal density inside portrait frame
cols = 40
rows = 36
im_small = im.resize((cols, rows), Image.Resampling.LANCZOS)
enhancer = ImageEnhance.Contrast(im_small)
im_contrasted = enhancer.enhance(1.25)

# ASCII Ramp: spaces for deep blacks, dots for dark background, structured glyphs for subject
char_ramp = " .,:;!+=*%#@"

ascii_matrix = []
for y in range(rows):
    row_chars = []
    for x in range(cols):
        val = im_contrasted.getpixel((x, y))
        # Intentional gaps in dark areas:
        if val < 30:
            ch = " "
        elif val < 60:
            ch = "." if (x + y) % 2 == 0 else " "
        else:
            idx = int((val / 255.0) * (len(char_ramp) - 1))
            ch = char_ramp[idx]
        row_chars.append(ch)
    ascii_matrix.append("".join(row_chars))

# Also read raw base64 portrait
with open("assets/portrait_base64.txt", "r") as f:
    portrait_b64 = f.read().strip()

print(f"ASCII Matrix ready: {len(ascii_matrix)} rows of {cols} chars.")
