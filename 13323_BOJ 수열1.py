# 13323. BOJ 수열 1

# 점화식
# Dp[1,k] = |k-A1|
# Dp[n,k] = min(Dp[n-1,k-1],Dp[n-1,k-2],...,Dp[n-1,0]) + |k-An|
# Dp[n,k]는 Dp[n-1,k]를 우측으로 1만큼 shift
# |k-An| term을 더한 후 양의 기울기는 0으로 무시가능 
# (최소값은 음의 기울기에서 발생)

import sys
import heapq

n = int(sys.stdin.readline().strip())
A = list(map(int,sys.stdin.readline().split()))
pq, ans = [], 0
for i in range(n):
    num = i - A[i] # sort invert
    if pq and pq[0] < num:
        ans += (num - pq[0])
        heapq.heappush(pq, num)
        heapq.heappop(pq)
        heapq.heappush(pq, num)
    else:
        heapq.heappush(pq, num)
print(ans)