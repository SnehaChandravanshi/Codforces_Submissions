import sys
 
t = int(sys.stdin.readline())
out = []
 
for _ in range(t):
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    
    freq = {}
    for x in a:
        freq[x] = freq.get(x, 0) + 1
        
    counts = sorted(list(freq.values()))
    m = len(counts)
    min_remove = n
    
    for i in range(m):
        kept = counts[i] * (m - i)
        min_remove = min(min_remove, n - kept)
        
    out.append(str(min_remove))
 
print('
'.join(out))