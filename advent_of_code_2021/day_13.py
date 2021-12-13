"""
Day 13: Transparent Origami
"""
import re
import numpy as np
from rich import print
from rich.console import Console
from rich.highlighter import Highlighter

class ZeroOneHighlighter(Highlighter):
    color_map = {
        "0": "color(16)",
        "1": "color(39)",
    }
    def highlight(self, text):
        for i in range(len(text)):
            text.stylize(self.color_map.get(text.plain[i:i+1]), i, i + 1)
console = Console(highlighter=ZeroOneHighlighter())

with open("data/day-13.txt") as f:
    coords, folds = f.read().split("\n\n")

def array_to_string(a):
    return "\n".join(
        "".join(str(a[i,j]) for i in range(a.shape[0]))
        for j in range(a.shape[1])
    )

def to_coords(line):
    x,y = line.strip().split(",")
    return int(x), int(y)

coords = [to_coords(line) for line in coords.split("\n")]
folds = [line.strip() for line in folds.split("\n")]

dimensions = max(coord[0] for coord in coords)+1, max(coord[1] for coord in coords)+1
a = np.zeros(dimensions, dtype=np.int32)

for x,y in coords:
    a[x,y] = 1

def pr(a, label=None):
    if label: print(f"{label}=")
    print(np.transpose(a))

pr(a)

axis_map = {'x': 0, 'y': 1}

def fold(a, axis, i):
    axis = axis_map[axis]
    j = i+1
    k = a.shape[axis] - j
    m = abs(i - k)
    if axis==1:
        b = a[:,0:i].copy()
        c = a[:,j:].copy()
        c = np.flip(c, axis=axis)
        if i >= k:
            b[:,m:] += c
            return b
        else:
            c[:,m:] += b
            return c
    else:
        b = a[0:i,:].copy()
        c = a[j:,:].copy()
        c = np.flip(c, axis=axis)
        if i >= k:
            b[m:,:] += c
            return b
        else:
            c[m:,:] += b
            return c

for instruction in folds[0:1]:
    m = re.match(r"fold along (\w)=(\d+)", instruction)
    if m:
        a = fold(a, axis=m.group(1), i=int(m.group(2)))

print((a > 0).sum())


for instruction in folds:
    m = re.match(r"fold along (\w)=(\d+)", instruction)
    if m:
        a = fold(a, axis=m.group(1), i=int(m.group(2)))

console.print(array_to_string(np.clip(a, 0, 1)))
