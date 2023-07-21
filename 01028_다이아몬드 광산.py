# 1028. 다이아몬드 광산 (dp)

import sys
import time
R, C = map(int,sys.stdin.readline().split())
l = [[0] + list(map(int,sys.stdin.readline().rstrip())) + [0] for _ in range(R)]
l.insert(0, [0] * len(l[0]))
l.append([0] * len(l[0]))

d_lu = [[0]*(C+2) for _ in range(R+2)]
d_ru = [[0]*(C+2) for _ in range(R+2)]
d_ld = [[0]*(C+2) for _ in range(R+2)]
d_rd = [[0]*(C+2) for _ in range(R+2)]
max_d = 0

for i in range(1,R+1):
    for j in range(1,C+1):
        if l[i][j] == 1:
            d_lu[i][j] = d_lu[i-1][j-1] + 1
            d_ru[i][j] = d_ru[i-1][j+1] + 1

for i in range(R,0,-1):
    for j in range(1,C+1):
        if l[i][j] == 1:
            d_ld[i][j] = d_ld[i+1][j-1] + 1
            d_rd[i][j] = d_rd[i+1][j+1] + 1

for i in range(1,R+1):
    for j in range(1,C+1):
        sz_d = min([d_ld[i][j], d_rd[i][j]])
        if sz_d > max_d:
            for k in range(sz_d,max_d,-1):
                pos_l = i+2*(k-1)
                if pos_l < R+1:
                    if (min([d_lu[pos_l][j], d_ru[pos_l][j]]) >= k) & (k > max_d):
                        max_d = k
print(max_d)