# 1307. 마방진
# import numpy as np
# import matplotlib.pyplot as plt

def magic(n):
    if n % 2 == 1:
        # Odd order
        M = oddMagic(n)
    elif n % 4 == 0:
        # Doubly even order
        J = [(i % 4) // 2 for i in range(1, n + 1)]
        K = [[J[i] == J[j] for j in range(n)] for i in range(n)]
        M = [[i + 1 + j * n for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                if K[i][j]:
                    M[i][j] = n * n + 1 - M[i][j]
    else:
        # Singly even order
        p = n // 2  # p is odd.
        M = oddMagic(p)
        M = [M[i] + [M[i][j] + 2 * p * p for j in range(p)] for i in range(p)]
        M += [[M[i][j] + 3 * p * p for j in range(p)] + [M[i][j] + p * p for j in range(p)] for i in range(p)]
        if n == 2:
            return M
        i = list(range(p))
        k = (n - 2) // 4
        j = list(range(k)) + list(range(n-k+1,n))
        i_p = i + [x+p for x in i]
        p_i = [x+p for x in i] + i
        for y in j:
            for x in range(n//2):
                M[i_p[x]][y], M[p_i[x]][y] = M[p_i[x]][y], M[i_p[x]][y]
        i = k
        j = [0] + [i]
        for y in j:
            M[i][y], M[i+p][y] = M[i+p][y], M[i][y]
    return M

def oddMagic(n):
    p = [i + 1 for i in range(n)]
    M = [[n * ((p[i] + p[j] - (n + 3) // 2) % n) + (p[i] + 2 * p[j] - 2) % n + 1 for j in range(n)] for i in range(n)]
    return M

N = int(input())
# temp = np.array(magic(N))
# plt.plot(list(temp.sum(axis=0)) + list(temp.sum(axis=1)) + [sum(np.diag(temp,k=0))] + [sum(np.diag(temp.transpose(),k=0))])
# plt.ylim([sum(np.diag(temp,k=0))-1, sum(np.diag(temp,k=0))+1])
for line in magic(N):
    print (' '.join(map(str, line)))