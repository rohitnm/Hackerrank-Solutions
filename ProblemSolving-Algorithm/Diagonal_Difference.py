n = int(input())
ar = []
ss = 0
s1 = 0
s2 = 0
for i in range(0, n):
    x = (input().split())
    ar.append(x)
    a = ar[i]
    b = int(a[i])
    ss = ss + b
    c = int(a[n-1-i])
    s1 = s1 + c
s2 = ss - s1
print(abs(s2))