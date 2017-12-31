
import os
import sqlite3 as sql
from clube_stat.db import tables
from clube_stat.db import sql_keeper
from clube_stat import pth


tbls = tables.Tables()
tbls.add_table({"club":"text", "visitor":"text", "load":"text"}, "stat")
print(tbls["stat"].queries)

kp = sql_keeper.Keeper(os.path.join(pth.DATA_DIR, "pd_sql.sql"))
kp.open_connect()
kp.open_cursor()
print(kp.cursor.description)
# kp.create_table(tbls["stat"].queries)
# kp.close()

