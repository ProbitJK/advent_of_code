with open("test.txt", mode="r", encoding="utf-8") as f:
    all_banks = [line.strip() for line in f]
total_joltage = 0
for bank in all_banks:
    bank_length = len(bank)
    bank_jolts = []
    for i in range(bank_length):
        bank_jolts.append(bank[i : i + 1])
    max_jolt = max(bank_jolts[:-1])
    max_jolt_idx = bank_jolts.index(max_jolt)
    nex_max_jolt = max(bank_jolts[max_jolt_idx + 1 :])
    bank_joltage = int(max_jolt) * 10 + int(nex_max_jolt)
    total_joltage += bank_joltage
print("total output joltage ", total_joltage)
# there is some flaw in the logic that is making it not work
# larger_total_joltage = 0
# for bank in all_banks:
#     bank_length = len(bank)
#     bank_jolts = []
#     for i in range(bank_length):
#         bank_jolts.append(bank[i : i + 1])
#     bank_big_jolts = []
#     bank_big_jolts.append(max(bank_jolts[:-11]))
#     startind = bank_jolts.index(bank_big_jolts[0])
#     print(bank_jolts)
#     print(bank_big_jolts, startind)
#     while True:
#         nex_jolt = max(bank_jolts[startind + 1 :])
#         nex_jolt_idx = bank_jolts[startind + 1 :].index(nex_jolt)
#         print(nex_jolt, nex_jolt_idx)
#         if len(bank_big_jolts) + len(bank_jolts[startind + nex_jolt_idx :]) >= 12:
#             bank_big_jolts.append(nex_jolt)
#             startind += nex_jolt_idx
#             print(bank_big_jolts, startind)
#         else:
#             nex_jolt = max(bank_jolts[startind + 1 : nex_jolt_idx])
#             nex_jolt_idx = bank_jolts[startind + 1 : nex_jolt_idx -1].index(nex_jolt)
#             bank_big_jolts.append(nex_jolt)
#             startind += nex_jolt_idx
#             print(bank_big_jolts, startind)
#         if len(bank_big_jolts)==12:
#             print(bank_big_jolts)
#             break
