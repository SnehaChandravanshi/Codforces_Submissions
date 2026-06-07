x = list(input().strip())
 
for i in range(len(x)):
    digit = int(x[i])
    if digit >= 5:
        if i == 0 and digit == 9:
            continue
        x[i] = str(9 - digit)
 
print("".join(x))