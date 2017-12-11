# import csv, os
# from clubestat import pth
#
# csv_file = os.path.join(pth.DATA_DIR, "data3.csv")
#
#
# from pandas import read_csv
#
# df2 = read_csv(csv_file,";", encoding = "1251")
# num = ["1", "2", "3", "4"]
#
# df2.insert(1, "num", num)
# # df[(df.foo == 222) | (df.bar == 444)]
#
# print(df2[(df2.pro == True) & (df2.class_ == "comp bg_resid")])

class Line:
    def __init__(self, line):
        self.line = line

class Table:
    def __init__(self, lines):
        self.lines = lines


class Map:
    def __init__(self, table):
        self.table = table


class Stat:
    def __init__(self, taken, free):
        self.free = free
        self.taken = taken

class Entry:
    def __init__(self, date, time, club, stat, map):
        self.map = map
        self.stat = stat
        self.club = club
        self.time = time
        self.date = date



data = []
lines = [Line(*line) for line in data]
map = Map(Table(lines))
stat = Stat(25, 12)
entry = Entry("28.03.2017", "23:50", "les", stat, map)

print(entry.stat.taken == 25)

