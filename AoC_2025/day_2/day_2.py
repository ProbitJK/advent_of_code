with open("input.txt", mode="r", encoding="utf-8") as f:
    all_text = f.readline().strip()
blocks = all_text.split(",")
nums_to_check: list[int] = []
for block in blocks:
    ends = block.split("-")
    lower = int(ends[0])
    upper = int(ends[1])
    for i in range(lower, upper + 1):
        nums_to_check.append(i)
invalid_sum: int = 0
for num in nums_to_check:
    numstr = str(num)
    leng = len(numstr)
    if leng % 2 == 0:
        p1 = numstr[: int(leng / 2)]
        p2 = numstr[int(leng / 2) :]
        if p1 == p2:
            invalid_sum += num
print(invalid_sum)
new_invalid_sum: int = 0
for num in nums_to_check:
    NUM_S = str(num)
    MAX_BLOCKS = len(NUM_S)
    num_blocks = 2
    while num_blocks <= MAX_BLOCKS:
        if MAX_BLOCKS % num_blocks == 0:
            parts: list[str] = []
            block_size = int(MAX_BLOCKS / num_blocks)
            for i in range(0, MAX_BLOCKS, block_size):
                parts.append(NUM_S[i : i + block_size])
            condi = False
            for i in range(1, num_blocks):
                if parts[i] == parts[i-1]:
                    condi = True
                else:
                    condi = False
                    break
            if condi==True:
                new_invalid_sum += num
                break
            num_blocks += 1
        else:
            num_blocks += 1
print(new_invalid_sum)
