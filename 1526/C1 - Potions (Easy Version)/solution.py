import sys
import heapq
 
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
 
health = 0
potions = 0
min_heap = []
 
for x in a:
    health += x
    potions += 1
    heapq.heappush(min_heap, x)
    
    if health < 0:
        health -= heapq.heappop(min_heap)
        potions -= 1
 
print(potions)