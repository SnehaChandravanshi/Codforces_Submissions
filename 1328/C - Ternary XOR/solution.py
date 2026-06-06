t = int(input())
for _ in range(t):
    n = int(input())
    x = input().strip()
    
    a = []
    b = []
    diverged = False
    
    for char in x:
        if diverged:
            a.append('0')
            b.append(char)
        else:
            if char == '2':
                a.append('1')
                b.append('1')
            elif char == '1':
                a.append('1')
                b.append('0')
                diverged = True
            else:
                a.append('0')
                b.append('0')
                
    print("".join(a))
    print("".join(b))