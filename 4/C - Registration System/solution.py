import sys
 
n = int(sys.stdin.readline())
database = {}
results = []
 
for _ in range(n):
    name = sys.stdin.readline().strip()
    if name in database:
        database[name] += 1
        results.append(f"{name}{database[name]}")
    else:
        database[name] = 0
        results.append("OK")
 
print('
'.join(results))