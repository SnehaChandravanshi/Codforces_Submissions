import sys
 
input_data = sys.stdin.read().split()
if not input_data:
    exit()
 
t = int(input_data[0])
idx = 1
results = []
 
for _ in range(t):
    n = int(input_data[idx])
    k = int(input_data[idx+1])
    idx += 2
    
    a = [int(x) for x in input_data[idx:idx+n]]
    idx += n
    
    rem_counts = {}
    max_val = 0
    
    for num in a:
        rem = num % k
        if rem != 0:
            needed = k - rem
            rem_counts[needed] = rem_counts.get(needed, 0) + 1
            current_val = needed + (rem_counts[needed] - 1) * k
            if current_val > max_val:
                max_val = current_val
                
    if max_val == 0:
        results.append("0")
    else:
        results.append(str(max_val + 1))
 
print('
'.join(results))