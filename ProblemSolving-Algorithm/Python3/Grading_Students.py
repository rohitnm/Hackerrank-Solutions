n = int(input())
grade = []
new_grade = []
q = 0
r = 0
m = 0
for i in range(0, n):
    x = int(input())
    grade.append(x)
for i in range(len(grade)):
    q = grade[i] // 5
    q = q + 1
    m = q * 5
    if grade[i] < 38:
        new_grade.append(grade[i])
    elif m - grade[i] < 3:
        new_grade.append(m)
    elif m - grade[i] >= 3:
        new_grade.append(grade[i])
for i in range(len(new_grade)):
    print(new_grade[i])
