n = int(input())
a = list(map(int, input().split()))
 
counts = [0] * 100005
for x in a:
    counts[x] += 1
 
dp = [0] * 100005
dp[1] = counts[1]
 
for i in range(2, 100005):
    dp[i] = max(dp[i-1], dp[i-2] + counts[i] * i)
 
print(dp[100000])