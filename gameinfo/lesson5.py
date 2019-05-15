#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random

def check_win(coordinate_map):
    candidates = [2**i for i in range(9)]
    decision_coordinates = []
    for i in range(3):
        # 横の合計を求める
        row_first = i*3
        row_last = (i+1)*3
        row_total = sum(candidates[row_first:row_last])
        decision_coordinates.append(row_total)

        # 縦の合計を求める
        col_list = [candidates[i+3*j] for j in range(3)]
        col_total = sum(col_list)
        decision_coordinates.append(col_total)
        
        # 斜め
        # 1+16+256=273
        # 4+16+64=84
        cross1_list = [candidates[4*i] for i in range(3)]
        cross1_ans = sum(cross1_list)
        decision_coordinates.append(cross1_ans)
       
        # 斜め 2
        # 4+16+64=84
        cross2_list = [candidates[2*(i+1)] for i in range(3)]
        cross2_ans = sum(cross2_list)
        decision_coordinates.append(cross2_ans)
       
        # 横列
        # 1+2+4=7
        # 8+16+32=56
        # 64+128+256=448
        # 縦列
        # 1+8+64=73
        # 2+16+128=146
        # 4+32+256=292
       
        # print('coordinate_map : ', coordinate_map)
        # print('decision_coordinates : ', decision_coordinates)

        # リスト内を全て足して、decision_coordinates内に
        # total_valがあるかを判定する
        # 判定処理
    total_val = sum([int(i) for i in coordinate_map])
    if total_val in decision_coordinates:
        return True
    return False

def tic_tac_toe():

    win_rate1=0
    win_rate2=0

    for i in range(10000):
        text ="""
        1|2|3
        -----
        4|5|6
        -----
        7|8|9
        """
        #print(text)
        coordinate_list = [str(i) for i in range(1, 10)]
        pos = ['1','2','3','4','5','6','7','8','9']
        candidates = [2**i for i in range(9)]
        turn_user = 0
        turn_count = 0
        user1_move = []
        pos_user_operations = []
        while True:
            if turn_user == 0:

                #1手目に真ん中を取る場合
                """
                if len(pos) == 9:
                    choice = '5'
                """

                #1手目に上下左右のどれかを取る場合
                """
                if len(pos) == 9:
                    udlr = ['2','4','6','8']
                    choice = random.choice(udlr)
                """
        
                #1手目に上下左右のどれかを取る場合
                if len(pos) == 9:
                    corners = ['1','3','7','9']
                    choice = random.choice(corners) 

                else:
                    choice = random.choice(pos)
                pos.remove(choice)
                user1_input = choice


                if user1_input in coordinate_list:
                    text = text.replace(str(user1_input), "o")
                    idx = coordinate_list.index(user1_input)
                    coordinate_list[idx] = "o"
                    user1_move.append(candidates[idx])
                    #print(text)
                    if check_win(user1_move):
                        win_rate1 += 1
                        break
                turn_user = 1
                turn_count +=1

            else:
                choice = random.choice(pos)
                pos.remove(choice)
                pos_user_input = choice

                if pos_user_input in coordinate_list:
                    text = text.replace(str(pos_user_input), "x")
                    idx = coordinate_list.index(pos_user_input)
                    coordinate_list[idx] = "x"
                    pos_user_operations.append(candidates[idx]) 
                    # print(text)
                    if check_win(pos_user_operations):
                        win_rate2 += 1
                        break
                    turn_user = 0
                    turn_count += 1

            if turn_count == 9:
                win_rate1 += 0.5
                win_rate2 += 0.5
                break
    return [win_rate1, win_rate2]

print(tic_tac_toe())
