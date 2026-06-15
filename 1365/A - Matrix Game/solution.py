t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    
    free_rows = 0
    for i in range(n):
        if 1 not in grid[i]:
            free_rows += 1
            
    free_cols = 0
    for j in range(m):
        has_one = False
        for i in range(n):
            if grid[i][j] == 1:
                has_one = True
                break
        if not has_one:
            free_cols += 1
            
    moves = min(free_rows, free_cols)
    
    if moves % 2 == 1:
        print("Ashish")
    else:
        print("Vivek")