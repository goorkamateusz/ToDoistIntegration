import discord
from src.LanguageProcessor.Processor import Result
from src.ToDoist.ApiClient import ApiClient
from src.Discord.Reactions import managed_msg_reaction, error_reaction
from src.Database.Entities import TaskEntity
from src.Discord.DiscordClient import OnMessageComponent


class AddComment(OnMessageComponent):

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
