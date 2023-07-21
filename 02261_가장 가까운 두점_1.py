# 2261. Divide and Conquer

import sys
sys.stdin = open("D:/OneDrive/2. Project/98. PS/code/2261.txt", "r") 
n = int(sys.stdin.readline().strip())
pnt = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
pnt.sort()

def dist(a, b): # sqrt of Euclidean distance
    return (a[0] - b[0])**2 + (a[1] - b[1])**2

def DivConq(start, end):
    if start == end:
        return 100000 # maximum range
    elif end - start == 1:
        return dist(pnt[start], pnt[end])

    mid = (start + end) // 2
    min_dist = min(DivConq(start, mid), DivConq(mid, end))
    min_dist_root = min_dist**(1/2) # faster than 33%!
    pnt_grey = []
    for i in range(start, end+1):
        if abs(pnt[i][0] - pnt[mid][0]) < min_dist_root:
            pnt_grey.append(pnt[i])

    pnt_grey.sort(key=lambda x: x[1])

    for i in range(len(pnt_grey)-1):
        for j in range(i+1, len(pnt_grey)):
            if abs(pnt_grey[i][1] - pnt_grey[j][1]) < min_dist_root:
                min_dist = min(min_dist, dist(pnt_grey[i], pnt_grey[j]))
                min_dist_root = min_dist**(1/2)
            else:
                break

    return min_dist

print(DivConq(0, n-1))