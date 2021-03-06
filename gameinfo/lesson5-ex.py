#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random

# 手を決定
def choose_point():
    if len(pos) == 9:
        # 初手で真ん中を取る場合
        #choice = 5
        # 初手で上下左右のどれかを取る場合
        """
        udlr = [2,4,6,8]
        choice = random.choice(udlr)
        #初手で四隅のどれかを取る場合
        corners = [1,3,7,9]
        choice = random.choice(corners) 
        """
        choice = random.choice(pos)
    else:
        choice = random.choice(pos)
    pos.remove(choice)
    #print(pos)

    return choice

def check_win(lis):
    if [1, 2, 3] == list(set([1, 2, 3]) & set(lis)):
        return True
    if [4, 5, 6] == list(set([4, 5, 6]) & set(lis)):
        return True
    if [7, 8, 9] == list(set([7, 8, 9]) & set(lis)):
        return True
    if [1, 4, 7] == list(set([1, 4, 7]) & set(lis)):
        return True
    if [2, 5, 8] == list(set([2, 5, 8]) & set(lis)):
        return True
    if [3, 6, 9] == list(set([3, 6, 9]) & set(lis)):
        return True
    if [1, 5, 9] == list(set([1, 5, 9]) & set(lis)):
        return True
    if [3, 5, 7] == list(set([3, 5, 7]) & set(lis)):
        return True
    return False

def tic_tac_toe(board):
    win_rate = [0,0]                        # 勝率

    coord_list = list(pos)                  # 座標
    options = [2**i for i in range(9)]
    turn = 0                                # 先手と後手を0,1で表現
    cnt = 0                                 # 手数を保存
    player_moves = [[],[]]                  # それぞれの手を格納
    chars = ["o", "x"]                      # 先手，後手

    while True:
        # 座標を決定
        player_input = choose_point()       

        # 先手
        if turn == 0:
            board = board.replace(str(player_input), chars[turn])
            #idx = coord_list.index(player_input)
            #coord_list[idx] = chars[turn]
            player_moves[turn].append(player_input)
            if check_win(player_moves[turn]):
                win_rate[turn] += 1
                print(board)
                break
            turn = 1

        # 後手
        else:
            #print(turn) 
            board = board.replace(str(player_input), chars[turn])
            #idx = coord_list.index(player_input)
            #coord_list[idx] = chars[turn]
            player_moves[turn].append(player_input)
            if check_win(player_moves[turn]):
                win_rate[turn] += 1
                #print(board)
                break
            turn = 0

        cnt +=1

        #print(board)
        if cnt == 9:

            win_rate[0] += 0.5
            #print("draw")
            break

    return win_rate[0]

if __name__ == '__main__':
    board = """
    1 2 3
    4 5 6
    7 8 9
    """
    total = []

    for i in range(10000):
        pos = [1,2,3,4,5,6,7,8,9]
        result =tic_tac_toe(board)
        total.append(result) 

    print("win_rate")
    print("player1: ", sum(total)/100, "%")
    print("player2: ", 100 - sum(total)/100, "%")
