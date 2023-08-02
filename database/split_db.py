import sqlite3
import os

cur_path = os.path.dirname(os.path.abspath(__file__))
data_directory = os.path.join(cur_path, "..", "data")
db_file = os.path.join(data_directory, "channels.db")
db_file_1 = os.path.join(data_directory, "channels_1.db")
db_file_2 = os.path.join(data_directory, "channels_2.db")

def split_database():

    conn_og = sqlite3.connect(db_file)
    cursor_og = conn_og.cursor()

    conn_1 = sqlite3.connect(db_file_1)
    cursor_1 = conn_1.cursor()

    conn_2 = sqlite3.connect(db_file_2)
    cursor_2 = conn_2.cursor()

    cursor_og.execute("ATTACH DATABASE ? AS channels_1", (db_file_1,))
    cursor_og.execute("ATTACH DATABASE ? AS channels_2", (db_file_2,))
    conn_og.commit()

    cursor_og.execute("SELECT COUNT(*) FROM main.channels")
    rows = cursor_og.fetchone()[0]
    #print(rows)
    mid = rows // 2

    # Export the first half
    query_1 = f"INSERT INTO channels_1.channels SELECT * FROM main.channels LIMIT {mid}"
    cursor_og.execute(query_1)
    conn_og.commit()

    # Export the second half
    query_2 = f"INSERT INTO channels_2.channels SELECT * FROM main.channels LIMIT -1 OFFSET {mid}"
    cursor_og.execute(query_2)
    conn_og.commit()

    cursor_og.close()
    conn_og.close()

    cursor_1.close()
    conn_1.close()

    cursor_2.close()
    conn_2.close()
    return


if __name__ == "__main__":
    split_database()