n, length = map(int, input().split())
lanterns = list(map(int, input().split()))
 
lanterns.sort()
 
max_gap = 0
for i in range(1, n):
    gap = lanterns[i] - lanterns[i - 1]
    if gap > max_gap:
        max_gap = gap
 
radius_between = max_gap / 2.0
radius_start = lanterns[0]
radius_end = length - lanterns[-1]
 
min_radius = max(radius_between, radius_start, radius_end)
 
print(f"{min_radius:.10f}")