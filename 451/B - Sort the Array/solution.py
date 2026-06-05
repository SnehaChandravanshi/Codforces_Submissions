n = int(input())
a = list(map(int, input().split()))
 
sorted_a = sorted(a)
 
left = 0
while left < n and a[left] == sorted_a[left]:
    left += 1
 
right = n - 1
while right >= 0 and a[right] == sorted_a[right]:
    right -= 1
 
if left >= right:
    print("yes
1 1")
else:
    segment = a[left:right + 1]
    segment.reverse()
    
    if a[:left] + segment + a[right + 1:] == sorted_a:
        print("yes")
        print(f"{left + 1} {right + 1}")
    else:
        print("no")