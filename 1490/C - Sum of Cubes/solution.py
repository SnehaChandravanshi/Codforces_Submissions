import sys
 
t = int(sys.stdin.readline())
queries = sys.stdin.read().split()
 
cubes = set()
for i in range(1, 10001):
    cubes.add(i**3)
 
results = []
for q in queries:
    x = int(q)
    found = False
    
    for i in range(1, int(x**(1/3)) + 2):
        a3 = i**3
        b3 = x - a3
        if b3 in cubes:
            found = True
            break
            
    if found:
        results.append("YES")
    else:
        results.append("NO")
 
print('
'.join(results))