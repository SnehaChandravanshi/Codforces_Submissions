n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
 
c = [a[i] - b[i] for i in range(n)]
c.sort()
 
ans = 0
left = 0
right = n - 1
 
while left < right:
    if c[left] + c[right] > 0:
        ans += right - left
        right -= 1
    else:
        left += 1
 
print(ans)