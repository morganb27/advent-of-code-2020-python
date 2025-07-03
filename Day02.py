from collections import Counter
from utils import ints_positives

PUZZLE = [line.strip() for line in open("input.txt")]
PART_1, PART_2 = 0, 0

for line in PUZZLE:
    low, high = ints_positives(line)
    char = line.split()[1][0]
    pwd = line.split(": ")[1]

    counter = Counter(pwd)
    first_position = low - 1
    second_position = high - 1
    if low <= counter[char] <= high:
        PART_1 += 1
    if (pwd[first_position] == char or pwd[second_position] == char) and pwd[first_position] != pwd[second_position]:
        PART_2 += 1

print(PART_1)
print(PART_2)

    
