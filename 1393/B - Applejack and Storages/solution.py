import sys
 
input_data = sys.stdin.read().split()
if not input_data:
    exit()
 
n = int(input_data[0])
counts = {}
 
pairs = 0
quads = 0
 
def add_plank(length):
    global pairs, quads
    c = counts.get(length, 0)
    if c % 2 == 1:
        pairs += 1
    if c % 4 == 3:
        quads += 1
        pairs -= 2
    counts[length] = c + 1
 
def remove_plank(length):
    global pairs, quads
    c = counts[length]
    if c % 2 == 0:
        pairs -= 1
    if c % 4 == 0:
        quads -= 1
        pairs += 2
    counts[length] = c - 1
 
for i in range(1, n + 1):
    add_plank(int(input_data[i]))
 
q = int(input_data[n + 1])
idx = n + 2
results = []
 
for _ in range(q):
    op = input_data[idx]
    length = int(input_data[idx+1])
    idx += 2
    
    if op == '+':
        add_plank(length)
    else:
        remove_plank(length)
        
    if quads >= 1 and (quads >= 2 or pairs >= 2):
        results.append("YES")
    else:
        results.append("NO")
 
print('
'.join(results))