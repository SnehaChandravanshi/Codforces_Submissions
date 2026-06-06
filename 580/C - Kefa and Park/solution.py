import sys
from collections import deque
 
n, m = map(int, sys.stdin.readline().split())
cats = [0] + list(map(int, sys.stdin.readline().split()))
 
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
 
queue = deque([(1, cats[1])])
visited = [False] * (n + 1)
visited[1] = True
 
valid_restaurants = 0
 
while queue:
    node, consecutive_cats = queue.popleft()
    
    is_leaf = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            is_leaf = False
            visited[neighbor] = True
            
            next_cats = consecutive_cats + 1 if cats[neighbor] else 0
            if next_cats <= m:
                queue.append((neighbor, next_cats))
                
    if is_leaf:
        valid_restaurants += 1
 
print(valid_restaurants)