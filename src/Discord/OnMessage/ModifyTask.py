import discord
from src.LanguageProcessor.Processor import Result
from src.ToDoist.ApiClient import ApiClient
from src.Database.Entities import TaskEntity
from src.Discord.DiscordClient import OnMessageComponent


class ModifyTask(OnMessageComponent):

    async def process(self, msg: discord.Message, content: str) -> None:
        entity: TaskEntity = self.db.find_one(
            TaskEntity, {"discord_thread_id": msg.channel.id})

        todoist: ApiClient = self.todoist.get_client(msg.channel.id)

        if todoist.update_task(entity.todoist_task_id, content):
            await self.report(entity, f"Zmodyfikowano zadanie na: {content}")
        else:
            communicate = "Coś poszło nie tak... Nie udało się zamknąć zadania"
            await self.report(entity, communicate)

    async def process_command(self, msg: discord.Message, command: Result):
        await self.process(msg, command.dict["content"])
