t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    counts = [0, 0, 0]
    for num in a:
        counts[num % 3] += 1
        
    target = n // 3
    moves = 0
    
    for i in range(6):
        curr = i % 3
        next_rem = (i + 1) % 3
        
        if counts[curr] > target:
            excess = counts[curr] - target
            counts[curr] -= excess
            counts[next_rem] += excess
            moves += excess
            
    print(moves)