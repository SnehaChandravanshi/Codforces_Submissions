import sys
 
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
 
freq = {}
left = 0
max_len = 0
 
for right in range(n):
    freq[a[right]] = freq.get(a[right], 0) + 1
    
    while len(freq) > 2:
        freq[a[left]] -= 1
        if freq[a[left]] == 0:
            del freq[a[left]]
        left += 1
        
    max_len = max(max_len, right - left + 1)
 
print(max_len)