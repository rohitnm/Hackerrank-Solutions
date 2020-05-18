n = int(input())
p = int(input())
x = 0
ar = []
for i in range(1, n + 1):
    ar.append(i)
if p in ar:
    x = ar.index(p) / 2
    if x % 2 == 0:
        x = round(x)
    else:
        if round(x) < x:
            x = round(x)
            x = x + 1
        else:
            x = round(x)
page = abs((n // 2) - x)
if page < x:
    print(page)
else:
    print(x)
