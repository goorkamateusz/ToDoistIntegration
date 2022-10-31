import discord
from src.Discord.Reactions import done_reaction
from src.Database.Entities import TaskEntity
from src.Discord.DiscordClient import OnMessageComponent


class DoneTask(OnMessageComponent):

    async def process(self, msg: discord.Message, content: str) -> None:
        entity: TaskEntity = self.db.find_one(
            TaskEntity, {"discord_thread_id": msg.channel.id})

        if self.todoist.close_task(entity.todoist_task_id):
            await self.report(entity, "Zamknięto zadanie", done_reaction)
        else:
            communicate = "Coś poszło nie tak... Nie udało się zamknąć zadania"
            await self.report(entity, communicate)
