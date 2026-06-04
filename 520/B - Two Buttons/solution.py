n, m = map(int, input().split())
clicks = 0
 
while m > n:
    if m % 2 == 0:
        m //= 2
    else:
        m += 1
    clicks += 1
 
print(clicks + n - m)