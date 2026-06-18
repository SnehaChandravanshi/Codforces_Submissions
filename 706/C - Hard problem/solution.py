import sys
 
n = int(sys.stdin.readline())
c = list(map(int, sys.stdin.readline().split()))
s = [sys.stdin.readline().strip() for _ in range(n)]
rev_s = [x[::-1] for x in s]
 
INF = float('inf')
dp = [[INF, INF] for _ in range(n)]
dp[0][0] = 0
dp[0][1] = c[0]
 
for i in range(1, n):
    if s[i] >= s[i-1]:
        dp[i][0] = min(dp[i][0], dp[i-1][0])
    if s[i] >= rev_s[i-1]:
        dp[i][0] = min(dp[i][0], dp[i-1][1])
        
    if rev_s[i] >= s[i-1]:
        dp[i][1] = min(dp[i][1], dp[i-1][0] + c[i])
    if rev_s[i] >= rev_s[i-1]:
        dp[i][1] = min(dp[i][1], dp[i-1][1] + c[i])
        
ans = min(dp[n-1][0], dp[n-1][1])
print(ans if ans != INF else -1)