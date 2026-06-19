t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    
    def digit_sum(x):
        return sum(int(d) for d in str(x))
        
    if digit_sum(n) <= s:
        print(0)
        continue
        
    ans = 0
    p = 1
    
    while digit_sum(n) > s:
        digit = (n // p) % 10
        add = p * (10 - digit)
        n += add
        ans += add
        p *= 10
        
    print(ans)