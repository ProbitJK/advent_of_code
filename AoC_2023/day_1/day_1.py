#!/usr/bin/env python3


def decode(gibberish):
    leng = len(gibberish)
    tens = []
    ones = []
    for i in range(leng):
        if gibberish[i].isdigit():
            tens.append(int(gibberish[i]))
        if gibberish[leng - i - 1].isdigit():
            ones.append(int(gibberish[leng - i - 1]))
    num = 10 * tens[0] + ones[0]
    return num


example = "treb7uchet"

calibration = decode(example)
print(calibration)

sum = 0
with open('input.txt', encoding='utf-8') as in_file:
    lines = in_file.readlines()
    for text in lines:
        sum += decode(text)
print(sum)
