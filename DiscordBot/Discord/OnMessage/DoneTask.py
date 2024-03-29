import discord
from Common.LanguageProcessor.Processor import Result
from Common.ToDoist.ApiClient import ApiClient
from DiscordBot.Discord.Reactions import done_reaction
from DiscordBot.Database.Entities import TaskEntity
from DiscordBot.Discord.DiscordClient import OnMessageComponent


class DoneTask(OnMessageComponent):
    """ Set task as done
    """
    
    async def process(self, msg: discord.Message, content: str | None) -> None:
        entity: TaskEntity = self.db.find_one(
            TaskEntity, {"discord_thread_id": msg.channel.id})

        todoist: ApiClient = self.todoist.get_client(entity.discord_channel_id)

        if todoist.close_task(entity.todoist_task_id):
            await self.report(entity, "Zamknięto zadanie", done_reaction)
        else:
            communicate = "Coś poszło nie tak... Nie udało się zamknąć zadania"
            await self.report(entity, communicate)

    async def process_command(self, msg: discord.Message, command: Result):
        await self.process(msg, None)
