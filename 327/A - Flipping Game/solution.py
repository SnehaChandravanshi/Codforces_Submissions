length = int(input())
numbers = list(map(int, input().split()))
 
total_ones = numbers.count(1)
max_gain = -1
current_gain = 0
 
for num in numbers:
    if num == 0:
        current_gain += 1
    else:
        current_gain -= 1
        
    if current_gain > max_gain:
        max_gain = current_gain
        
    if current_gain < 0:
        current_gain = 0
 
print(total_ones + max_gain)