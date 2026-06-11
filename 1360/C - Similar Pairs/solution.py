t = int(input())
for _ in range(t):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    
    odds = sum(1 for x in a if x % 2 != 0)
    
    if odds % 2 == 0:
        print("YES")
    else:
        has_diff_one = False
        for i in range(1, n):
            if a[i] - a[i - 1] == 1:
                has_diff_one = True
                break
        print("YES" if has_diff_one else "NO")