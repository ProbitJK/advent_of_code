#!/usr/bin/env python3
"""
Day 1 of Advent of Code 2015.

Why just start with 2023 when I have the entire catalogue of previous AoCs to try out?
"""


def which_floor(inp_text):
    """LSP keeps nagging me for a docstring, so here you go."""
    floor = 0
    for letter in inp_text:
        floor += 1 if letter == "(" else -1
    return floor


with open("input.txt") as inp_file:
    text = inp_file.readline()
    text = text[:-1]
    FINAL_FLOOR = which_floor(text)
    print(FINAL_FLOOR)
