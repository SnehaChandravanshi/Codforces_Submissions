t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    
    sheep_positions = []
    for i in range(n):
        if s[i] == '*':
            sheep_positions.append(i)
            
    k = len(sheep_positions)
    if k == 0:
        print(0)
        continue
        
    median_idx = k // 2
    target_pos = sheep_positions[median_idx]
    moves = 0
    
    for i in range(k):
        actual_pos = sheep_positions[i]
        expected_pos = target_pos - median_idx + i
        moves += abs(actual_pos - expected_pos)
        
    print(moves)