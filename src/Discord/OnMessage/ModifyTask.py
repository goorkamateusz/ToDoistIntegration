import discord
from src.Database.TaskMsg import TaskMsg
from src.Discord.Container import Container
from src.Database.Database import Database
from src.Discord.DiscordClient import OnMessageComponent


class ModifyTask(OnMessageComponent):

    async def process(self, msg: discord.Message, content: str) -> None:
        select = self.db.find_one({"discord_thread_id": msg.channel.id})
        entity: TaskMsg = TaskMsg.from_dict(select)

        if self.todoist.update_task(entity.todoist_task_id, content):
            thread = self.client.get_channel(entity.discord_thread_id)
            await thread.send(f"Zmodyfikowano zadanie na: {content}")
        else:
            await msg.channel.send("Coś poszło nie tak... Nie udało się zamknąć zadania")
