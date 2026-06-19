import sys
 
input_data = sys.stdin.read().split()
if not input_data:
    exit()
 
n = int(input_data[0])
k = int(input_data[1])
 
both = []
alice = []
bob = []
 
idx = 2
for _ in range(n):
    t = int(input_data[idx])
    a = int(input_data[idx+1])
    b = int(input_data[idx+2])
    idx += 3
    
    if a == 1 and b == 1:
        both.append(t)
    elif a == 1:
        alice.append(t)
    elif b == 1:
        bob.append(t)
 
both.sort()
alice.sort()
bob.sort()
 
for i in range(min(len(alice), len(bob))):
    both.append(alice[i] + bob[i])
 
both.sort()
 
if len(both) < k:
    print(-1)
else:
    print(sum(both[:k]))