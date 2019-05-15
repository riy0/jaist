#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random

def check_win(coordinate_map):
    candidates = [2**i for i in range(9)]
    decision_coordinates = []
    for i in range(3):

        # 列と行の合計を計算
        row_first = i*3
        row_last = (i+1)*3
        row_total = sum(candidates[row_first:row_last])
        decision_coordinates.append(row_total)

        col_list = [candidates[i+3*j] for j in range(3)]
        decision_coordinates.append(sum(col_list))

        # 斜めの合計を計算
        cross1 = [candidates[4*i] for i in range(3)]
        cross2 = [candidates[2*(i+1)] for i in range(3)]
        decision_coordinates.append(sum(cross1)) 
        decision_coordinates.append(sum(cross2))

        # print('coordinate_map : ', coordinate_map)
        # print('decision_coordinates : ', decision_coordinates)

    # 判定処理
    total_val = sum([int(i) for i in coordinate_map])
    if total_val in decision_coordinates:
        return True
    return False

def choose_point():
    if len(pos) == 9:
        # 初手で真ん中を取る場合
        choice = '5'
        """
        # 初手で上下左右のどれかを取る場合
        udlr = ['2','4','6','8']
        choice = random.choice(udlr)

        #初手で四隅のどれかを取る場合
        corners = ['1','3','7','9']
        choice = random.choice(corners) 
        """
    else:
        choice = random.choice(pos)
    pos.remove(choice)

    return choice

def tic_tac_toe(board):
    win_rate = 0

    coordinate_list = list(pos)
    candidates = [2**i for i in range(9)]
    turn = 0
    cnt = 0
    player1_moves = []
    player2_moves = []

    while True:
        #print(board)
        if turn == 0:
            player1_input = choose_point()

            if player1_input in coordinate_list:
                board = board.replace(str(player1_input), "o")
                idx = coordinate_list.index(player1_input)
                coordinate_list[idx] = "o"
                player1_moves.append(candidates[idx])
                if check_win(player1_moves):
                    win_rate += 1
                    break
            turn = 1

        else:
            player2_input = choose_point() 

            if player2_input in coordinate_list:
                board = board.replace(str(player2_input), "x")
                idx = coordinate_list.index(player2_input)
                coordinate_list[idx] = "x"
                player2_moves.append(candidates[idx])
                if check_win(player2_moves):
                    break
            turn = 0
        cnt +=1

        if cnt == 9:
            win_rate += 0.5
            break

    return win_rate

if __name__ == '__main__':
    board = """
    1 2 3
    4 5 6
    7 8 9
    """
    total = []

    for i in range(10000):
        pos = ['1','2','3','4','5','6','7','8','9']
        result =tic_tac_toe(board)
        total.append(result) 
    print("win_rate")
    print("player1: ", sum(total)/100, "%")
    print("player2: ", 100 - sum(total)/100, "%")
