with open("input.txt", mode="r", encoding="utf-8") as f:
    all_text = f.readline().strip()
blocks = all_text.split(",")
nums_to_check: list[int] = []
for block in blocks:
    ends = block.split("-")
    lower = int(ends[0])
    upper = int(ends[1])
    for i in range(lower, upper+1):
        nums_to_check.append(i)
invalid_sum: int = 0
for num in nums_to_check:
    numstr = str(num)
    leng = len(numstr)
    if leng%2==0:
        p1 = numstr[: int(leng/2)]
        p2 = numstr[int(leng/2) :]
        if p1 == p2:
            invalid_sum += num
print(invalid_sum)
# new_invalid = 0
# for num in nums_to_check[10000:10001]:
#     numstr = str(num)
#     maxidx = int(len(numstr)/2)
#     splits = []
