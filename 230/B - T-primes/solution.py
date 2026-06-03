import sys
 
limit = 1000000
is_prime = [True] * (limit + 1)
is_prime[0] = is_prime[1] = False
 
for i in range(2, int(limit**0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, limit + 1, i):
            is_prime[j] = False
 
n = int(input())
numbers = list(map(int, sys.stdin.read().split()))
 
results = []
for num in numbers:
    root = int(num**0.5)
    if root * root == num and is_prime[root]:
        results.append("YES")
    else:
        results.append("NO")
 
print('
'.join(results))