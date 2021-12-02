"""
"""
import re

def parse_cmd(line):
    m = re.match(r"(\w+) (\d+)", line.strip())
    return m.group(1), int(m.group(2))

with open("data/day-02.txt") as f:
    cmds = [parse_cmd(line) for line in f]

# part 1

x = 0
y = 0

for cmd, arg in cmds:
    if cmd == "up":
        y -= arg
    elif cmd == "down":
        y += arg
    elif cmd == "forward":
        x += arg
    else:
        raise ValueError(f"Unexpected command: '{cmd}'.")

print(x*y)

# part 2

x = 0
y = 0
aim = 0

for cmd, arg in cmds:
    if cmd == "up":
        aim -= arg
    elif cmd == "down":
        aim += arg
    elif cmd == "forward":
        x += arg
        y += aim * arg
    else:
        raise ValueError(f"Unexpected command: '{cmd}'.")

print(x*y)
