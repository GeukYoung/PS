# 2261. Sweep line

import sys
sys.stdin = open("D:/OneDrive/2. Project/98. PS/code/2261.txt", "r") 
input = sys.stdin.readline

from collections import defaultdict, deque

def BOJ_2261():
    n = int(input())
    pts = []
    for _ in range(n):
        x,y = map(int,input().split())
        pts.append(x + y*1j) # using complex number
    pts = sorted(pts, key=lambda x: x.real)

    min_ = min(abs(pts[i + 1] - pts[i]) for i in range(len(pts) - 1)) # abs is dist in complex
    if min_ in [0,1]:
        return print(round(min_**2))

    group = [int(p.imag // min_) for p in pts]

    candidate = defaultdict(deque)
    start = 0
    for idx, p1 in enumerate(pts):
        while min_ <= p1.real - pts[start].real:
            i = candidate[group[start]].popleft()
            assert start == i, (start, i)
            start += 1

        for k in range(group[idx] - 1, group[idx] + 2):
            if k not in candidate:
                continue
            for i in candidate[k]:
                min_ = min(min_, abs(pts[i] - p1))
        candidate[group[idx]].append(idx)
    print(round(min_**2))
BOJ_2261()