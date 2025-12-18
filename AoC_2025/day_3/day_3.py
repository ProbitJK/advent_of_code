with open("input.txt", mode="r", encoding="utf-8") as f:
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
new_total_joltage = 0
for bank_line in all_banks:
    bank = list(map(int, bank_line))
    bank_joltage = 0
    for i in range(11):
        jolt = max(bank[: i - 11])
        bank = bank[bank.index(jolt) + 1 :]
        bank_joltage = (bank_joltage * 10) + jolt
    bank_joltage = (bank_joltage * 10) + max(bank)
    new_total_joltage += bank_joltage
print("New total output joltage ", new_total_joltage)
