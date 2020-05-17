def digit_add(x):
    ar = list(map(int, str(x)))
    n = len(ar)
    br = []
    f = 0
    for j in range(0, n):
        if ar[j] % 2 == 0:
            br.append(0)
        else:
            br.append(ar[j])
            break
    if sum(br) == 0:
        return sum(br)
    else:
        br = []
        for i in range(0, n):
            if ar[i] % 2 != 0:
                z = ar[i] + 1
                f = ar.index(ar[i])
                br.append(z)
                break
            else:
                br.append(ar[i])
        if n > 1:
            for i in range(f+1, n):
                z = ar[i] - ar[i]
                br.append(z)
        m = convert(br)
        return m - x


def convert(l1):
    s = [str(i) for i in l1]
    res = int("".join(s))
    return res


def digit_sub(y):
    ar = list(map(int, str(y)))
    n = len(ar)
    br = []
    f = 0
    for i in range(0, n):
        if ar[i] % 2 != 0:
            z = ar[0] - 1
            f = ar.index(ar[i])
            br.append(z)
            break
        else:
            br.append(ar[i])
    if n > 1:
        for i in range(f+1, n-1):
            z = ar[i] + 1
            br.append(z)
    z = ar[-1] + 2
    br.append(z)
    o = convert(br)
    return o


num = int(input())
if digit_add(num) < digit_sub(num):
    print(digit_add(num))
else:
    print(digit_sub(num))