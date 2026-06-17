import sys
 
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
total = sum(a)
 
if total % 3 != 0:
    print(0)
else:
    target = total // 3
    ways = 0
    ans = 0
    curr = 0
    
    for i in range(n - 1):
        curr += a[i]
        if curr == 2 * target:
            ans += ways
        if curr == target:
            ways += 1
            
    print(ans)