import sys
import random
import numpy as np
from numpy.random import *

SIZE = 20

t_point=(randint(19, size =(5,2))).tolist() 
f_point=(randint(19, size =(5,2))).tolist() 

ok = 'o '
out= 'x '

def decide_shortest_point(x,y):
    min_t = 100000000
    min_f = 100000000
    for i in range(5):
        tx = t_point[i][0] - x
        ty = t_point[i][1] - y
        dist = tx * tx + ty * ty
        if dist < min_t:
            min_t = dist

    for i in range(5):
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

for i in range(5):
    array[t_point[i][0]][t_point[i][1]] = '@ '
    array[f_point[i][0]][f_point[i][1]] = 'X '

for i in range(SIZE):
    for j in range(SIZE):
        if array[i][j] == '. ':
            decide_shortest_point(i,j)
        sys.stdout.write(array[i][j])
    print()
