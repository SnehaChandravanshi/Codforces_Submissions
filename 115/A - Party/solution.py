n = int(input())
managers = [int(input()) for _ in range(n)]
 
max_depth = 0
 
for i in range(n):
    current_depth = 0
    current_employee = i + 1
    
    while current_employee != -1:
        current_employee = managers[current_employee - 1]
        current_depth += 1
        
    if current_depth > max_depth:
        max_depth = current_depth
 
print(max_depth)