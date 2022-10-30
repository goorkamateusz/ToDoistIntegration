import discord
from src.Discord.Reactions import managed_msg_reaction
from src.Database.TaskEntity import TaskEntity
from src.Discord.DiscordClient import OnMessageComponent


class AddingTask(OnMessageComponent):

    async def process(self, msg: discord.Message, content: str) -> None:
        task = self.todoist.add_task(content)

        thread = await msg.channel.create_thread(
            name=content,
            auto_archive_duration=(60 * 24),
            message=msg)

        entity = TaskEntity(discord_channel_id=msg.channel.id,
                            discord_msg_id=msg.id,
                            discord_thread_id=thread.id,
                            todoist_task_id=task.id)

        self.db_tasks.insert_one(entity.to_dict())

        await self.report(entity, reaction=managed_msg_reaction)
