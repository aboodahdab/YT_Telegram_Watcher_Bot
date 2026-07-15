import requests
import os
from dotenv import load_dotenv
from telegramBot import sending_message
import asyncio
load_dotenv()
channel_IDs = ["UCPokJ1HtDczTd0rRPMwMeWw", "UCQB9yZWLvcSNI9ruw74iF8Q","UCd4LWpxIFRnoXJB63WEc-vw",
               "UC8F8MJyWevV2EzzLxZnSRLg", "UC5p0FTpOleZUc87YVJ8VX-g", "UCGW5zIEencf7p6IncKLFtuA", "UCFq4pOuTiZmfJyCxaYTT3Hg", "UCdYt25YVNOQET06LMlr54aA", "UCEHvaZ336u7TIsUQ2c6SAeQ"]
API_KEY = os.getenv("API_KEY")
FILENAME = "storingFile.txt"

joined_data = ",".join(channel_IDs)


def read_file():
    with open(FILENAME, "r") as f:
        arr = f.readlines()
        if not arr:
            return []
        return arr


def write_to_file(text):
    file_data = read_file()
    with open(FILENAME, "a") as f:
        if not file_data:
            f.write(f"{text}")
        else:
            f.write(f"\n{text}")


def add_the_id_to_the_link(id):
    link = f"https://www.youtube.com/watch?v={id}"
    return link


def open_uploads_playlist(uploads, max_results):
    api_endpoint = f"https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails&playlistId={uploads}&maxResults={max_results}&key={API_KEY}"
    print(api_endpoint)
    data = requests.get(api_endpoint)
    jsoned_data = data.json()
    items = jsoned_data["items"][0]
    contentDetails = items["contentDetails"]
    videoId = contentDetails["videoId"]
    print(contentDetails)

    data = read_file()
    if f"{videoId}\n" in data or videoId in data:

        return
    print("we're going to send the video for you!")
    link = add_the_id_to_the_link(videoId)
    asyncio.run(sending_message(f"New video:\n{link}"))
    write_to_file(videoId)


def get_uploads_playlist():
    #  I think there is a way to skip channels API call enterily by converting the "UC" in the start of the id to "UU" and giving it to playlist items that will work too.
    api_endpoint = f"https://www.googleapis.com/youtube/v3/channels?part=snippet,contentDetails&id={joined_data}&key={API_KEY}"
    data = requests.get(api_endpoint)
    jsoned_data = data.json()
    items = jsoned_data["items"]
    for item in items:

        contentDetails = item["contentDetails"]
        uploads = contentDetails["relatedPlaylists"]["uploads"]
        print(uploads)
        open_uploads_playlist(uploads, 1)


# we need to use channels api to get uploads playlist and then get it's item using the playlistItems  api .
get_uploads_playlist()
