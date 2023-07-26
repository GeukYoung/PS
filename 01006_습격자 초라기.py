import sys

E_max = 10000
IN, OUT, BOTH = 0, 1, 2

def init_dp():
    dp = [[0]*3 for _ in range(N)]
    dp[0][OUT], dp[0][IN],dp[0][BOTH] = 1, 1, 2
    return dp

def find_N(dp, E_in, E_out):
    if E_out[0] + E_in[0] <= W: dp[0][BOTH] = 1
    for i in range(1, N):
        N_in = 1 if E_in[i-1] + E_in[i] <= W else 2
        N_out = 1 if E_out[i-1] + E_out[i] <= W else 2
        N_both = 1 if E_out[i] + E_in[i] <= W else 2
        
        dp[i][IN] = min(dp[i-1][BOTH] + 1, dp[i-1][OUT] + N_in)
        # sel min/  dp[BOTH] +  1 /vs. dp[OUT] + N_in(1 or 2)
        # Out: Both[1][1][1]         Out[1][1][1]
        # In :  n-1[1][1][1] + [1]   n-1[1][1] + [0  1]
        
        dp[i][OUT] = min(dp[i-1][BOTH] + 1, dp[i-1][IN] + N_out)
        # sel min/  dp[BOTH] +  1 /vs.  dp[IN] + N_out(1 or 2)
        # Out: Both[1][1][1] + [1]    In[1][1] + [0  1]
        # In :  n-1[1][1][1]         n-1[1][1][1]
        
        dp[i][BOTH] = min(dp[i-1][BOTH] + N_both, dp[i-2][BOTH] + N_out + N_in, dp[i-1][IN] + 1 + N_out, dp[i-1][OUT] + 1 + N_in)
        # sel min/  dp[BOTH] + N_both /vs.   dp[BOTH] + N_in&out(2 ~ 4) /vs. dp[IN] + 1 + N_out(1 or 2) /vs. dp[OUT] + 1 + N_in(1 or 2)
        # Out: Both[1][1][1] + |0|(1       Both[1][1] + [0  1](2           In[1][1] + [0  1]               OUT[1][1][1] + [1]
        # In :  n-1[1][1][1] + |1|or2)      n-2[1][1] + [0  1] ~4)        n-1[1][1][1] + [1]               n-1[1][1] + [0  1]
    return dp

T = int(sys.stdin.readline().strip())
for _ in range(T):
    N, W = map(int,sys.stdin.readline().split())
    E_in = list(map(int,sys.stdin.readline().split()))
    E_out = list(map(int,sys.stdin.readline().split()))
    ans = N*2
    
    # 0. size = 1
    if N == 1:
        print(1 if E_in[0] + E_out[0] <= W else 2)
        continue
    
    # 1. No connection check
    dp = find_N(init_dp(), E_in[:], E_out[:])
    ans = min(ans, dp[-1][BOTH])
    
    # 2. Outer circle connection check
    if E_out[0] + E_out[-1] <= W:
        dp = find_N(init_dp(), E_in[:], [E_max]+E_out[1:-1]+[E_max])
        ans = min(ans, dp[-1][IN])

    # 3. Inner circle connection check
    if E_in[0] + E_in[-1] <= W:
        dp = find_N(init_dp(), [E_max]+E_in[1:-1]+[E_max], E_out[:])
        ans = min(ans, dp[-1][OUT])

    # 4. Both connection check
    if (E_out[0] + E_out[-1] <= W) & (E_in[0] + E_in[-1] <= W):
        dp = find_N(init_dp(), [E_max]+E_in[1:-1]+[E_max], [E_max]+E_out[1:-1]+[E_max])
        ans = min(ans, dp[-2][BOTH])
    
    print(ans)
