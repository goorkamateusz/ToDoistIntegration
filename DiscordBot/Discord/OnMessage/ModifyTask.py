import discord
from Common.LanguageProcessor.Processor import Result
from Common.ToDoist.ApiClient import ApiClient
from DiscordBot.Database.Entities import TaskEntity
from DiscordBot.Discord.DiscordClient import OnMessageComponent


class ModifyTask(OnMessageComponent):
    """ Modify task content
    """

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
