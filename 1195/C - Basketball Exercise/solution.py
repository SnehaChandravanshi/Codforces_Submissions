import sys
 
n = int(sys.stdin.readline())
h1 = list(map(int, sys.stdin.readline().split()))
h2 = list(map(int, sys.stdin.readline().split()))
 
dp1 = 0
dp2 = 0
 
for i in range(n):
    dp1, dp2 = max(dp1, dp2 + h1[i]), max(dp2, dp1 + h2[i])
 
print(max(dp1, dp2))