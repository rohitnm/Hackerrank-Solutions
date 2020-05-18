def leap_year(x):
    if x % 100 == 0:
        if x % 400 == 0:
            return True
        else:
            return False
    elif x % 4 == 0:
        return True
    else:
        return False


year = int(input())
not_leap = 243
leap = 244
if year < 1918:
    if year % 4 == 0:
        yr = leap
    else:
        yr = not_leap
elif year == 1918:
    yr = 230
else:
    if leap_year(year):
        yr = leap
    else:
        yr = not_leap

day = 256 - yr
print(str(day) + '.09.' + str(year))
