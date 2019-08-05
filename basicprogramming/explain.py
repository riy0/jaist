# how to install pillow:
#   for Windows users:
#     py -m pip install pillow
#   for MacOS users:
#     python -m pip install pillow
import sys
from PIL import Image, ImageDraw

argv = sys.argv[1]
print(argv)
im = Image.open(argv)
draw = ImageDraw.Draw(im)

(width, height) = im.size

edge = []

for x in range(0, width):
    for y in range(0, height):
        (r,g,b,a) = im.getpixel((x,y))
        if (r,g,b) == (255, 0, 0):
            edge.append((x,y))          #[(x1,y1), (x2,y2)]

print(edge)



im.save("a.png")
