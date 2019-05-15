import sys
import numpy as np
from numpy.random import *

SIZE = 20
DATA = 2
ok = 'o '
out= 'x '
total = 0

# 正例・負例に近い方を決定し 'x', 'o'を決定
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

    # 負例が近ければ'x', 違えば'o'
    if min_f < min_t:
        return out
    return  ok

# main 
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

    for j in range(SIZE):
        for i in range(SIZE):
            #判定
            if array[i][j] == '. ':
                array[i][j]= decide_shortest_point(t_point, f_point, i,j)

            #正しく判定できる個数をカウント
            if i >= 10:
                if array[i][j] == out:
                    f_cnt = f_cnt + 1
            if i < 10:
                if array[i][j] == ok:
                    t_cnt = t_cnt + 1
            #sys.stdout.write(array[i][j])
        #print()
    rate = (t_cnt + f_cnt) / 400 *100
    #print('concordance rate:', rate) 
    return rate

# 10回試行し,平均を算出
for i in range(10):
    total = (execute() + total) 
print('average of concordance rate, 10 times NN method: ',total/10 , '%')
