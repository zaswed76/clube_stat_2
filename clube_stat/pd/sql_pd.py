
import os
import sqlite3 as sql
from clube_stat.db import tables
from clube_stat.db import sql_keeper
from clube_stat import pth
import pandas as pd
import arrow
import matplotlib.pyplot as plt


tbls = tables.Tables()
tbls.add_table({"club":"text", "visitor":"INTEGER", "dt":"TIMESTAMP"}, "stat")
kp = sql_keeper.Keeper(r"D:\0SYNC\python_projects\clube_stat_2\clube_stat\data\data.sql")
kp.open_connect()
kp.open_cursor()

# kp.create_table(tbls["stat"].queries)
#
#
#
# data = (["les", 12, '2017-12-30 09:30:12'],
#         ["les", 14, '2017-12-30 09:35:12'],
#         ["les", 15, '2017-12-30 09:40:12'],
#         ["les", 17, '2017-12-30 09:45:12'],
#         ["les", 22, '2017-12-30 09:50:12'])
#
# kp.cursor.executemany("insert into stat values (?,?,?)", data)
# kp.commit()
# kp.close()

def f(lst):
    res = []
    for i in lst:
        res.append(arrow.get(i).time().strftime("%H:%M"))
    return res

df = pd.read_sql_query("SELECT data_time FROM club", kp.connect)
# print(df)
# print("----------------------")
res =  df[(df["data_time"] > '2017-12-27 12:50:00')&(df["data_time"] <='2017-12-27 13:20:59')]
print(res)


# times = f(res["dt"])
#
# res.insert(3, "times", times)
# # print(res[["visitor","times"]])
# df = res[["visitor","times"]]
#
# # .plot(kind="bar", x=res.times)
# res2 = pd.DataFrame({"load": [5, 6, 12], "times": [0, 1, 2]})
# # res2[["load","times"]].plot(kind="bar", x=res.times)
#
# fig, ax = plt.subplots()
# ax.plot(res2)
# plt.show()







