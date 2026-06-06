t = int(input())
for _ in range(t):
    n = int(input())
    y = n % 2020
    x_plus_y = n // 2020
    
    if y <= x_plus_y:
        print("YES")
    else:
        print("NO")