"""
Day 10: Syntax Scoring
"""
from collections import deque
import numpy as np

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

# part 1

def parse(line):
    stack = deque()
    for c in line:
        if c in brackets:
            stack.append(c)
        elif c == brackets[stack[-1]]:
            stack.pop()
        elif c in score:
            return score[c]
        else:
            raise ValueError(line)
    return 0

print(sum(parse(line) for line in lines))


# part 2

score2 = {
    '(': 1, 
    '[': 2,
    '{': 3,
    '<': 4,
}

def complete(line):
    stack = deque()
    for c in line:
        if c in brackets:
            stack.append(c)
        elif c == brackets[stack[-1]]:
            stack.pop()
        elif c in score:
            return 0
        else:
            raise ValueError(line)

    x = 0
    for c in reversed(stack):
        x = 5*x + score2[c]
    return x

ac_scores = []
for line in lines:
    ac_score = complete(line)
    if ac_score:
        ac_scores.append(ac_score)

ac_scores = sorted(ac_scores)
i = int((len(ac_scores))/2)
print(ac_scores[i])
