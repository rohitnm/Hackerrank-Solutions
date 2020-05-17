m, n = list(map(int, input().split()))
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))
x = 0
br = []
for i in range(len(a)):
    ar = []
    for j in range(1, 101):
        x = a[i] * j
        ar.append(x)
        if x == b[0]:
            print(ar)
            for k in range(len(ar)):
                y = 0
                for f in range(len(b)):
                    if b[f] % ar[k] == 0:
                        y += 1
                        if y == len(b):
                            br.append(ar[k])
cr = sorted(list(set(br)))
print(cr)
last = []
for i in range(len(cr)):
    z = 0
    for j in range(len(a)):
        if cr[i] % a[j] == 0:
            z += 1
            if z == len(a):
                last.append(cr[i])
print(sorted(list(set(last))))
print(len(last))
