import sys
 
k = int(sys.stdin.readline())
seen = {}
 
for i in range(k):
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    total_sum = sum(a)
    
    for j in range(n):
        val = total_sum - a[j]
        
        if val in seen and seen[val][0] != i + 1:
            print("YES")
            print(f"{seen[val][0]} {seen[val][1]}")
            print(f"{i + 1} {j + 1}")
            sys.exit()
            
        seen[val] = (i + 1, j + 1)
 
print("NO")