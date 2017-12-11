import csv, os
from clubestat import pth

csv_file = os.path.join(pth.DATA_DIR, "data3.csv")


from pandas import read_csv

df2 = read_csv(csv_file,";", encoding = "1251")
num = ["1", "2", "3", "4"]

df2.insert(1, "num", num)
# df[(df.foo == 222) | (df.bar == 444)]

print(df2[(df2.pro == True) & (df2.class_ == "comp bg_resid")])