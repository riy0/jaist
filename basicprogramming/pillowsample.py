# how to install pillow:
#   for MacOS users:
#     python -m pip install pillow

from PIL import Image, ImageDraw

im = Image.open("maze.png")
draw = ImageDraw.Draw(im)

(width, height) = im.size

L = []
for x in range(0, width):
    for y in range(0, height):
        (r,g,b,a) = im.getpixel((x,y))
        if (r,g,b) == (255,255,255):
            L.append((x,y))
print((L))

for (x, y) in L:
    #draw.ellipse((x-10,y-10,x+10,y+10),outline=(0,0,255),width=5)
    draw.point((x,y),(0,0,255))

#draw.line([(100,100),(200,150),(300,100),(400,150)], fill=(255, 0, 0), width=5)

im.save("b.png")
