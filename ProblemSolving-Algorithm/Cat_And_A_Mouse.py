def position(num):
    arr = []
    value = []
    for i in range(0, num):
        z = list(map(int, input().split()))
        arr.append(z)
    for j in range(len(arr)):
        a, b, c = arr[j]
        val = calc(a, b, c)
        value.append(val)
    return '\n'.join([str(k) for k in value])


def calc(x, y, z):
    p1 = abs(z - x)
    p2 = abs(z - y)
    if p1 > p2:
        return 'Cat B'
    elif p2 > p1:
        return 'Cat A'
    elif p1 == p2:
        return 'Mouse C'


n = int(input())
print(position(n))
