# 11003. 최솟값 찾기 (que)

from collections import deque
import sys
input = sys.stdin.readline
    
n, m = map(int,input().split(' '))
l = list(map(int,input().split(' ')))

que = deque()

for i in range(n):
    while que and que[0][0] <= i-m:
        que.popleft()
        
    while que and que[-1][1] >= l[i]:
        que.pop()
        
    que.append((i,l[i]))
    print(que[0][1], end=' ')
    