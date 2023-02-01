import discord
from Common.LanguageProcessor.Processor import Result
from Common.ToDoist.ApiClient import ApiClient
from DiscordBot.Discord.Reactions import managed_msg_reaction, error_reaction
from DiscordBot.Database.Entities import TaskEntity
from DiscordBot.Discord.DiscordClient import OnMessageComponent


class AddComment(OnMessageComponent):
    """ Add comment to task
    """

    async def process(self, msg: discord.Message, content: str) -> None:
        entity: TaskEntity = self.db.find_one(
            TaskEntity, {"discord_thread_id": msg.channel.id})

        todoist: ApiClient = self.todoist.get_client(entity.discord_channel_id)

        comment_content = f"🤖 {msg.author.name}: {content}"

        if todoist.add_comment(entity.todoist_task_id, comment_content):
            await msg.add_reaction(managed_msg_reaction)
        else:
            await msg.add_reaction(error_reaction)

    async def process_command(self, msg: discord.Message, command: Result):
        await self.process(msg, command.dict["content"])
