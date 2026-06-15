t = int(input())
for _ in range(t):
    n, x, y = map(int, input().split())
    diff = y - x
    step = 1
    
    for d in range(1, diff + 1):
        if diff % d == 0 and diff // d + 1 <= n:
            step = d
            break
            
    ans = []
    curr = y
    while len(ans) < n and curr > 0:
        ans.append(curr)
        curr -= step
        
    curr = y + step
    while len(ans) < n:
        ans.append(curr)
        curr += step
        
    print(" ".join(map(str, sorted(ans))))