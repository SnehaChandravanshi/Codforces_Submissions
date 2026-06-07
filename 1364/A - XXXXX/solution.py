t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    
    total_sum = sum(a)
    if total_sum % x != 0:
        print(n)
        continue
        
    left_idx = -1
    right_idx = -1
    
    for i in range(n):
        if a[i] % x != 0:
            left_idx = i
            break
            
    for i in range(n - 1, -1, -1):
        if a[i] % x != 0:
            right_idx = i
            break
            
    if left_idx == -1:
        print(-1)
    else:
        print(max(n - 1 - left_idx, right_idx))