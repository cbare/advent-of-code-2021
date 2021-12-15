"""
Day 14: Extended Polymerization
"""
from collections import Counter
from rich.progress import track

with open("data/day-14.txt") as f:
    start, rules = f.read().strip().split("\n\n")

rules = dict(line.split(" -> ") for line in rules.split("\n"))

def pairs(a):
    for i in range(len(a)-1):
        yield a[i:(i+2)]

def apply(rules, pair):
    if pair in rules:
        a,b = pair
        return a + rules[pair]
    raise ValueError(f"No rule found for {pair}.")

def step(rules, a):
    return "".join([apply(rules, pair) for pair in pairs(a)]) + a[-1]

def step_counts(rules, c):
    b = Counter()
    for pair, n in c.items():
        z = rules[pair]
        b[pair[0]+z] += n
        b[z+pair[1]] += n
    return b

a = start
for i in range(1,11):
    a = step(rules, a)

c = Counter(a)
_, n = c.most_common()[0]
_, m = c.most_common()[-1]
print("part 1:", (n-m))


a = start
pc = Counter(pair for pair in pairs(start))
print(f"  0: {a}")
print(pc)

for i in range(1,11):
    a = step(rules, a)
    print(f" {i:2}: {a}")
    pc = step_counts(rules, pc)
    print(pc)

c = Counter()
for pair, n in pc.items():
    for z in pair:
        c[z] += n
c[start[0]] += 1
c[start[-1]] += 1
_, n = c.most_common()[0]
_, m = c.most_common()[-1]
print("part 1:", (n-m)//2)

for i in track(range(11,41)):
    pc = step_counts(rules, pc)

c = Counter()
for pair, n in pc.items():
    for z in pair:
        c[z] += n
c[start[0]] += 1
c[start[-1]] += 1
_, n = c.most_common()[0]
_, m = c.most_common()[-1]
print("part 2:", (n-m)//2)
