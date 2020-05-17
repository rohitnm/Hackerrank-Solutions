def electronics(budget, kb, usb, p1, p2):
    ar = []
    for i in range(0, kb):
        x = p1[i]
        for j in range(0, usb):
            z = x + p2[j]
            if z <= budget:
                ar.append(z)
    if not ar:
        return -1
    else:
        return max(ar)


b, n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))
brr = list(map(int, input().split()))
print(electronics(b, n, m, arr, brr))
