import discord
from src.Database.TaskMsg import TaskMsg
from src.DiscordToDoist.Container import Container
from src.Database.Database import Database
from src.DiscordToDoist.DiscordClient import DiscordComponent


class ModifyTask(DiscordComponent):
    async def process(self, msg: discord.Message, content: str) -> None:
        # todo make dependency injection
        todoist = Container.apiClient

        db = Database().discord
        select = db.find_one({"discord_thread_id": msg.channel.id})
        entity: TaskMsg = TaskMsg.from_dict(select)

        if todoist.update_task(entity.todoist_task_id, content):
            thread = self.client.get_channel(entity.discord_thread_id)
            await thread.send(f"Zmodyfikowano zadanie na: {content}")

        else:
            await msg.channel.send("Coś poszło nie tak... Nie udało się zamknąć zadania")
