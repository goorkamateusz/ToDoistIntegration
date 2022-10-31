import discord
from src.Database.Entities import TaskEntity
from src.Discord.DiscordClient import OnMessageComponent


class ModifyTask(OnMessageComponent):

    async def process(self, msg: discord.Message, content: str) -> None:
        entity: TaskEntity = self.db.find_one(
            TaskEntity, {"discord_thread_id": msg.channel.id})

        if self.todoist.update_task(entity.todoist_task_id, content):
            await self.report(entity, f"Zmodyfikowano zadanie na: {content}")
        else:
            communicate = "Coś poszło nie tak... Nie udało się zamknąć zadania"
            await self.report(entity, communicate)
