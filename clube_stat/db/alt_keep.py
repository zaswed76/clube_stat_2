import sqlite3
import os

import yaml

from clube_stat.db import tables, sql_keeper
from clube_stat import pth

tables_cfg = tables.get_data(
    os.path.join(pth.DATA_DIR, "tables.yaml"))
db = os.path.join(pth.DATA_DIR, "test2.sql")
kp = sql_keeper.Keeper(db)
tb = tables.Tables()
print(tables_cfg["tables"]["stat"])
t = tb.add_table(tables_cfg["tables"]["stat"], "stat_table",
                 "CREATE TABLE IF NOT EXISTS")
print(t)
kp.open_connect()
kp.open_cursor()
kp.create_table(t)
