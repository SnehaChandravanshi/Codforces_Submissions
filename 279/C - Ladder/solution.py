import sys
 
input_data = sys.stdin.read().split()
if not input_data:
    exit()
 
n = int(input_data[0])
m = int(input_data[1])
a = [int(x) for x in input_data[2:n+2]]
 
inc = [1] * n
dec = [1] * n
 
for i in range(1, n):
    if a[i] <= a[i-1]:
        dec[i] = dec[i-1] + 1
        
for i in range(n - 2, -1, -1):
    if a[i] <= a[i+1]:
        inc[i] = inc[i+1] + 1
 
idx = n + 2
results = []
for _ in range(m):
    l = int(input_data[idx]) - 1
    r = int(input_data[idx+1]) - 1
    idx += 2
    
    if inc[l] + dec[r] >= r - l + 1:
        results.append("Yes")
    else:
        results.append("No")
 
print('
'.join(results))