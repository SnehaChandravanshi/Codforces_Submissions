t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    
    odds = sum(1 for num in a if num % 2 != 0)
    evens = n - odds
    
    possible = False
    for i in range(1, odds + 1, 2):
        if i <= x and (x - i) <= evens:
            possible = True
            break
            
    print("Yes" if possible else "No")