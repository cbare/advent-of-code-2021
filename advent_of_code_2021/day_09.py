"""
Day 9: Smoke Basin
"""
from collections import deque
import numpy as np

with open("data/day-09.txt") as f:
    a = np.array([
        [int(n) for n in line.strip()]
        for line in f
    ])

print(a)

b = np.empty_like(a)
b[0] = 9
b[1:,:] = a[0:-1,:]

c = np.empty_like(a)
c[:,0] = 9
c[:,1:] = a[:,0:-1]

d = np.empty_like(a)
d[-1] = 9
d[0:-1,:] = a[1:,:]

e = np.empty_like(a)
e[:,-1] = 9
e[:,0:-1] = a[:,1:]

low_points = (a < np.stack((b,c,d,e)).min(0))
print(sum(a[low_points]+1))

low_point_coords = np.transpose(low_points.nonzero())

def neighbors(coords, shape):
    x,y = coords
    m,n = shape
    if x > 0:
        yield (x-1),y
    if y > 0:
        yield x,(y-1)
    if (x+1) < m:
        yield (x+1),y
    if (y+1) < n:
        yield x,(y+1)

def expand(a, coords):
    basin = set()
    basin.add(coords)
    seen = set()
    seen.add(coords)
    q = deque()
    q.append(coords)
    while not len(q)==0:
        coords = q.popleft()
        for neighbor in neighbors(coords, a.shape):
            if neighbor not in seen:
                seen.add(neighbor)
                if a[neighbor] < 9:
                    q.append(neighbor)
                    basin.add(neighbor)
    return basin

basins = [expand(a, (x,y)) for x,y in low_point_coords]

basins = sorted(basins, key=len, reverse=True)

print(len(basins[0]) * len(basins[1]) * len(basins[2]))
