t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    
    leftover_odd = n - (k - 1)
    if leftover_odd > 0 and leftover_odd % 2 != 0:
        print("YES")
        print("1 " * (k - 1) + str(leftover_odd))
        continue
        
    leftover_even = n - 2 * (k - 1)
    if leftover_even > 0 and leftover_even % 2 == 0:
        print("YES")
        print("2 " * (k - 1) + str(leftover_even))
        continue
        
    print("NO")