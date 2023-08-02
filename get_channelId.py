import requests
import re
import json
import bs4
from bs4 import BeautifulSoup

def get_channel_id(channel_url):
    
    # if the channel url contains "channel/UCXXXXX"
    # then UCXXXXX is the channel id
    match_id = re.search(r"channel/(UC[a-zA-Z0-9-_]+)", channel_url)
    if match_id:
        channel_id = match_id.group(1)
        return channel_id

    # otherwise we examine the html of the channel homepage
    response = requests.get(channel_url,allow_redirects=True)
    soup=BeautifulSoup(response.text, "html.parser")

    """
    The channel id is stored under ytInitialData - header - c4TabbedHeaderRenderer
    Simplying searching for "channelid" may not return the main channel id
    because the html also contains channelid(s) of other channels by the same uploader
    """
    data= re.search(r"var ytInitialData = ({.*});", str(soup.prettify())).group(1)

    json_data=json.loads(data)
    return json_data['header']['c4TabbedHeaderRenderer']['channelId']