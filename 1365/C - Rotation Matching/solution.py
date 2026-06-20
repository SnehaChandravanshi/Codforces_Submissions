import sys
 
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
 
pos_a = [0] * (n + 1)
for i in range(n):
    pos_a[a[i]] = i
    
shifts = [0] * n
for i in range(n):
    target_val = b[i]
    orig_pos = pos_a[target_val]
    shift = (i - orig_pos) % n
    shifts[shift] += 1
    
print(max(shifts))