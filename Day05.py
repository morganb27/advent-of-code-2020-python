import math

PUZZLE = open("input.txt").read().splitlines()
PART_1, PART_2 = 0, 0
seats = []

for p in PUZZLE:
    row = p[:7].replace("F", "0").replace("B", "1")
    col = p[7:].replace("L", "0").replace("R", "1")
    seat_id = int(row, 2) * 8 + int(col, 2)
    PART_1 = max(PART_1, seat_id)
    seats.append(seat_id)

seats.sort()

for a, b in zip(seats, seats[1:]):
    if b - a > 1:
        PART_2 = a + 1

print(PART_1)
print(PART_2)



