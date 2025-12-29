import numpy as np

with open("input.txt", mode="r", encoding="utf-8") as f:
    database = [line.strip() for line in f]
hit_break = 0
id_ranges = []
ingredients = []
for data_line in database:
    if len(data_line) == 0:
        hit_break = 1
        continue
    if hit_break == 0:
        line = data_line.split("-")
        id_ranges.append([int(line[0]), int(line[1])])
    if hit_break == 1:
        line = int(data_line)
        ingredients.append(line)
id_ranges.sort()
cleaned_range = []
for id_range in id_ranges:
    if not cleaned_range or id_range[0] > cleaned_range[-1][1] + 1:
        cleaned_range.append(id_range)
    else:
        cleaned_range[-1][1] = max(cleaned_range[-1][1], id_range[1])
ingredients = np.array(ingredients)
fresh_ingredients = 0
for ingredient in ingredients:
    lowend = 0
    upend = len(cleaned_range)
    while lowend < upend:
        midway = int((lowend + upend)/2)
        if cleaned_range[midway][0] <= ingredient <= cleaned_range[midway][1]:
            fresh_ingredients += 1
            break
        elif ingredient < cleaned_range[midway][0]:
            upend = midway
        elif ingredient > cleaned_range[midway][1]:
            lowend = midway + 1
print("Fresh ingredients = ", fresh_ingredients)
fresh_ingredient_ids = 0
for interval in cleaned_range:
    interval_size = interval[1] - interval[0] + 1
    fresh_ingredient_ids += interval_size
print("Number of ingredient IDs considered fresh = ", fresh_ingredient_ids)
