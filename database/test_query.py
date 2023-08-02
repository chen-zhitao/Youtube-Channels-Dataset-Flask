import sqlite3
import os
cur_path = os.path.dirname(os.path.abspath(__file__))
data_directory = os.path.join(cur_path, "..", "data")
db_file = os.path.join(data_directory, "channels.db")
db_file_1 = os.path.join(data_directory, "channels_1.db")
db_file_2 = os.path.join(data_directory, "channels_2.db")

conn_1 = sqlite3.connect(db_file_1)
cursor_1 = conn_1.cursor()

conn_2 = sqlite3.connect(db_file_2)
cursor_2 = conn_2.cursor()

cursor_1.execute("SELECT * FROM channels LIMIT 1")
res1 = cursor_1.fetchall()
for row in res1:
    print(row)
    print()


cursor_2.execute("SELECT * FROM channels LIMIT 1")
res2 = cursor_2.fetchone()
for row in res2:
    print(row)
    print()