from src.Discord.OnMessage.ModifyTask import ModifyTask
from src.Discord.OnMessage.DoneTask import DoneTask
from src.Discord.OnMessage.AddingTask import AddingTask
from src.Discord.OnMessage.ApplicationStatus import ApplicationStatus
from src.Discord.OnMessage.RegisterTodoistToken import RegisterToDoistToken
from src.Discord.OnMessage.SelectToDoistProject import SelectToDoistProject
from src.Discord.OnMessage.AddComment import AddComment
from src.Discord.OnMessage.RemoveToDoistConnection import \
    RemoveToDoistConnection
from src.Discord.OnMessage.LanguageProcessMessage import LanguageProcessMessage
from src.Discord.OnNotification.OnComplete import OnComplete
from src.Discord.OnNotification.OnAdded import OnAdded
from src.Discord.DiscordClient import DiscordClient
from src.config import discord_token


def main() -> None:
    client = DiscordClient()

    client.on_messages["!token"] = RegisterToDoistToken(client)
    client.on_messages["!project"] = SelectToDoistProject(client)
    client.on_messages["!rmtoken"] = RemoveToDoistConnection(client)

    client.on_messages["!test"] = ApplicationStatus(client)
    client.on_messages["!add"] = AddingTask(client)
    client.on_messages["!dodaj"] = AddingTask(client)
    client.on_messages["!done"] = DoneTask(client)
    client.on_messages["!gotowe"] = DoneTask(client)
    client.on_messages["!update"] = ModifyTask(client)

    client.on_messages["!add_comment"] = AddComment(client)

    client.on_messages["!!"] = LanguageProcessMessage(client)

    client.on_notification["item:completed"] = OnComplete(client)
    client.on_notification["item:added"] = OnAdded(client)

    client.run(discord_token)
