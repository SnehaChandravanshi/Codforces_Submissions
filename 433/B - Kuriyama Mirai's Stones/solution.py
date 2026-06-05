import sys
 
n = int(sys.stdin.readline())
costs = list(map(int, sys.stdin.readline().split()))
 
sorted_costs = sorted(costs)
 
pref1 = [0] * (n + 1)
pref2 = [0] * (n + 1)
 
for i in range(n):
    pref1[i + 1] = pref1[i] + costs[i]
    pref2[i + 1] = pref2[i] + sorted_costs[i]
 
m = int(sys.stdin.readline())
queries = sys.stdin.read().split()
 
results = []
for i in range(m):
    type_q = int(queries[3 * i])
    l = int(queries[3 * i + 1])
    r = int(queries[3 * i + 2])
    
    if type_q == 1:
        ans = pref1[r] - pref1[l - 1]
    else:
        ans = pref2[r] - pref2[l - 1]
    results.append(str(ans))
 
print('
'.join(results))