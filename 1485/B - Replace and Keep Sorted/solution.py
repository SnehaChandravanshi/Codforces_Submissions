import sys
 
input_data = sys.stdin.read().split()
if not input_data:
    exit()
 
n = int(input_data[0])
q = int(input_data[1])
k = int(input_data[2])
 
a = [int(x) for x in input_data[3:n+3]]
idx = n + 3
results = []
 
for _ in range(q):
    l = int(input_data[idx]) - 1
    r = int(input_data[idx+1]) - 1
    idx += 2
    
    ans = k + a[r] - a[l] - 2 * (r - l) - 1
    results.append(str(ans))
 
print('
'.join(results))