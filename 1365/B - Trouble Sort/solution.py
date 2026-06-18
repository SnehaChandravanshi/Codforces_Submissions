t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    if a == sorted(a):
        print("Yes")
    elif 0 in b and 1 in b:
        print("Yes")
    else:
        print("No")