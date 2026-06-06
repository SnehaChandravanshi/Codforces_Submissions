s = input().strip()
 
if (s.find('AB') != -1 and s.find('BA', s.find('AB') + 2) != -1) or \
   (s.find('BA') != -1 and s.find('AB', s.find('BA') + 2) != -1):
    print("YES")
else:
    print("NO")