#!/usr/bin/env python3
"""
Day 1 of Advent of Code 2015.

Why just start with 2023 when I have the entire catalogue of previous AoCs to try out?
"""


def when_basement(inp_text):
    """Find which move sends Santa to the basement."""
    floor = 0
    entry_point = 0
    for position, letter in enumerate(inp_text):
        floor += 1 if letter == "(" else -1
        if floor == -1:
            entry_point = position + 1
            break
    return entry_point


def which_floor(inp_text):
    """LSP keeps nagging me for a docstring, so here you go."""
    floor = 0
    for letter in inp_text:
        floor += 1 if letter == "(" else -1
    return floor


with open("input.txt", encoding="utf-8") as inp_file:
    text = inp_file.readline()
    text = text[:-1]
    FINAL_FLOOR = which_floor(text)
    BASEMENT_ENTRY = when_basement(text)
    print(FINAL_FLOOR, BASEMENT_ENTRY)
