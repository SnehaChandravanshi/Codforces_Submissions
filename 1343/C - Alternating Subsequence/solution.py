import sys
 
input_data = sys.stdin.read().split()
if not input_data:
    exit()
 
t = int(input_data[0])
idx = 1
results = []
 
for _ in range(t):
    n = int(input_data[idx])
    idx += 1
    
    max_sum = 0
    current_max = int(input_data[idx])
    
    for i in range(1, n):
        val = int(input_data[idx + i])
        if (val > 0 and current_max > 0) or (val < 0 and current_max < 0):
            if val > current_max:
                current_max = val
        else:
            max_sum += current_max
            current_max = val
            
    max_sum += current_max
    results.append(str(max_sum))
    idx += n
 
print('
'.join(results))