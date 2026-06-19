s = input().strip()
n = len(s)
 
for i in range(n):
    if int(s[i]) % 8 == 0:
        print(f"YES
{s[i]}")
        exit()
        
for i in range(n):
    for j in range(i + 1, n):
        val = int(s[i] + s[j])
        if val % 8 == 0:
            print(f"YES
{val}")
            exit()
            
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            val = int(s[i] + s[j] + s[k])
            if val % 8 == 0:
                print(f"YES
{val}")
                exit()
 
print("NO")