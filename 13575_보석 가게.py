# 13575. 보석 가게 (FFT)

import sys
import decimal
# import time
def Conv(a, b, digit = 0):
    """by teferi"""
    decimal.setcontext(
        decimal.Context(prec=decimal.MAX_PREC, Emax=decimal.MAX_EMAX))
    if digit == 0:
        digit = min(20, len(str(min(len(a), len(b)) * max(a) * max(b))))
    f = f'0{digit}d'
    a_dec = decimal.Decimal(''.join(format(x, f) for x in a))
    b_dec = decimal.Decimal(''.join(format(x, f) for x in b))
    c_dec = a_dec * b_dec
    total_digit = digit * (len(a) + len(b) - 1)
    c = format(c_dec, f'0{total_digit}f')
    return [int(c[i:i + digit]) for i in range(0, total_digit, digit)]

N, K = map(int, input().split())
a = list(map(int,input().split(' ')))

# N, K = 3, 999
# a = [3,5,11]

cost = [0]*(max(a)+1)
for i in a:
    cost[i] += 1
cost_s = cost
ans = [1]

# start = time.time()
K = bin(K)
for i in K[::-1]:
    if i == '1':
        ans = Conv(ans,cost_s)
        ans = [1 if x > 0 else 0 for x in ans]
    cost_s = Conv(cost_s,cost_s)
    cost_s = [1 if x > 0 else 0 for x in cost_s]
# print(time.time() - start)

ans_list = []
for i, x in enumerate(ans):
    if x != 0:
        print(i, end=' ')