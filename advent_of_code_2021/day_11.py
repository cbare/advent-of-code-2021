"""
Day 11: Dumbo Octopus
"""
import numpy as np

with open("data/day-11.txt") as f:
    x = np.array([
        [int(c) for c in line.strip()]
        for line in f
    ])

print(x)

flashes = 0
for step in range(1000):
    x += 1
    while x.max() > 9:
        for i,j in np.transpose((x > 9).nonzero()):
            a,b,c,d = max(0,i-1), min(x.shape[0],i+2), max(0,j-1), min(x.shape[1],j+2)
            x[a:b,c:d] = np.where(x[a:b,c:d] == 0, x[a:b,c:d], x[a:b,c:d]+1)
            x[i,j] = 0
            flashes += 1
    if step == 99:
        print("part 1:", flashes)
    if (x == 0).all():
        print("part 2:", step+1)
        break
