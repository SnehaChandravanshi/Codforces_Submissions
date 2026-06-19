import sys
 
n = int(sys.stdin.readline())
trees = []
for _ in range(n):
    trees.append(tuple(map(int, sys.stdin.readline().split())))
 
if n <= 2:
    print(n)
    exit()
 
ans = 2
last_pos = trees[0][0]
 
for i in range(1, n - 1):
    x, h = trees[i]
    if x - h > last_pos:
        ans += 1
        last_pos = x
    elif x + h < trees[i+1][0]:
        ans += 1
        last_pos = x + h
    else:
        last_pos = x
 
print(ans)