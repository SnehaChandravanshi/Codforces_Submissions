import sys
 
n, m = map(int, sys.stdin.readline().split())
languages = [[] for _ in range(n)]
has_language = False
 
for i in range(n):
    data = list(map(int, sys.stdin.readline().split()))
    if data[0] > 0:
        has_language = True
        languages[i] = data[1:]
        
if not has_language:
    print(n)
    exit()
    
parent = list(range(n))
 
def find(i):
    if parent[i] == i:
        return i
    parent[i] = find(parent[i])
    return parent[i]
    
def union(i, j):
    root_i = find(i)
    root_j = find(j)
    if root_i != root_j:
        parent[root_i] = root_j
        
for i in range(n):
    for j in range(i + 1, n):
        if set(languages[i]) & set(languages[j]):
            union(i, j)
            
components = len(set(find(i) for i in range(n)))
print(components - 1)