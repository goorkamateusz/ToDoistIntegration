import json


def config(id: str) -> str:
    f = open("~config.json")
    data = json.load(f)
    return data[id] if id in data else ''


client_id = config("client_id")
client_secret = config("client_secret")
scope = config("scope")
discord_token = config("discord_token")
todoist_token = config("todoist_token")
connection_string = config("connection_string")
logging_file = config("logging_file")
temp_channel_id = config("temp_channel_id")
thread_archive_time = (60 * 1)
