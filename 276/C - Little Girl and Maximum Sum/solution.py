import sys
 
n, q = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
 
queries = sys.stdin.read().split()
freq = [0] * (n + 1)
 
for i in range(q):
    l = int(queries[2 * i]) - 1
    r = int(queries[2 * i + 1]) - 1
    freq[l] += 1
    freq[r + 1] -= 1
 
for i in range(1, n):
    freq[i] += freq[i - 1]
 
freq = freq[:-1]
freq.sort(reverse=True)
a.sort(reverse=True)
 
max_sum = 0
for i in range(n):
    if freq[i] == 0:
        break
    max_sum += a[i] * freq[i]
 
print(max_sum)