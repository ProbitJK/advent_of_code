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
for i, problems in enumerate(workbook):
    if operations[i] == "+":
        answer = 0
        for value in problems:
            answer += value
    elif operations[i] == "*":
        answer = 1
        for value in problems:
            answer *= value
    grand_total += answer
print("Grand total of all answers ", grand_total)
## Part 2
with open("input.txt", mode="r", encoding="utf-8") as f:
    workbook_raw = [line.strip("\n") for line in f]
problems = []
for i in range(len(workbook_raw[0]) - 1, -1, -1):
    number = []
    for j in range(rows - 1):
        number.append(workbook_raw[j][i])
    num = "".join(number)
    problems.append(num)
all_problems = []
for i in range(0, len(problems), rows):
    all_problems.append(problems[i : i + rows - 1])
new_grand_total = 0
print(all_problems)
for i, problem in enumerate(all_problems):
    if operations[len(operations) - i - 1] == "*":
        answer = 1
        for value in problem:
            answer *= int(value)
    elif operations[len(operations) - i - 1] == "+":
        answer = 0
        for value in problem:
            answer += int(value)
    new_grand_total += answer
print("Corrected grand total of all answers ", new_grand_total)
