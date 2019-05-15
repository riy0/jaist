import sys
import numpy as np
from numpy.random import *

SIZE = 20

# 正例・負例の座標をランダムに決定
t_point=(randint(19, size =(5,2))).tolist() 
f_point=(randint(19, size =(5,2))).tolist() 

ok = 'o '
out= 'x '

# k-nn のkを取得
def get_num():
    print("k-nn: Enter number > ") 
    x = input()
    if int(x) > 10:
        print("too big. please enter number again (below 10):")
        get_num()
    return int(x) 

# k-nnにより'o'または'x'を決定
def decide_shortest_point(x,y,k):
    sample = t_point
    sample.extend(f_point)
    l=[]
    cnt= 0

    #現在の座標と正例・負例との距離を算出し、距離の短い順に並べ替え
    for i in range(10):
        l.append([i, (sample[i][0]- x) ** 2 + (sample[i][1] - y) ** 2])
    sort= sorted(l, key=lambda x:x[1])
    del sort[k:]

    for i in range(len(sort)):
        if sort[i][0] < 5:
            cnt =  cnt + 1
    if cnt > k/2:
        array[x][y] = ok
    else:
        array[x][y] = out


array = np.full((SIZE, SIZE),'. ')
k = get_num() 

for i in range(5):
    array[t_point[i][0]][t_point[i][1]] = '@ '
    array[f_point[i][0]][f_point[i][1]] = 'X '

for i in range(SIZE):
    for j in range(SIZE):
        if array[i][j] == '. ':
            decide_shortest_point(i,j,k)
        sys.stdout.write(array[i][j])
    print()
