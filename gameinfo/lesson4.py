# coding=utf-8
import sys
import queue

SIZE =  15
NUM = 1000000

#問題を解く
def solve_maze(maze):
    dist = [[NUM for i in range(SIZE)] for j in range(SIZE)]
    dist[1][1] = 0
    queue = [(1,1)]
    route=[[1,1]]

    #ゴールに到達するまで迷路を探索する
    while len(queue):
        x,y = queue.pop()
        if x == 13 and y ==13:
            break

        # ↑ → ↓ ←　を探索し、進行先があればqueueに追加し探索する
        for i in range(0, 4):
            nx, ny = x + [1, 0, -1, 0][i], y + [0, 1, 0, -1][i]
            if (1 <= nx and nx < SIZE-1 and 1 <= ny and ny < SIZE -1):
                if maze[nx][ny] == '*':
                    continue
                elif (maze[nx][ny] == '-' and dist[nx][ny] ==NUM):
                    queue.insert(0, ((nx, ny)))
                    dist[nx][ny] = dist[x][y] + 1

                    # 出力のため成形
                    if int(maze[x][y]) < 9:
                        maze[nx][ny] = str(int(maze[x][y]) + 1) + ' '
                    else:
                        maze[nx][ny] = str(int(maze[x][y]) + 1)
                    route.append([nx,ny])

    #探索結果を出力
    for i in range(SIZE):
        for j in range(SIZE):
            sys.stdout.write(str(maze[i][j])) 
        print()

    #探索順序を出力
    order=[[13,13]]
    pursue_best(maze, order[0], 40, order)


# 最短の道順を再帰的にゴールから計算
def pursue_best(maze, now, step, order):
    if step == 0:
        best = order[::-1]
        print("steps", best)
        return 0

    #現在の座標
    y,x = now

    # 前の手を探す。
    # リファクタリングする時間がありませんでした。
    if maze[y-1][x] != '* ':
        if int(maze[y-1][x])  == step-1:
            now = [y-1,x]
    if maze[y+1][x] != '* ':
        if int(maze[y+1][x]) == step-1:
            now = [y+1,x]
    if maze[y][x-1] != '* ':
        if int(maze[y][x-1]) == step-1:
            now = [y,x-1]
    if maze[y][x+1] != '* ':
        if int(maze[y][x+1]) == step-1:
            now = [y,x+1]

    order.append(now)
    pursue_best(maze, now, step-1, order)


if __name__ == '__main__':
    #迷路
    maze = [['* ', '* ', '* ', '* ', '* ', '* ', '* ', '* ', '* ', '* ', '* ', '* ', '* ', '* ', '* '],
            ['* ', '0 ', '-' , '-' , '-' , '-' , '-' , '-' , '-' , '-' , '-' , '-' , '-' , '-' , '* '],
            ['* ', '-' , '* ', '* ', '-' , '* ', '* ', '* ', '* ', '* ', '* ', '* ', '* ', '* ', '* '],
            ['* ', '-' , '* ', '* ', '-' , '* ', '* ', '* ', '* ', '* ', '* ', '* ', '* ', '* ', '* '],
            ['* ', '-' , '* ', '* ', '-' ,  '-', '-' , '-' , '-' , '-' , '-' , '-' , '-' , '* ', '* '],
            ['* ', '-' , '* ', '* ', '* ', '* ', '-' , '* ', '* ', '-' , '* ', '* ', '* ', '* ', '* '],
            ['* ', '-' , '* ', '* ', '* ', '* ', '-' , '* ', '* ', '* ', '* ', '* ', '* ', '* ', '* '],
            ['* ', '-' , '-' , '-' , '* ', '* ', '-' , '* ', '* ', '* ', '* ', '* ', '* ', '* ', '* '],
            ['* ', '* ', '* ', '* ', '* ', '* ', '-' , '* ', '* ', '* ', '* ', '* ', '* ', '* ', '* '],
            ['* ', '* ', '* ', '* ', '* ', '* ', '-' , '* ', '-' , '-' , '-' , '* ', '* ', '* ' , '* '],
            ['* ', '* ', '* ', '* ', '* ', '* ', '-' , '* ', '-' , '* ', '-' , '* ', '* ', '-' , '* '],
            ['* ', '* ', '-' , '-' , '-' ,  '-', '-' , '* ', '-' , '* ', '-' , '-' , '-' , '-' , '* '],
            ['* ', '* ', '-' , '* ', '* ', '* ', '* ', '* ', '-' , '* ', '* ', '* ', '* ', '-' , '* '],
            ['* ', '* ', '-' , '-' , '-' ,  '-', '-' , '-' , '-' , '* ', '* ', '* ', '* ', '-' , '* '],
            ['* ', '* ', '* ', '* ', '* ', '* ', '* ', '* ', '* ', '* ', '* ', '* ', '* ', '* ', '* ']]

    solve_maze(maze) 
