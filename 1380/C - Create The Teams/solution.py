import sys
 
input_data = sys.stdin.read().split()
if not input_data:
    exit()
 
t = int(input_data[0])
idx = 1
results = []
 
for _ in range(t):
    n = int(input_data[idx])
    x = int(input_data[idx+1])
    idx += 2
    
    a = sorted([int(v) for v in input_data[idx:idx+n]], reverse=True)
    idx += n
    
    teams = 0
    count = 0
    
    for skill in a:
        count += 1
        if skill * count >= x:
            teams += 1
            count = 0
            
    results.append(str(teams))
 
print('
'.join(results))