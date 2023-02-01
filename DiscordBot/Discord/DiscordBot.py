from DiscordBot.Discord.OnMessage.Help import Help
from DiscordBot.Discord.OnMessage.ModifyTask import ModifyTask
from DiscordBot.Discord.OnMessage.DoneTask import DoneTask
from DiscordBot.Discord.OnMessage.AddingTask import AddingTask
from DiscordBot.Discord.OnMessage.DeletingTask import DeletingTask
from DiscordBot.Discord.OnMessage.ApplicationStatus import ApplicationStatus
from DiscordBot.Discord.OnMessage.RegisterTodoistToken import RegisterToDoistToken
from DiscordBot.Discord.OnMessage.SelectToDoistProject import SelectToDoistProject
from DiscordBot.Discord.OnMessage.AddComment import AddComment
from DiscordBot.Discord.OnMessage.RemoveToDoistConnection import \
    RemoveToDoistConnection
from DiscordBot.Discord.OnMessage.LanguageProcessMessage import LanguageProcessMessage
from DiscordBot.Discord.OnNotification.OnComplete import OnComplete
from DiscordBot.Discord.OnNotification.OnAdded import OnAdded
from DiscordBot.Discord.OnNotification.OnDeleted import OnDeleted
from DiscordBot.Discord.DiscordClient import DiscordClient
from DiscordBot.config import discord_token


def main() -> None:
    client = DiscordClient()

    client.on_messages["!token"] = RegisterToDoistToken(client)
    client.on_messages["!project"] = SelectToDoistProject(client)
    client.on_messages["!rmtoken"] = RemoveToDoistConnection(client)

    client.on_messages["!test"] = ApplicationStatus(client)
    client.on_messages["!add"] = AddingTask(client)
    client.on_messages["!dodaj"] = AddingTask(client)
    client.on_messages["!delete"] = DeletingTask(client)
    client.on_messages["!usun"] = DeletingTask(client)
    client.on_messages["!done"] = DoneTask(client)
    client.on_messages["!gotowe"] = DoneTask(client)
    client.on_messages["!update"] = ModifyTask(client)
    client.on_messages["!help"] = Help(client)

    client.on_messages["!add_comment"] = AddComment(client)

    client.on_messages["!!"] = LanguageProcessMessage(client)

    client.on_notification["item:completed"] = OnComplete(client)
    client.on_notification["item:added"] = OnAdded(client)
    client.on_notification["item:deleted"] = OnDeleted(client)

    client.run(discord_token)
