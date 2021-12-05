"""
Day 05 - Hydrothermal vents
"""
import numpy as np
from collections import namedtuple

Point = namedtuple("Point", "x y")

def coords(line):
    p1, p2 = line.strip().split(" -> ")
    return (
        Point(*(int(elem) for elem in p1.split(","))),
        Point(*(int(elem) for elem in p2.split(",")))
    )

with open("data/day-05.txt") as f:
    lines = [coords(line) for line in f]

n = max(max(p1.x, p2.x) for p1,p2 in lines) + 1
m = max(max(p1.y, p2.y) for p1,p2 in lines) + 1


def normalized_range(a, b):
    return range(min(a,b), max(a,b)+1)

# part 1

grid = np.zeros((n,m))
for p1,p2 in lines:
    # only allow lines that are horiz. vert.
    if p1.x == p2.x:
        for y_i in normalized_range(p1.y, p2.y):
            grid[p1.x, y_i] += 1
    elif p1.y == p2.y:
        for x_i in normalized_range(p1.x, p2.x):
            grid[x_i, p1.y]

print( (grid > 1).sum() )


# part 2

def find_inc(a, b):
    if a > b:
        return -1
    if a < b:
        return 1
    return 0

grid = np.zeros((n,m))
for p1,p2 in lines:
    # assume that lines are horiz. vert. or 45°
    x_inc = find_inc(p1.x, p2.x)
    y_inc = find_inc(p1.y, p2.y)
    x, y = p1
    while (x,y) != p2:
        grid[x,y] += 1
        x += x_inc
        y += y_inc
    grid[x,y] += 1

print( (grid > 1).sum() )
