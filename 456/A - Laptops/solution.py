import sys
 
input_data = sys.stdin.read().split()
if not input_data:
    exit()
 
n = int(input_data[0])
for i in range(n):
    if int(input_data[2 * i + 1]) != int(input_data[2 * i + 2]):
        print("Happy Alex")
        exit()
        
print("Poor Alex")