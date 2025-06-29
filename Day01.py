from utils import two_sum, three_sum

PUZZLE = [int(line) for line in open("input.txt")]
TARGET = 2020

first, second = two_sum(PUZZLE, TARGET)
first, second, third = three_sum(PUZZLE, TARGET)

print(first * second)
print(first * second * third)


