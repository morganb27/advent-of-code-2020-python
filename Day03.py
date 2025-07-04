PUZZLE = open("input.txt").read().splitlines()

def count_trees(dx, dy):
    x, y, count = 0, 0, 0
    while x < len(PUZZLE):
        if PUZZLE[x][y%len(PUZZLE[0])] == "#":
            count += 1
        x += dx
        y += dy
    return count


print(count_trees(1, 3))
print(count_trees(1, 1) * count_trees(1, 3) * count_trees(1, 5) * count_trees(1, 7) * count_trees(2, 1))
