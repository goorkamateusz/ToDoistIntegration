import discord
from src.Discord.Reactions import managed_msg_reaction
from src.Database.TaskMsg import TaskMsg
from src.Discord.DiscordClient import OnMessageComponent


class AddingTask(OnMessageComponent):

    async def process(self, msg: discord.Message, content: str) -> None:
        task = self.todoist.add_task(content)

        thread = await msg.channel.create_thread(
            name=content,
            auto_archive_duration=(60 * 24),
            message=msg)

        entity = TaskMsg(msg.channel.id, msg.id, thread.id, task.id)
        self.db.insert_one(entity.to_dict())

        await self.report(entity, reaction=managed_msg_reaction)
