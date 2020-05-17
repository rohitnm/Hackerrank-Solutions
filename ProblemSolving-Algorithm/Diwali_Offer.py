t = int(input())
l = []
m = 0
ar = []
for k in range(0, t):
    l1 = list(map(int, input().split()))
    l.append(l1)
for j in range(len(l)):
    ar = []
    z = l[j]
    n, c, m = z
    x = n // c
    ar.append(x)
    for i in range(0, x):
        y = x // m
        ar.append(y)
        x = x - y*m + y
        if x >= m:
            continue
        else:
            break
    print(sum(ar))
