from src.DiscordToDoist.Components.AddingTask import AddingTask
from src.DiscordToDoist.Components.ApplicationStatus import ApplicationStatus
from src.DiscordToDoist.DiscordClient import DiscordClient
from src.config import discord_token


def main() -> None:
    client = DiscordClient()

    client.components["!test"] = ApplicationStatus(client)
    client.components["!add"] = AddingTask(client)

    client.run(discord_token)
