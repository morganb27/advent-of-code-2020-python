from utils import Point, DIRS_8

PUZZLE = open("input.txt").read().split("\n")

EMPTY = set()
OCCUPIED = set()
SEATS = set()

# Parse input
for y, _ in enumerate(PUZZLE):
    for x, _ in enumerate(PUZZLE[0]):
        if PUZZLE[y][x] == "L":
            EMPTY.add(Point(x, -y))
        elif PUZZLE[y][x] == "#":
            OCCUPIED.add(Point(x, -y))
        SEATS.add(Point(x, -y))


def arrange_seats_part_one(empty, occupied):
    empty_new = set()
    occupied_new = set()

    for seat in empty:
        count = 0
        for adj in DIRS_8:
            if seat + adj in occupied:
                count += 1
        if count == 0:
            occupied_new.add(seat)
        else:
            empty_new.add(seat)
    
    for seat in occupied:
        count = 0
        for adj in DIRS_8:
            if seat + adj in occupied:
                count += 1
        if count >= 4:
            empty_new.add(seat)
        else:
            occupied_new.add(seat)
    
    return empty_new, occupied_new


def arrange_seats_part_two(empty, occupied):
    empty_new = set()
    occupied_new = set()

    for seat in empty:
        count = 0
        for adj in DIRS_8:
            pos = seat
            while True:
                pos = pos + adj
                if pos not in SEATS:
                    break
                elif pos in empty:
                    break
                elif pos in occupied:
                    count += 1
                    break
        if count == 0:
            occupied_new.add(seat)
        else:
            empty_new.add(seat)
    
    for seat in occupied:
        count = 0
        for adj in DIRS_8:
            pos = seat
            while True:
                pos = pos + adj
                if pos not in SEATS:
                    break
                elif pos in empty:
                    break
                elif pos in occupied:
                    count += 1
                    break
        if count >= 5:
            empty_new.add(seat)
        else:
            occupied_new.add(seat)
    
    return empty_new, occupied_new


EMPTY_ORIG = EMPTY.copy()
OCCUPIED_ORIG = OCCUPIED.copy()


while True:
    empty_cur, occupied_cur = EMPTY.copy(), OCCUPIED.copy()
    EMPTY, OCCUPIED = arrange_seats_part_one(EMPTY, OCCUPIED)
    if empty_cur == EMPTY and occupied_cur == OCCUPIED:
        break

while True:
    empty_cur, occupied_cur = EMPTY_ORIG.copy(), OCCUPIED_ORIG.copy()
    EMPTY_ORIG, OCCUPIED_ORIG = arrange_seats_part_two(EMPTY_ORIG, OCCUPIED_ORIG)
    if empty_cur == EMPTY_ORIG and occupied_cur == OCCUPIED_ORIG:
        break


PART_1 = len(OCCUPIED)
PART_2 = len(OCCUPIED_ORIG)
print(PART_1)
print(PART_2)

