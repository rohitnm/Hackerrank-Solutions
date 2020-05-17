n = int(input())
arr = list(map(int, input().split()))
p = 0
q = 0
z = 0
for i in range(0, n):
    if arr[i] < 0:
        p = p + 1
    elif arr[i] > 0:
        q = q + 1
    else:
        z = z + 1
p = p / n
q = q / n
z = z / n
print(p)
print(q)
print(z)
