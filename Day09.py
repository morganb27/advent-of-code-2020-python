from itertools import combinations

PUZZLE = list(map(int, open("input.txt")))
PART_1, PART_2 = 0, 0


for i, num in enumerate(PUZZLE):
    if not any(int(a) + int(b) == int(num) for a, b in combinations(PUZZLE[i-25:i], 2)) and i > 25:
        PART_1 = num
        break


for i in range(2, len(PUZZLE)):
    for j in range(i+2, len(PUZZLE)):
        if sum(PUZZLE[i:j]) == PART_1:
            PART_2 = min(PUZZLE[i:j]) + max(PUZZLE[i:j])

print(PART_1)
print(PART_2)





