n1, n2, k1, k2 = map(int, input().split())
MOD = 100000000
 
dp = [[[0, 0] for _ in range(n2 + 1)] for __ in range(n1 + 1)]
dp[0][0][0] = 1
dp[0][0][1] = 1
 
for i in range(n1 + 1):
    for j in range(n2 + 1):
        for k in range(1, min(i, k1) + 1):
            dp[i][j][0] = (dp[i][j][0] + dp[i - k][j][1]) % MOD
            
        for k in range(1, min(j, k2) + 1):
            dp[i][j][1] = (dp[i][j][1] + dp[i][j - k][0]) % MOD
 
print((dp[n1][n2][0] + dp[n1][n2][1]) % MOD)