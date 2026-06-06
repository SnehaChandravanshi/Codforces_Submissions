t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    max_val = a[0]
    max_diff = 0
    
    for i in range(1, n):
        if a[i] < max_val:
            max_diff = max(max_diff, max_val - a[i])
        else:
            max_val = a[i]
            
    if max_diff == 0:
        print(0)
    else:
        print(max_diff.bit_length())