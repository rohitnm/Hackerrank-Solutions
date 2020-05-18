s, t = list(map(int, input().split()))
a, b = list(map(int, input().split()))
m, n = list(map(int, input().split()))
x = list(map(int, input().split()))
y = list(map(int, input().split()))
j = []
k = []
p = 0
q = 0
for i in range(0, m):
    z = x[i] + a
    j.append(z)
    if s <= j[i] <= t:
        p += 1
for i in range(0, n):
    z = y[i] + b
    k.append(z)
    if s <= k[i] <= t:
        q += 1
print(p)
print(q)
