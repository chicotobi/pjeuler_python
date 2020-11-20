mnths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
ds = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']


def is_leapyear(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


def days_in_year(year):
    d = 365
    if is_leapyear(year):
        d += 1
    return d


def find_weekday(day, month, year):
    d = 0
    for y in range(1900,year):
        d += days_in_year(y)
    for m in range(1,month):
        d += mnths[m-1]
    if is_leapyear(year) and month > 2:
        d += 1
    d += day
    return ds[(d-1) % 7]


s = 0
for y in range(1901,2001):
    for m in range(1,13):
        wkd = find_weekday(1,m,y)
        if wkd == 'Su':
            s += 1
print(s)