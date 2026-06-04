m, s = map(int, input().split())
 
if s == 0:
    print("0 0" if m == 1 else "-1 -1")
elif s > 9 * m:
    print("-1 -1")
else:
    min_str = ""
    sum_left = s - 1
    for i in range(m - 1):
        digit = min(9, sum_left)
        min_str = str(digit) + min_str
        sum_left -= digit
    min_str = str(sum_left + 1) + min_str
    
    max_str = ""
    sum_left = s
    for i in range(m):
        digit = min(9, sum_left)
        max_str += str(digit)
        sum_left -= digit
        
    print(min_str, max_str)