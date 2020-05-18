t = int(input())
ar = list(map(int, input().split()))
m = int(input())
brr = list(map(int, input().split()))
rank = []
rankk = []
arr = []
y = 0
for k in range(len(brr)):
    rank = []
    x = 1
    rank.append(x)
    arr = ar.copy()
    y = brr[k]
    arr.append(y)
    arr = sorted(arr, reverse=True)
    n = len(arr)
    for i in range(0, n):
        z = arr[i]
        if i == n-1:
            break
        if arr[i] == arr[i+1]:
            x = x
            rank.append(x)
            if arr[i] == y:
                y = -1
                rankk.append(x)
            elif arr[i + 1] == y:
                y = -1
                rankk.append(x)
        else:
            if arr[i] == y:
                y = -1
                rankk.append(x)
            x += 1
            rank.append(x)
            if arr[i+1] == y:
                y = -1
                rankk.append(x)
for j in range(len(rankk)):
    print(rankk[j])
