import numpy as np

with open("input.txt", mode="r", encoding="utf-8") as f:
    workbook_raw = [line.strip() for line in f]
rows = len(workbook_raw)
workbook = []
operations = workbook_raw[-1].split()
for i in range(rows - 1):
    line = list(map(int, workbook_raw[i].split()))
    workbook.append(line)
workbook = np.array(workbook, dtype=int).T
grand_total = 0
for i, problem in enumerate(workbook):
    if operations[i] == "+":
        answer = 0
        for value in problem:
            answer += value
    elif operations[i] == "*":
        answer = 1
        for value in problem:
            answer *= value
    grand_total += answer
print(grand_total)
