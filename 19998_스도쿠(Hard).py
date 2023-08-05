# 19998. 스도쿠 (Hard) dlx 알고리즘

import sys
from itertools import product

def sdoku_DLX(Q):
    R, C = 3, 3
    N = R * C
    X = ([("rc", rc) for rc in product(range(N), range(N))] +
         [("rn", rn) for rn in product(range(N), range(1, N + 1))] +
         [("cn", cn) for cn in product(range(N), range(1, N + 1))] +
         [("bn", bn) for bn in product(range(N), range(1, N + 1))])
    Y = dict()
    for r, c, n in product(range(N), range(N), range(1, N + 1)):
        b = (r // R) * R + (c // C) # Box number
        Y[(r, c, n)] = [("rc", (r, c)), ("rn", (r, n)), ("cn", (c, n)), ("bn", (b, n))] # row, col, box num
    X, Y = exact_cover(X, Y)
    for i, row in enumerate(Q):
        for j, n in enumerate(row):
            if n:
                add_num(X, Y, (i, j, n))
    for solution in solve(X, Y, []):
        for (r, c, n) in solution:
            Q[r][c] = n
        yield Q

def exact_cover(X, Y):
    X = {j: set() for j in X}
    for i, row in Y.items():
        for j in row:
            X[j].add(i)
    return X, Y

def solve(X, Y, solution):
    if not X:
        yield list(solution)
    else:
        c = min(X, key=lambda c: len(X[c]))
        for r in list(X[c]):
            solution.append(r)
            cols = add_num(X, Y, r)
            for s in solve(X, Y, solution):
                yield s
            del_num(X, Y, r, cols)
            solution.pop()

def add_num(X, Y, r):
    cols = []
    for j in Y[r]:
        for i in X[j]:
            for k in Y[i]:
                if k != j:
                    X[k].remove(i)
        cols.append(X.pop(j))
    return cols

def del_num(X, Y, r, cols):
    for j in reversed(Y[r]):
        X[j] = cols.pop()
        for i in X[j]:
            for k in Y[i]:
                if k != j:
                    X[k].add(i)

# path = "C:/Users/rmrdu/Downloads/test1.txt"
# sys.stdin = open(path, "r")
Q = [list(map(int,sys.stdin.readline().split())) for _ in range(9)]
for i in sdoku_DLX(Q):
    for j in i:
        print(' '.join(map(str, j)))
    break # only first answer used