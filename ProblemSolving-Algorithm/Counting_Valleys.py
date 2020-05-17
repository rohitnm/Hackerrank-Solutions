def counting(num, arr):
    x = 0
    count = 0
    for i in range(0, num):
        if arr[i] == 'U':
            x += 1
            if x == 0:
                count += 1
        elif arr[i] == 'D':
            x -= 1
    return count


n = int(input())
ar = input()
print(counting(n, ar))
