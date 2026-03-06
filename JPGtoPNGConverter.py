import sys
import os
from PIL import Image

jpg_folder = sys.argv[1]
png_folder = sys.argv[2]

if not os.path.exists(png_folder):
    os.makedirs(png_folder)

for file in os.listdir(jpg_folder):
    img = Image.open(f'{jpg_folder}{file}')
    strip_name = os.path.splitext(file)[0]
    img.save(f'{png_folder}{strip_name}.png', 'png')



