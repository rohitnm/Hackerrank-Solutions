n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
charged = int(input())
a.pop(k)
y = sum(a) // 2
if y == charged:
    print('Bon Appetit')
else:
    print(charged - y)
