import os
import base64
from PIL import Image, ImageEnhance

# Input portrait provided by Babul
source_path = os.path.join("assets", "Babulprofile.jpeg")
if not os.path.exists(source_path):
    source_path = os.path.join("assets", "babul_portrait.jpg")

im = Image.open(source_path)
width, height = im.size
print(f"Source image size: {width}x{height}")

# Optimal editorial crop:
# Focus on Babul's face and upper tech jacket
# x: 320 to 1240 (920 wide)
# y: 30 to 950 (920 high)
crop = im.crop((320, 30, 1240, 950))
crop = crop.resize((480, 480), Image.Resampling.LANCZOS)

# Subtle contrast enhancement for editorial studio finish
enhancer = ImageEnhance.Contrast(crop)
crop = enhancer.enhance(1.05)

out_path = os.path.join("assets", "portrait_processed.jpg")
crop.save(out_path, "JPEG", quality=88, optimize=True)

# Generate base64 string
b64_data = base64.b64encode(open(out_path, "rb").read()).decode("utf-8")
b64_path = os.path.join("assets", "portrait_base64.txt")
with open(b64_path, "w", encoding="utf-8") as f:
    f.write(b64_data)

print(f"Processed portrait saved to {out_path} ({os.path.getsize(out_path)} bytes)")
print(f"Base64 saved to {b64_path} ({len(b64_data)} characters)")
