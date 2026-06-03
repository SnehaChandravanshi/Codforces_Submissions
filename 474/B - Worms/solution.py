import bisect
 
n = int(input())
a = list(map(int, input().split()))
m = int(input())
q = list(map(int, input().split()))
 
prefix = []
curr = 0
for x in a:
    curr += x
    prefix.append(curr)
 
for x in q:
    print(bisect.bisect_left(prefix, x) + 1)