from src.DiscordToDoist.Components.DoneTask import DoneTask
from src.DiscordToDoist.Components.AddingTask import AddingTask
from src.DiscordToDoist.Components.ApplicationStatus import ApplicationStatus
from src.DiscordToDoist.DiscordClient import DiscordClient
from src.config import discord_token


def main() -> None:
    client = DiscordClient()

    client.components["!test"] = ApplicationStatus(client)
    client.components["!add"] = AddingTask(client)
    client.components["!done"] = DoneTask(client)

    client.run(discord_token)
