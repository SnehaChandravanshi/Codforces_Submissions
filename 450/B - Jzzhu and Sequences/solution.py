x, y = map(int, input().split())
n = int(input())
MOD = 1000000007
 
seq = [x, y, y - x, -x, -y, x - y]
idx = (n - 1) % 6
 
print(seq[idx] % MOD)