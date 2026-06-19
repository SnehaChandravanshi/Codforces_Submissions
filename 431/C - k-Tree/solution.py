n, k, d = map(int, input().split())
MOD = 1000000007
 
dp = [[0, 0] for _ in range(n + 1)]
dp[0][0] = 1
 
for i in range(1, n + 1):
    for j in range(1, k + 1):
        if i - j >= 0:
            if j >= d:
                dp[i][1] = (dp[i][1] + dp[i-j][0] + dp[i-j][1]) % MOD
            else:
                dp[i][0] = (dp[i][0] + dp[i-j][0]) % MOD
                dp[i][1] = (dp[i][1] + dp[i-j][1]) % MOD
                
print(dp[n][1])