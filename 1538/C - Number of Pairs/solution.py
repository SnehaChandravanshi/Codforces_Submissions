import sys
import bisect
 
input_data = sys.stdin.read().split()
if not input_data: 
    exit()
 
t = int(input_data[0])
idx = 1
results = []
 
for _ in range(t):
    n = int(input_data[idx])
    l = int(input_data[idx+1])
    r = int(input_data[idx+2])
    idx += 3
    
    a = []
    for _ in range(n):
        a.append(int(input_data[idx]))
        idx += 1
        
    a.sort()
    count = 0
    
    for i in range(n):
        x = a[i]
        min_y = l - x
        max_y = r - x
        
        left_idx = max(i + 1, bisect.bisect_left(a, min_y))
        right_idx = bisect.bisect_right(a, max_y)
        
        if right_idx > left_idx:
            count += right_idx - left_idx
            
    results.append(str(count))
 
print('
'.join(results))