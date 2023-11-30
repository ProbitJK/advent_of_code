#!/usr/bin/env python3
"""
Day 2 of Advent of Code 2015.

The elf gift wrapping problem.
"""

import numpy as np


def single_gift(dimensions):
    """Find the amount of paper needed for a single gift."""
    l, w, h = np.sort(dimensions)
    paper = 2 * (l * w + w * h + h * l) + (l * w)
    ribbon = 2 * (l + w) + (l * w * h)
    return paper, ribbon


all_gifts = np.loadtxt("input.txt", delimiter="x")
total_paper, total_ribbon = 0, 0
for gift_size in all_gifts:
    paper, ribbon = single_gift(gift_size)
    total_paper += paper
    total_ribbon += ribbon
print(total_paper, total_ribbon)
