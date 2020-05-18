n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
z = 0
for i in range(0, n-1):
    for j in range(i+1, n):
        x = a[i] + a[j]
        if x % k == 0:
            z += 1
print(z)
