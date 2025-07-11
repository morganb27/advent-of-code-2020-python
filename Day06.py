PUZZLE = open("input.txt").read().split("\n\n")

PART_1 = sum(len(set.union(*map(set, group.split("\n")))) for group in PUZZLE)
PART_2 = sum(len(set.intersection(*map(set, group.split("\n")))) for group in PUZZLE)

print(PART_1)
print(PART_2)