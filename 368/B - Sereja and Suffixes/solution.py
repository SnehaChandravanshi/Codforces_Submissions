n, m = map(int, input().split())
a = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]
 
distinct_counts = [0] * n
seen = set()
 
for i in range(n - 1, -1, -1):
    seen.add(a[i])
    distinct_counts[i] = len(seen)
 
for q in queries:
    print(distinct_counts[q - 1])