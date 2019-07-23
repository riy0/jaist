from PIL import Image, ImageDraw
from itertools import groupby

def find_min(W, dist):
    u = W[0]
    for v in W:
        if dist[u] > dist[v]:
            u = v
    return u

def dijkstra(A, c, x, y):
    dist = {x: 0}
    W = [x]
    P = {}
    while W != []:
       u = find_min(W, dist)
       W.remove(u)
       if u == y:
            break
       for v in A[u]:
           u2,v2 = sorted([u,v])
           dv = dist[u] + c(u2, v2)
           if not v in dist or dv < dist[v]:
               dist[v] = dv
               P[v] = u
               W.append(v)
    if y in dist:
        return P
    else:
        return None

def draw_route(route, end_point):
    temp = route[end_point[1]]
    while end_point[0] != route[temp]:
        adj = route[temp]
        draw.line([adj,temp], fill=(255, 0, 0), width=4)
        temp = adj

im = Image.open("kanazawa.png")
draw = ImageDraw.Draw(im)

(width, height) = im.size

end_point =[]
L = {}
C = {}

for x in range(0, width):
    for y in range(0, height):
        (r,g,b,a) = im.getpixel((x,y))
        if (r,g,b) == (255,0,0):
            end_point.append((x,y))
            draw.point((x,y), fill=(255,255,255)) 


for x in range(0, width):
    for y in range(0, height):
        (r,g,b,a) = im.getpixel((x,y))

        if (r,g,b) == (255,255,255):
            adj = []
            if x < width - 1:
                cr, cg, cb, ca = im.getpixel((x+1,y))
                if (cr, cg, cb) == (255,255,255):
                    adj.append((x+1, y))
                    adj_cost = tuple(sorted(((x,y),(x+1, y))))
                    if not adj_cost in C.keys():
                        C[adj_cost] = 1

            if x > 0:
                cr, cg, cb, ca = im.getpixel((x-1,y))
                if (cr, cg, cb) == (255,255,255):
                    adj.append((x-1, y))
                    adj_cost = tuple(sorted(((x,y),(x-1, y))))
                    if not adj_cost in C.keys():
                        C[adj_cost] = 1

            if y > 0:
                cr, cg, cb, ca = im.getpixel((x,y-1))
                if (cr, cg, cb) == (255,255,255):
                    adj.append((x, y-1))
                    adj_cost = tuple(sorted(((x,y),(x, y-1))))
                    if not adj_cost in C.keys():
                        C[adj_cost] = 1

            if y < height - 1:
                cr, cg, cb, ca = im.getpixel((x,y+1))
                if (cr, cg, cb) == (255,255,255):
                    adj.append((x, y+1))
                    adj_cost = tuple(sorted(((x,y),(x, y+1))))
                    if not adj_cost in C.keys():
                        C[adj_cost] = 1

            if x < width - 1 and y > 0:
                cr, cg, cb, ca = im.getpixel((x+1,y-1))
                if (cr, cg, cb) == (255,255,255):
                    adj.append((x+1, y-1))
                    adj_cost = tuple(sorted(((x,y),(x+1, y-1))))
                    if not adj_cost in C.keys():
                        C[adj_cost] = 2 ** 0.5

            if x < width - 1 and y < height -1:
                cr, cg, cb, ca = im.getpixel((x+1,y+1))
                if (cr, cg, cb) == (255,255,255):
                    adj.append((x+1, y+1))
                    adj_cost = tuple(sorted(((x,y),(x+1, y+1))))
                    if not adj_cost in C.keys():
                        C[adj_cost] = 2 ** 0.5


            if x > 0 and y < height -1:
                cr, cg, cb, ca = im.getpixel((x-1,y+1))
                if (cr, cg, cb) == (255,255,255):
                    adj.append((x-1, y+1))
                    adj_cost = tuple(sorted(((x,y),(x+1, y+ 1))))
                    if not adj_cost in C.keys():
                        C[adj_cost] = 2 ** 0.5

            if x > 0 and y > 0:
                cr, cg, cb, ca = im.getpixel((x-1,y-1))
                if (cr, cg, cb) == (255,255,255):
                    adj.append((x-1, y-1))
                    adj_cost = tuple(sorted(((x,y),(x-1, y-1))))
                    if not adj_cost in C.keys():
                        C[adj_cost] = 2 ** 0.5

            L[(x,y)]= adj

route= dijkstra(L, lambda x,y:C[(x,y)], end_point[0], end_point[1])

draw_route(route, end_point)

im.save("a.png")
