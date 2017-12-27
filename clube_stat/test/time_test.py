from datetime import timedelta, datetime


# print(hour)

datetime.strptime("2009-11-12 23:18:53", "%Y-%m-%d %H:%M:%S")
x = datetime.strptime("14", "%H")
y = datetime.strptime("12", "%H")
# print(x - y == hour)


source = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
          0, 1, 2, 3, 4]


def f(lst, delta):
    delta = timedelta(hours=delta)
    lim = len(lst) - 1
    for i, t in enumerate(lst):
        if i < lim:
            x = datetime.strptime("{}".format(t), "%H")
            y = datetime.strptime("{}".format(lst[i + 1]), "%H")
            d = y - x
            if d == delta:
                print(True)
            else:
                print()




start_date = datetime.strptime("2017-12-27 9:00:00", "%Y-%m-%d %H:%M:%S")
end_date = datetime.strptime("2017-12-28 1:00:00", "%Y-%m-%d %H:%M:%S")

print(start_date)
print(end_date)
delta = end_date - start_date
print(delta)

def date_range(st, c):
    res = []
    ran = range(st, st+c+1)
    for t in ran:
        cd = t//24
        if t < 24:
            res.append(t)
        else:
            res.append(t-24*cd)
    return res

print(date_range(9, 124))







