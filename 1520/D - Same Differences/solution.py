t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    counts = {}
    ans = 0
    
    for i, x in enumerate(a):
        val = x - i
        ans += counts.get(val, 0)
        counts[val] = counts.get(val, 0) + 1
        
    print(ans)