from flask import Flask, request, jsonify, render_template
from get_channelId import get_channel_id
import sqlite3
import requests
import re
import json
import bs4
from bs4 import BeautifulSoup


app = Flask(__name__)

conn=sqlite3.connect("data/channels.db", check_same_thread=False)
cursor = conn.cursor()


@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        query_type = request.form.get('query_type')
        query_value = request.form.get('query_value')
        if query_type == "url":
            channelId = get_channel_id(query_value)
        else:
            channelId = query_value
        cursor.execute("SELECT * FROM channels WHERE id = ?;", (channelId,))
        res = cursor.fetchall()
        # res would be a tuple with length 3 if it is not None
        if res:
            return jsonify({"channelId": res[0][0], "channel_url": res[0][1], "channel_description": res[0][2]})
        else:
            return jsonify({"error": "Channel not in database."}), 404

    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)