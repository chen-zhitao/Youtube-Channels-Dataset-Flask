import sqlite3

def get_channel_data(channelId):
    conn = sqlite3.connect("data/channels.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM channels WHERE id = ?;", (channelId,))
    res = cursor.fetchall()
    conn.close()
    if not res:
        print('meh')
    print(len(res))
    return res[0] if res else None

# print(len(get_channel_data('UCX6OQ3DkcsbYNE6H8uQQuVA')))