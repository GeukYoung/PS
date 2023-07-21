# 5615. 아파트 임대 (확률소수론)

import sys

def isprime(n):
    a_base = [2, 3, 5, 7, 11, 13]
    if n < a_base[-1]:
        if n in a_base:
            return True
        else:
            return False
    else:
        for i in a_base:
            if fermat(i,n) != 1:
                return False
        return True

def fermat(a,n):
    r,d = 0,n-1
    while d%2 == 0: r += 1; d //= 2
    x = pow(a,d,n)
    if x == 1 or x+1 == n: return True
    for i in range(0, r-1):
        x = pow(x,2,n)
        if x+1 == n: return True
    return False

n_length = int(sys.stdin.readline())
cnt = 0
for _ in range(n_length):
    if(isprime(2*int(sys.stdin.readline())+1)): cnt += 1
print(cnt)