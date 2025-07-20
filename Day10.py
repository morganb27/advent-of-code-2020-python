PUZZLE = sorted(list(map(int, open("input.txt"))))

PUZZLE = [0] + PUZZLE + [PUZZLE[-1] + 3]
DP = {}
print(PUZZLE)

d = [b - a for a, b in zip(PUZZLE, PUZZLE[1:])]

DP[0] = 1

for n in PUZZLE[1:]:
    DP[n] = DP.get(n - 1, 0) + DP.get(n - 2, 0) + DP.get(n - 3, 0)

print(DP)


PART_1 = d.count(1) * d.count(3)
PART_2 = DP[PUZZLE[-1]]

print(PART_1)
print(PART_2)



