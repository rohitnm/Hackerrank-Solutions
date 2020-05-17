n = int(input())
a = list(map(int, input().split()))
m, d = list(map(int, input().split()))
y = 0
z = 0
for i in range(0, n-d+1):
    x = a[i]
    if len(a) == 1:
        if a[0] == m and d == 1:
            z += 1
            break
    for j in range(1, d):
        x = x + a[i+j]
    if x == m:
        z += 1
print(z)
