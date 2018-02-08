import sqlite3 as sql
from datetime import datetime, timedelta

import yaml

tables_file = "tables.yaml"
sql_data = "data.sql"


def get_data(path):
    with open(path, "r") as obj:
        return yaml.load(obj)


def create_table(cursor, table):
    try:
        cursor.executescript(table)
    except sql.OperationalError as er:
        print(er)
    else:
        cursor.close()

def test_data():
    res = []
    d = datetime.now()
    for i in range(500000):
        date = d + timedelta(days=1)
        res.append((date, 5))
    return res



conn = sql.connect(sql_data)
curs = conn.cursor()
#
# tables = get_data("tables.yaml")
# create_table(curs, tables["Les"])



curs.executemany("""INSERT INTO LES_STAT VALUES (? ,?)""", test_data())
conn.commit()
curs.close()


