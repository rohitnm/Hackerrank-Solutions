x = input().split(':')
y = x[2]
num = ""
alp = ""
hr = 0
for i in range(len(y)):
    if y[i].isdigit():
        num = num + y[i]
    elif 'A' <= y[i] <= 'Z':
        alp = alp + y[i]
if alp == 'PM':
    hr = 12 + int(x[0])
    if x[0] == '12':
        hr = 12
elif alp == 'AM':
    hr = int(x[0])
    if x[0] == '12':
        hr = '00'
print(str(hr) + ':' + x[1] + ':' + num)
