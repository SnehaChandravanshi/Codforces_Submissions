import sys
 
s = sys.stdin.readline().strip()
m = int(sys.stdin.readline())
queries = sys.stdin.read().split()
 
n = len(s)
prefix = [0] * n
 
for i in range(1, n):
    prefix[i] = prefix[i - 1] + (1 if s[i] == s[i - 1] else 0)
 
results = []
for i in range(m):
    l = int(queries[2 * i]) - 1
    r = int(queries[2 * i + 1]) - 1
    results.append(str(prefix[r] - prefix[l]))
 
print('
'.join(results))