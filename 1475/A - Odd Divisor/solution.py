import sys
 
t = int(sys.stdin.readline())
queries = sys.stdin.read().split()
results = []
 
for q in queries:
    n = int(q)
    if n & (n - 1) == 0:
        results.append("NO")
    else:
        results.append("YES")
        
print('
'.join(results))