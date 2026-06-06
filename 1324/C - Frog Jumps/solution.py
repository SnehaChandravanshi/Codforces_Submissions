t = int(input())
for _ in range(t):
    s = input().strip()
    max_l = 0
    current_l = 0
    
    for char in s:
        if char == 'L':
            current_l += 1
            max_l = max(max_l, current_l)
        else:
            current_l = 0
            
    print(max_l + 1)