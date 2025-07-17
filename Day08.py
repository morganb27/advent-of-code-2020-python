PUZZLE = [tuple((line.strip().split()[0], int(line.strip().split()[1]))) for line in open("input.txt")]

def run(input):
    acc = 0
    i = 0
    visited = set()
    while i not in visited:
        if i == len(input): 
            return acc, True
        op, arg = input[i]
        visited.add(i)
        if op == "acc":
            acc += arg
            i += 1
        elif op == "jmp":
            i += arg
        elif op == "nop":
            i += 1
    return acc, False 
    
# Part 1
PART_1, _ = run(PUZZLE)

# Part 2
for i, (op, arg) in enumerate(PUZZLE):
    if op == "acc":
        continue
    copy = PUZZLE.copy()
    modified = ("nop" if op == "jmp" else "jmp", arg)
    copy[i] = modified
    acc, terminated = run(copy)
    if terminated == True:
        PART_2 = acc
        break

print(PART_1)
print(PART_2)




