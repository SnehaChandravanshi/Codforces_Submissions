import sys
 
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    
    total_xor = 0
    for num in a:
        total_xor ^= num
        
    if total_xor == 0:
        print("YES")
    else:
        curr = 0
        count = 0
        for num in a:
            curr ^= num
            if curr == total_xor:
                count += 1
                curr = 0
                
        if count >= 3:
            print("YES")
        else:
            print("NO")