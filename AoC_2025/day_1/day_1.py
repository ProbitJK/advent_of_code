#!/home/probitjk/.virtualenvs/general/bin/python3
# -*- coding: utf-8 -*-
"""Advent of Code 2025 - Day 1

@date: 2025-12-01
@author: Probit Jyoti Kalita
"""

with open("input.txt", mode="r", encoding="utf-8") as f:
    full_text = f.readlines()
current_pos = 50
zeros = 0
clicks = 0
for line in full_text:
    direction = str(line[0])
    steps = int(line[1:-1])
    move_dir = 1 if direction == "R" else -1
    for i in range(steps):
        current_pos += move_dir
        if current_pos == -1:
            current_pos = 99
        elif current_pos == 100:
            current_pos = 0
        if current_pos == 0:
            clicks += 1
    if current_pos == 0:
        zeros += 1
print(
    f"Dial is currently pointing at {current_pos} and it has stopped at zero exactly {zeros} times."
)
print(f"Dial pointed to zero exactly {clicks} times.")
