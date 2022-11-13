import json
import os


def config(id: str) -> str:
    f = open("~config.json")
    data = json.load(f)
    return data[id] if id in data else ''


client_id = config("client_id")
client_secret = config("client_secret")
scope = config("scope")
discord_token = config("discord_token")
connection_string = os.getenv("CONNECTION_STRING")
logging_file = config("logging_file")
thread_archive_time = (60 * 1)
