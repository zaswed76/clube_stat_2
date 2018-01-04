import shutil
import os


data = "data.sql"
source_dir = os.path.abspath("./")
print(os.path.abspath("./"))



import sqlite3
conn = sqlite3.connect(data)
conn.execute("VACUUM")
conn.close()