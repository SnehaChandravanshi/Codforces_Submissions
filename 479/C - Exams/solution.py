n = int(input())
exams = []
for _ in range(n):
    a, b = map(int, input().split())
    exams.append((a, b))
 
exams.sort()
 
current_day = -1
for official_day, early_day in exams:
    if early_day >= current_day:
        current_day = early_day
    else:
        current_day = official_day
 
print(current_day)