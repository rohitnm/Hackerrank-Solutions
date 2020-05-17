x = list(map(int, input().split()))
sum1 = 0
sum2 = 0
y = x.copy()
x.remove(max(x))
y.remove(min(y))
for i in range(0, 4):
    sum1 = sum1 + x[i]
    sum2 = sum2 + y[i]
print(sum1, sum2)