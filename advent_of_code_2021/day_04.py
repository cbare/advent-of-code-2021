"""
Day 04 - Squid Bingo
"""
import numpy as np

with open("data/day-04.txt") as f:
    nums = [int(x) for x in next(f).strip().split(",")]
    next(f)

    boards = []
    acc = []
    for line in f:
        if line.strip() == "" and len(acc) > 0:
            boards.append(np.array(acc))
            acc.clear()
        else:
            acc.append([int(x) for x in line.split()])

def win(marks):
    n,m = marks.shape
    # win if any row or any column is complete
    return any(
        all(marks[i,j] for i in range(n))
        for j in range(m)
    ) or any(
        all(marks[i,j] for j in range(m))
        for i in range(n)
    )

def test_win():
    assert win(np.ones((5,5)))
    assert not win(np.zeros((5,5)))

    a = np.random.random_integers(0,1,(5,5))
    print(a)
    print(win(a))

def score(board, marks, n):
    return (board * ~marks).sum() * n


# part 1

marks = [np.full(board.shape, False) for board in boards]

def play(boards, marks, nums):
    for n in nums:
        for i,board,mark in zip(range(len(boards)), boards, marks):
            mark[np.where(board==n)] = True
            if win(mark):
                winning_score = score(board, mark, n)
                print(f"board {i} wins with a score of {winning_score}!")
                return

play(boards, marks, nums)


# part 2

marks = [np.full(board.shape, False) for board in boards]

def play(boards, marks, nums):
    won = set()
    for n in nums:
        for i,board,mark in zip(range(len(boards)), boards, marks):
            if i in won:
                continue
            mark[np.where(board==n)] = True
            if win(mark):
                won.add(i)
                if len(won) == len(boards):
                    winning_score = score(board, mark, n)
                    print(f"board {i} was last to win with a score of {winning_score}!")
                    return

play(boards, marks, nums)

