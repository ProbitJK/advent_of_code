#!/home/probit/.virtualenvs/python_env_4_probit/bin/python3
# -*- coding: utf-8 -*-
"""Advent of Code 2015, day 3.

@date: 2024-12-12
@author: Probit Jyoti Kalita
"""


def drunk_directions(full_input: str) -> int:
    pos: list[list[int]] = [[0, 0]]
    unique_pos: list[list[int]] = []
    for inp_str in full_input:
        if inp_str == "^":
            pos.append([pos[-1][0], pos[-1][1] + 1])
        elif inp_str == "v":
            pos.append([pos[-1][0], pos[-1][1] - 1])
        elif inp_str == ">":
            pos.append([pos[-1][0] + 1, pos[-1][1]])
        elif inp_str == "<":
            pos.append([pos[-1][0] - 1, pos[-1][1]])
        else:
            print("Unexpected input", inp_str)
    for position in pos:
        if position not in unique_pos:
            unique_pos.append(position)
    return len(unique_pos) 


def drunk_double_directions(full_input: str):
    pos_santa, pos_robo_santa = [[0, 0]], [[0, 0]]
    unique_pos: list[list[int]] = []
    for ind, inp_str in enumerate(full_input):
        if inp_str == "^" and ind%2!=0:
            pos_santa.append([pos_santa[-1][0], pos_santa[-1][1] + 1])
        elif inp_str == "^" and ind%2==0:
            pos_robo_santa.append([pos_robo_santa[-1][0], pos_robo_santa[-1][1] + 1])
        elif inp_str == "v" and ind%2!=0:
            pos_santa.append([pos_santa[-1][0], pos_santa[-1][1] - 1])
        elif inp_str == "v" and ind%2==0:
            pos_robo_santa.append([pos_robo_santa[-1][0], pos_robo_santa[-1][1] - 1])
        elif inp_str == ">" and ind%2!=0:
            pos_santa.append([pos_santa[-1][0] + 1, pos_santa[-1][1]])
        elif inp_str == ">" and ind%2==0:
            pos_robo_santa.append([pos_robo_santa[-1][0] + 1, pos_robo_santa[-1][1]])
        elif inp_str == "<" and ind%2!=0:
            pos_santa.append([pos_santa[-1][0] - 1, pos_santa[-1][1]])
        elif inp_str == "<" and ind%2==0:
            pos_robo_santa.append([pos_robo_santa[-1][0] - 1, pos_robo_santa[-1][1]])
        else:
            print("Unexpected input", inp_str)
    for pos in pos_santa:
        if pos not in unique_pos:
            unique_pos.append(pos)
    for pos in pos_robo_santa:
        if pos not in unique_pos:
            unique_pos.append(pos)
    return len(unique_pos)


with open("./input.txt", encoding="utf-8") as inp_file:
    inp = inp_file.readline()
    inp = inp[:-1]
first_year = drunk_directions(inp)
print(first_year)
second_year = drunk_double_directions(inp)
print(second_year)
