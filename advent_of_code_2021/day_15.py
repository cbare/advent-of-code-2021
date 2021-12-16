"""
Day 15: Chiton
"""
from rich import print
from rich.console import Console
from rich.highlighter import Highlighter
from rich.text import Text

import numpy as np

def array_to_string(a):
    return "\n".join(
        "".join(str(a[i,j]) for j in range(a.shape[1]))
        for i in range(a.shape[0])
    )


with open("data/day-15.txt") as f:
    data = np.array([
        [int(c) for c in line.strip()]
        for line in f
    ])

print(array_to_string(data))


def find_path(data):
    # 1 ↑
    # 2 ←
    # 3 ↓
    # 4 →
    back = np.zeros_like(data)

    cost = np.full_like(data, np.iinfo(data.dtype).max)
    cost[0,0] = 0

    for p in range(200):
        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                if i+1 < data.shape[0]:
                    x = cost[i,j] + data[i+1,j]
                    if x < cost[i+1,j]:
                        cost[i+1,j] = x
                        back[i+1,j] = 1
                if j+1 < data.shape[1]:
                    x = cost[i,j] + data[i,j+1]
                    if x < cost[i,j+1]:
                        cost[i,j+1] = x
                        back[i,j+1] = 2
                if i > 0:
                    x = cost[i,j] + data[i-1,j]
                    if x < cost[i-1,j]:
                        cost[i-1,j] = x
                        back[i-1,j] = 3
                if j > 0:
                    x = cost[i,j] + data[i,j-1]
                    if x < cost[i,j-1]:
                        cost[i,j-1] = x
                        back[i,j-1] = 4

    path = np.zeros_like(data)
    i,j = ((d-1) for d in path.shape)
    path[i,j] = 1
    while i>0 or j>0:
        if back[i,j] == 1: i -= 1
        elif back[i,j] == 2: j -= 1
        elif back[i,j] == 3: i += 1
        elif back[i,j] == 4: j += 1
        path[i,j] = 1

    return cost, path


def print_path(a, path):
    color_map = {
        0: "color(16)",
        1: "color(39)",
    }

    for i in range(a.shape[0]):
        text = Text("".join(str(a[i,j]) for j in range(a.shape[1])))
        for j in range(a.shape[1]):
            text.stylize(color_map.get(path[i,j]), j, j + 1)
        print(text)

print("\nPart 1:")
cost, path = find_path(data)
print(cost[-1,-1])
print_path(data, path)

m,n = data.shape

a = np.zeros((m*5,n*5), dtype=np.int32)
for i in range(5):
    for j in range(5):
        b = (data+(i+j)) % 9
        a[(i*m):(i*m)+m, (j*n):(j*n)+n] = np.where(b==0, 9, b)

print("\nPart 2:")
cost, path = find_path(a)
print(cost[-1,-1])
print_path(a, path)
