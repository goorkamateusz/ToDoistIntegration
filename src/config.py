import json


def config(id: str) -> str:
    f = open("~config.json")
    data = json.load(f)
    return data[id]


client_id = config("client_id")
client_secret = config("client_secret")
scope = config("scope")
discord_token = config("discord_token")
todoist_token = config("todoist_token")
