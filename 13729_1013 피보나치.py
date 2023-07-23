# 13729. 1013 피보나치 (pesano period & 분할정복 & 피보나치 행렬곱)

import sys

def Mat_mul(A, B, M):
    C = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j] += (A[i][k] * B[k][j])
                C[i][j] %= M
    return C

def Pesano(k):
    M, P = 10**k, 15*(10**(k-1))
    return M, P

def Fibo_gen(idx, M):
    mat_ans = [[1, 0], [0, 1]]
    mat_unit = [[1, 1], [1, 0]]

    while idx > 0:
        if idx & 1:
            mat_ans = Mat_mul(mat_ans, mat_unit, M)
        mat_unit = Mat_mul(mat_unit, mat_unit, M)
        idx >>= 1
    return mat_ans[1][0]

def Pesano_period(M,P,N):
    n_modeM = N % M
    a, b, c = 1, 0, 1
    candidate = []
    if N == 0:
        candidate.append(0)
    elif N == 1:
        candidate.append(1)
    for i in range(2,P+1):
        c = (a + b) % M
        b = a
        a = c
        if n_modeM == c:
            candidate.append(i) # put 0 in first idx
    return candidate

def solve(N):
    k = 3
    M,P = Pesano(k)
    candidate = Pesano_period(M,P,N) # minimum pesano(k=3) candidate
    M *= 10 # compare with next mod
    for k in range(3,13):
        temp = []
        for idx in candidate:
            for m in range(10):
                if Fibo_gen(idx + m*P, M)%M == N % M:
                    temp.append(idx + m*P)
        candidate = temp[:]
        M, P = M*10, P*10 # bottom-top
    print(-1 if (len(candidate) == 0)|(N==10**13) else min(candidate))

N = int(input())
solve(N)