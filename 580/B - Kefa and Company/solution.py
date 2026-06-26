import sys
 
input_data = sys.stdin.read().split()
if not input_data: exit()
 
n, d = int(input_data[0]), int(input_data[1])
friends = []
for i in range(n):
    friends.append((int(input_data[2+2*i]), int(input_data[3+2*i])))
 
friends.sort(key=lambda x: x[0])
 
max_f = 0
current_f = 0
left = 0
 
for right in range(n):
    current_f += friends[right][1]
    while friends[right][0] - friends[left][0] >= d:
        current_f -= friends[left][1]
        left += 1
    if current_f > max_f:
        max_f = current_f
 
sys.stdout.write(str(max_f) + '
')