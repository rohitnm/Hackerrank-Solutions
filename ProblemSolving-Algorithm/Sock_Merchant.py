n = int(input())
a = list(map(int, input().split()))
z = 0
y = []
for i in range(0, n):
    for k in range(len(y)):
        if i in y:
            i += 1
    if i > n-1:
        break
    x = a[i]
    y.append(i)
    for j in range(i+1, n):
        for k in range(len(y)):
            if j in y:
                j += 1
        if j > n-1:
            break
        if x == a[j]:
            y.append(j)
            z += 1
            break
print(z)
