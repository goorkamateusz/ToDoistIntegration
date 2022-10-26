from src.DiscordToDoist.OnMessage.ModifyTask import ModifyTask
from src.DiscordToDoist.OnMessage.DoneTask import DoneTask
from src.DiscordToDoist.OnMessage.AddingTask import AddingTask
from src.DiscordToDoist.OnMessage.ApplicationStatus import ApplicationStatus
from src.DiscordToDoist.OnNotification.OnComplete import OnComplete
from src.DiscordToDoist.DiscordClient import DiscordClient
from src.config import discord_token


def main() -> None:
    client = DiscordClient()

    client.on_messages["!test"] = ApplicationStatus(client)
    client.on_messages["!add"] = AddingTask(client)
    client.on_messages["!done"] = DoneTask(client)
    client.on_messages["!update"] = ModifyTask(client)

    client.on_notification["item:completed"] = OnComplete(client)

    client.run(discord_token)
