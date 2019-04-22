import sys
import numpy as np
from numpy.random import *

SIZE = 20
DATA = 2
ok = 'o '
out= 'x '
total = 0

def decide_shortest_point(t_point, f_point, x,y):
    min_t = 100000
    min_f = 100000
    for i in range(DATA):
        t = (t_point[i][0] - x) ** 2 + (t_point[i][1] - y) **2
        f = (f_point[i][0] - x) ** 2 + (f_point[i][1] - y) **2
        if t < min_t:
            min_t = t
        if f < min_f:
            min_f = f

    if min_f < min_t:
        return out
    else:
        return  ok

def execute(): 
    #初期化
    t_point = []
    f_point = []
    t_cnt = DATA
    f_cnt = DATA 
    array = np.full((SIZE, SIZE),'. ')

    for i in range(DATA):
        t_point.append([randint(0,9),randint(0,19)])
        f_point.append([randint(10,19),randint(0,19)])

    for i in range(DATA):
        array[t_point[i][0]][t_point[i][1]] = '@ '
        array[f_point[i][0]][f_point[i][1]] = 'X '

    #判定結果が正しいか
    for j in range(SIZE):
        for i in range(SIZE):
            if array[i][j] == '. ':
                array[i][j]= decide_shortest_point(t_point, f_point, i,j)
            if i >= 10:
                if array[i][j] == out:
                    f_cnt = f_cnt + 1
            if i < 10:
                if array[i][j] == ok:
                    t_cnt = t_cnt + 1
            #sys.stdout.write(array[i][j])
        # print()
    rate = (t_cnt + f_cnt) / 400 *100
    print(rate)
    return rate

a = 0
for i in range(10):
    total = (execute() + total) 
print(total/10 , '%')
