"""
Day 12: Passage Pathing
"""
from collections import deque

graph = {}
with open("data/day-12.txt") as f:
    for line in f:
        a,b = line.strip().split("-")
        graph.setdefault(a, []).append(b)
        graph.setdefault(b, []).append(a)

print(graph)

def visit(visits, b):
    x = visits.copy()
    x[b] = x.get(b,0) + 1
    return x

def traverse(graph, allow_extra=False, verbose=False):
    paths = []
    visits = {"start":1}
    q = deque()
    q.append(("start", [], visits, allow_extra))
    while q:
        a, path, visits, extra = q.pop()
        if verbose:
            print(f"pop {a=}, {path=}")
            print(f"{q=}")
        path = path+[a]
        if a == "end":
            if verbose: print(f"path {path=}")
            paths.append(path)
            continue
        for b in graph[a]:
            if visits.get(b,0) == 0 or b[0].isupper():
                if verbose: print(f"push {b=}, {path=}")
                q.append((b, path, visit(visits, b), extra))
            elif extra and visits.get(b) == 1 and b != "start":
                if verbose: print(f"push {b=}, {path=}")
                q.append((b, path, visit(visits, b), False))

        if verbose: print('-'*60)
    return paths

paths = traverse(graph)
print("part 1:", len(paths))

paths = traverse(graph, allow_extra=True)
print("part 2:", len(paths))
