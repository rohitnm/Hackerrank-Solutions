n = int(input())
m = n-2
for i in range(1, n):
    print(" " * m, "#" * i)
    m -= 1
print("#" * n)