import sys
 
n, k = map(int, sys.stdin.readline().split())
a = sorted(list(map(int, sys.stdin.readline().split())))
 
valid = set()
ans = 0
 
for x in a:
    if x % k != 0 or (x // k) not in valid:
        valid.add(x)
        ans += 1
 
print(ans)