n = int(input())
a = sorted(list(map(int, input().split())))
b = []
for i in range(1, 6):
    x = a.count(i)
    b.append(x)
index = b.index(max(b))
print(index + 1)
