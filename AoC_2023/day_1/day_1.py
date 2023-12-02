#!/usr/bin/env python3


starter_table = ["e", "f", "n", "o", "t", "s"]
conv_table = [
    ["one", 1],
    ["two", 2],
    ["three", 3],
    ["four", 4],
    ["five", 5],
    ["six", 6],
    ["seven", 7],
    ["eight", 8],
    ["nine", 9],
]


def decode(gibberish):
    nums = []
    for i, character in enumerate(gibberish):
        if character.isdigit():
            nums.append(int(character))
        elif character in starter_table:
            for j in range(9):
                if gibberish[i:].startswith(conv_table[j][0]):
                    nums.append(conv_table[j][1])
    num = 10 * nums[0] + nums[-1]
    return num


sum = 0
with open("input.txt", encoding="utf-8") as in_file:
    lines = in_file.readlines()
    for text in lines:
        sum += decode(text)
print(sum)
