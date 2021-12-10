"""
Day 10: Syntax Scoring
"""
from collections import deque

with open("data/day-10.txt") as f:
    lines = [line.strip() for line in f]

brackets = {
    '(': ')', 
    '[': ']',
    '{': '}',
    '<': '>',
}
score = {
    ')': 3, 
    ']': 57,
    '}': 1197,
    '>': 25137,
}
ac_score = {
    '(': 1, 
    '[': 2,
    '{': 3,
    '<': 4,
}

def parse(line):
    stack = deque()
    for c in line:
        if c in brackets:
            stack.append(c)
        elif c == brackets[stack[-1]]:
            stack.pop()
        elif c in score:
            return score[c], 0
        else:
            raise ValueError(line)
    else:
        x = 0
        for c in reversed(stack):
            x = 5*x + ac_score[c]
        return 0, x

scores = [parse(line) for line in lines]

print("part 1:", sum(sc[0] for sc in scores))

ac_scores = sorted(sc[1] for sc in scores if sc[1])
print("part 2:", ac_scores[len(ac_scores)//2])
