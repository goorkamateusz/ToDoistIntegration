import discord
from src.Database.TaskEntity import TaskEntity
from src.Discord.DiscordClient import OnMessageComponent


class ModifyTask(OnMessageComponent):

    async def process(self, msg: discord.Message, content: str) -> None:
        select = self.db_tasks.find_one({"discord_thread_id": msg.channel.id})
        entity: TaskEntity = TaskEntity.from_dict(select)

        if self.todoist.update_task(entity.todoist_task_id, content):
            await self.report(entity, f"Zmodyfikowano zadanie na: {content}")
        else:
            communicate = "Coś poszło nie tak... Nie udało się zamknąć zadania"
            await self.report(entity, communicate)
