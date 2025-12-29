import numpy as np

with open("input.txt", mode="r", encoding="utf-8") as f:
    full_grid = [line.strip() for line in f]
n_rows = len(full_grid)
n_cols = len(full_grid[0])
griddy = np.zeros((n_rows, n_cols), dtype=int)
for i in range(n_rows):
    for j in range(n_cols):
        if full_grid[i][j] == ".":
            griddy[i][j] = 0
        else:
            griddy[i][j] = 8
new_griddy = griddy.copy()
while(True):
    rolls_removed = 0
    for i in range(n_rows):
        for j in range(n_cols):
            if griddy[i][j]==8:
                surround_count = 0
                for ylim in range(i - 1, i + 2):
                    for xlim in range(j - 1, j + 2):
                        if ylim < 0 or ylim >= n_rows:
                            continue
                        if xlim < 0 or xlim >= n_cols:
                            continue
                        if ylim == i and xlim == j:
                            continue
                        if griddy[ylim][xlim] == 8:
                            surround_count += 1
                if surround_count < 4:
                    new_griddy[i][j] = 1
                    rolls_removed += 1
    if rolls_removed == 0:
        break
    else:
        griddy = new_griddy.copy()
accessible = np.count_nonzero(new_griddy==1)
print("Number of printer paper rolls accessible = ", accessible)
