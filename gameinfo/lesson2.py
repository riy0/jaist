import sys
import random
import numpy as np
from numpy.random import *

SIZE = 20
DATA = 2
t_point=[]
f_point=[]
cnt= DATA

for i in range(DATA):
    t_point.append([randint(0,9),randint(0,19)])
    f_point.append([randint(10,19),randint(0,19)])

ok = 'o '
out= 'x '

def decide_shortest_point(x,y):
    min_t = 100000000
    min_f = 100000000
    for i in range(DATA):
        tx = t_point[i][0] - x
        ty = t_point[i][1] - y
        dist = tx * tx + ty * ty
        if dist < min_t:
            min_t = dist

    for i in range(DATA):
        fx = f_point[i][0] - x
        fy = f_point[i][1] - y
        dist = fx * fx + fy * fy
        if dist < min_f:
            min_f = dist

    if min_f < min_t:
        array[x][y] = out
    else:
        array[x][y] = ok

array = np.full((SIZE, SIZE),'. ')

for i in range(DATA):
    array[t_point[i][0]][t_point[i][1]] = '@ '
    array[f_point[i][0]][f_point[i][1]] = 'X '


for j in range(SIZE):
    for i in range(SIZE):
        if array[i][j] == '. ':
            decide_shortest_point(i,j)
        sys.stdout.write(array[i][j])
        if array[i][j] == ok:
           cnt = cnt+1
    print()
print("rate of concordance:", cnt/200*100, "%")
print("o: ", cnt, "x: ",400-cnt )

