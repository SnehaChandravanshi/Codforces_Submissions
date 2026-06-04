n = int(input())
groups = list(map(int, input().split()))
 
# Count how many groups of size 1, 2, 3, and 4 we have
counts = [0] * 5
for g in groups:
    counts[g] += 1
 
taxis = counts[4]
 
# Match 3s with 1s
taxis += counts[3]
counts[1] = max(0, counts[1] - counts[3])
 
# Pair up 2s
taxis += counts[2] // 2
if counts[2] % 2 != 0:
    taxis += 1
    counts[1] = max(0, counts[1] - 2)
 
# Pack remaining 1s (4 per taxi)
if counts[1] > 0:
    taxis += (counts[1] + 3) // 4
 
print(taxis)