import discord
from Common.LanguageProcessor.Processor import Result
from DiscordBot.Discord.Reactions import deleted_message
from DiscordBot.Database.Entities import TaskEntity
from DiscordBot.Discord.DiscordClient import OnMessageComponent


class DeletingTask(OnMessageComponent):
    """ Deleting new task
    """

    async def process_command(self, msg: discord.Message, command: Result):
        await self.process(msg, command.dict["content"])

    async def process(self, msg: discord.Message, content: str) -> None:

        entity: TaskEntity = self.db.find_one(
            TaskEntity, {"discord_thread_id": msg.channel.id})

        if entity is None:
            await msg.reply("Usunięto to zadanie wcześniej")
            return

        result = self.db.delete_one(
            TaskEntity, {"todoist_task_id": entity.todoist_task_id})

        if result.deleted_count <= 0:
            await msg.reply("Usuwanie zadania nie powiodło się")
            return

        channel = self.todoist.get_client(entity.discord_channel_id)
        channel.delete_task(entity.todoist_task_id)

        await self.report(entity,
                          communicate="Usunięto zadanie",
                          reaction=deleted_message)
