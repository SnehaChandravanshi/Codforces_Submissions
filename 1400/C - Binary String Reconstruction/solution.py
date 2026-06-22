import sys
 
t = int(sys.stdin.readline())
for _ in range(t):
    s = sys.stdin.readline().strip()
    x = int(sys.stdin.readline())
    n = len(s)
    
    w = ['1'] * n
    
    for i in range(n):
        if s[i] == '0':
            if i - x >= 0:
                w[i - x] = '0'
            if i + x < n:
                w[i + x] = '0'
                
    valid = True
    for i in range(n):
        if s[i] == '1':
            ok = False
            if i - x >= 0 and w[i - x] == '1':
                ok = True
            if i + x < n and w[i + x] == '1':
                ok = True
            if not ok:
                valid = False
                break
                
    if valid:
        print("".join(w))
    else:
        print("-1")