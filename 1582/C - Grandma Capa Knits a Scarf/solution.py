import sys
 
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    
    best_deletions = float('inf')
    
    for char_code in range(97, 123):
        target = chr(char_code)
        left = 0
        right = n - 1
        deletions = 0
        possible = True
        
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            elif s[left] == target:
                left += 1
                deletions += 1
            elif s[right] == target:
                right -= 1
                deletions += 1
            else:
                possible = False
                break
                
        if possible:
            best_deletions = min(best_deletions, deletions)
            
    if best_deletions == float('inf'):
        print(-1)
    else:
        print(best_deletions)