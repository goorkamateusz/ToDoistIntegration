import discord
from Common.LanguageProcessor.Processor import Result
from DiscordBot.Discord.Reactions import managed_msg_reaction
from DiscordBot.Database.Entities import TaskEntity
from DiscordBot.Discord.DiscordClient import OnMessageComponent
from Common.ToDoist.ApiClient import ApiClient
from DiscordBot.config import thread_archive_time


class AddingTask(OnMessageComponent):
    """ Create new task
    """

    async def process_command(self, msg: discord.Message, command: Result):
        await self.process(msg, command.dict["content"])

    async def process(self, msg: discord.Message, content: str) -> None:
        todoist: ApiClient = self.todoist.get_client(msg.channel.id)

        if todoist is None or not todoist.is_project_selected:
            await msg.reply("Kanał jest nie połączony")
            return

        task = todoist.add_task(content)

        thread = await msg.channel.create_thread(
            name=content,
            auto_archive_duration=thread_archive_time,
            message=msg)

        entity = TaskEntity(discord_channel_id=msg.channel.id,
                            discord_msg_id=msg.id,
                            discord_thread_id=thread.id,
                            todoist_task_id=task.id)

        self.db.insert(entity)

        await self.report(entity, reaction=managed_msg_reaction)
