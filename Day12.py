from utils import Point

PUZZLE = open("input.txt").read().split("\n")

DIRECTION = {
    "N": lambda x, y, steps: Point(x, y + steps),
    "S": lambda x, y, steps: Point(x, y - steps),
    "E": lambda x, y, steps: Point(x + steps, y),
    "W": lambda x, y, steps: Point(x - steps, y)
}


DIR_4 = [
    "N",
    "E",
    "S",
    "W"
]

def rotate(p: Point, angle, direction):
    if direction == "L":
        angle = (360 - angle) % 360
    print("angle", angle)
    if angle == 90:
        p = Point(p.y, -p.x)
    elif angle == 180:
        p = Point(-p.x, -p.y)
    elif angle == 270:
        p = Point(-p.y, p.x)
    
    print(p)
    return p
    



def move_ship():
    FACING = "E"
    SHIP_POS = Point(0, 0)
    for instruction in PUZZLE:
        dir = instruction[0]
        steps = int(instruction[1:])
        x = SHIP_POS.x
        y = SHIP_POS.y
        if dir in DIRECTION:
            SHIP_POS = DIRECTION[dir](x, y, steps)
        elif dir == "F":
            SHIP_POS = DIRECTION[FACING](x, y, steps)
        elif dir in ("L", "R"):
            idx = DIR_4.index(FACING)
            steps = steps // 90
            if dir == "R":
                FACING = DIR_4[(idx + steps) % 4]
            else:
                FACING = DIR_4[(idx - steps) % 4]
    return abs(SHIP_POS.x) + abs(SHIP_POS.y)

def move_ship_part_two():
    FACING = "E"
    SHIP_POS = Point(0, 0)
    WAYPOINT = Point(10, 1)

    for instruction in PUZZLE:
        print("WAYPOINT", WAYPOINT)
        dir = instruction[0]
        steps = int(instruction[1:])
        print(dir, steps)
        x = SHIP_POS.x
        y = SHIP_POS.y
        dx = WAYPOINT.x
        dy =  WAYPOINT.y

        if dir == "F":
            SHIP_POS = Point(x + (dx * steps), y + (dy * steps))
            print(SHIP_POS)
        elif dir == "N":
            WAYPOINT = Point(dx, dy + steps)
        elif dir == "S":
            WAYPOINT = Point(dx, dy - steps)
        elif dir == "E":
            WAYPOINT = Point(dx + steps, dy)
        elif dir == "W":
            WAYPOINT = Point(dx - steps, dy)
        elif dir in ("L", "R"):
            WAYPOINT = rotate(WAYPOINT, steps, dir)
    return abs(SHIP_POS.x) + abs(SHIP_POS.y)


PART_1 = move_ship()
PART_2 = move_ship_part_two()
print(PART_1, PART_2)

