t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    
    prefix_counts = {0: 1}
    current_sum = 0
    ans = 0
    
    for char in s:
        val = int(char) - 1
        current_sum += val
        
        ans += prefix_counts.get(current_sum, 0)
        prefix_counts[current_sum] = prefix_counts.get(current_sum, 0) + 1
        
    print(ans)