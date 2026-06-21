import sys
 
input_data = sys.stdin.read().split()
if not input_data:
    exit()
 
t = int(input_data[0])
k = int(input_data[1])
MOD = 1000000007
MAX_N = 100005
 
dp = [0] * MAX_N
dp[0] = 1
 
for i in range(1, MAX_N):
    dp[i] = dp[i-1]
    if i >= k:
        dp[i] = (dp[i] + dp[i-k]) % MOD
 
pref = [0] * MAX_N
for i in range(1, MAX_N):
    pref[i] = (pref[i-1] + dp[i]) % MOD
 
idx = 2
results = []
for _ in range(t):
    a = int(input_data[idx])
    b = int(input_data[idx+1])
    idx += 2
    
    ans = (pref[b] - pref[a-1] + MOD) % MOD
    results.append(str(ans))
 
print('
'.join(results))