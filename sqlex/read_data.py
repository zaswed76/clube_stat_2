

import pandas as pd
import sqlite3
import sqlalchemy

conn = sqlite3.connect("data.sql")
df = pd.read_sql_query("select * from LES_STAT;", conn)
# print(df["data_time"])
# # print(df[df["data_time"] == "2018-02-09"])
df['data_time'] = df['data_time'].astype('datetime64[ns]')
# conn2 = sqlite3.connect("data_pd.sql")
# df = pd.read_sql_query("select * from LES_STAT;", conn)
print(df["data_time"])
# df.to_sql("LES_STAT", conn2, dtype={'data_time': sqlalchemy.DateTime()})