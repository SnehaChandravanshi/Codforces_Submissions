n = int(input())
a = list(map(int, input().split()))
 
seq = [4, 8, 15, 16, 23, 42]
pos = {seq[i]: i for i in range(6)}
counts = [0] * 6
 
for x in a:
    if x not in pos:
        continue
    idx = pos[x]
    
    if idx == 0:
        counts[0] += 1
    else:
        if counts[idx - 1] > 0:
            counts[idx - 1] -= 1
            counts[idx] += 1
 
print(n - counts[5] * 6)