"""
Day 8: Seven Segment Search
"""
from collections import Counter

def parse(line):
    codes, input = line.strip().split(" | ")
    return codes.split(), input.split()

with open("data/day-08.txt") as f:
    lines = [parse(line) for line in f]

digits = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg",
}

len_to_tr = {}
for v in digits.values():
    len_to_tr.setdefault(len(v), set()).update(v)

def freq(codes):
    return Counter(letter
        for code in codes
            for letter in code)

def invert_dict(d):
    inv = {}
    for k,v in d.items():
        inv.setdefault(v, set()).add(k)
    return inv

letter_freq = freq(digits.values())
inv_letter_freq = invert_dict(letter_freq)

inv_digits = {v:k for k,v in digits.items()}

tr = {
    'a': 'abcdefg',
    'b': 'abcdefg',
    'c': 'abcdefg',
    'd': 'abcdefg',
    'e': 'abcdefg',
    'f': 'abcdefg',
    'g': 'abcdefg',
}

def tr_by_freq(codes):
    code_letter_freq = freq(codes)
    return {k:inv_letter_freq[count] for k,count in code_letter_freq.items()}

def tr_by_count(codes):
    tr = {}
    for code in codes:
       poss_tr = len_to_tr[len(code)]
       for letter in code:
           tr[letter] = tr.get(letter, set("abcdefg")) & poss_tr
    return tr

def elim(tr):
    while True:
        onlys = set(next(iter(x)) for x in tr.values() if len(x)==1)
        if len(onlys) == 7:
            return tr
        new_tr = {k:(v if len(v)==1 else v-onlys) for k,v in tr.items()}
        if new_tr == tr:
            return tr
        tr = new_tr

def collapse_sets(tr):
    return {k:next(iter(v)) for k,v in tr.items()}

def to_num(input, tr):
    return inv_digits.get("".join(sorted(tr[x] for x in input)))

counter = Counter()
total = 0
for codes, inputs in lines:
    tr1 = tr_by_freq(codes)
    tr2 = tr_by_count(codes)

    tr = {x:(tr1[x] & tr2[x]) for x in "abcdefg"}
    tr = collapse_sets(elim(tr))

    nums = [to_num(input, tr) for input in inputs]
    print(nums)

    counter.update(nums)

    total += int("".join(str(d) for d in nums))

print(counter)
print("part 1 =", sum(counter[x] for x in [1,4,7,8]))
print("part 2 =", total)
