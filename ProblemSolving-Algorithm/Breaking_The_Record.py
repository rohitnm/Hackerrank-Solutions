n = int(input())
a = list(map(int, input().split()))
x = a[0]
y = 0
p = a[0]
q = 0
for i in range(1, n):
    if x < a[i]:
        x = a[i]
        y += 1
    if p > a[i]:
        p = a[i]
        q += 1
print(y, q)
