"""
Day 3
"""
from collections import Counter

N_BITS = 12

counters = [Counter() for _ in range(N_BITS)]

with open("data/day-03.txt") as f:
    lines = [line.strip() for line in f]

for line in lines:
    assert len(line) == N_BITS
    for counter, b in zip(counters, line):
        counter[b] += 1

# part 1

gamma = "".join(
    "1" if counter["1"] >= counter["0"] else "0"
    for counter in counters
)
epsilon = "".join(
    "1" if b=="0" else "0"
    for b in gamma
)

print(gamma)
print(epsilon)

print((int(gamma, base=2) * int(epsilon, base=2)))

# part 2

remaining = lines.copy()
for i in range(N_BITS):
    counter = Counter(line[i] for line in remaining)
    b = "1" if counter["1"] >= counter["0"] else "0"
    remaining = [line
        for line in remaining
        if line[i] == b
    ]
    if len(remaining) == 1:
        oxygen = remaining[0]
        break
else:
    raise RuntimeError("Didn't find it")

remaining = lines.copy()
for i in range(N_BITS):
    counter = Counter(line[i] for line in remaining)
    b = "0" if counter["1"] >= counter["0"] else "1"
    remaining = [line
        for line in remaining
        if line[i] == b
    ]
    if len(remaining) == 1:
        co2 = remaining[0]
        break
else:
    raise RuntimeError("Didn't find it")
print(f"{oxygen=} = {int(oxygen, base=2)}")
print(f"{co2=} = {int(co2, base=2)}")
print(int(oxygen, base=2)*int(co2, base=2))
