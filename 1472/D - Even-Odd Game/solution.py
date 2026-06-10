import sys
 
input_data = sys.stdin.read().split()
if not input_data:
    exit()
 
t = int(input_data[0])
idx = 1
results = []
 
for _ in range(t):
    n = int(input_data[idx])
    idx += 1
    a = sorted([int(x) for x in input_data[idx:idx+n]], reverse=True)
    idx += n
    
    alice = 0
    bob = 0
    
    for i in range(n):
        if i % 2 == 0:
            if a[i] % 2 == 0:
                alice += a[i]
        else:
            if a[i] % 2 != 0:
                bob += a[i]
                
    if alice > bob:
        results.append("Alice")
    elif bob > alice:
        results.append("Bob")
    else:
        results.append("Tie")
 
print('
'.join(results))