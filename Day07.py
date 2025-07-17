import re
from collections import defaultdict

#re.findall(r"(\d+) (\w+) (\w+)"

PUZZLE = open("input.txt").read().split("\n")
graph_one = defaultdict(list)
graph_two = defaultdict(list)

def dfs(graph, node, visited = None):
    if visited is None:
        visited = set()
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            visited.add(neighbor)
            dfs(graph, neighbor, visited)
    return len(visited)


def count_bags(graph, node):
    total = 0
    for count, child in graph[node]:
        print(count, child)
        total += count * (1 + count_bags(graph, child))
    return total

for line in PUZZLE:
    outer, rest = line.strip().split(" bags contain ")
    for count, a, b in re.findall(r"(\d+) (\w+) (\w+)", rest):
        inner  = f"{a} {b}"
        graph_one[inner].append(outer)
        graph_two[outer].append((int(count), inner))


PART_1 = dfs(graph_one, "shiny gold")
PART_2 = count_bags(graph_two, "shiny gold")
print(PART_1)
print(PART_2)
