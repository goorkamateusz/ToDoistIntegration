import discord
from src.Database.TaskMsg import TaskMsg
from src.DiscordToDoist.Container import Container
from src.Database.Database import Database
from src.DiscordToDoist.DiscordClient import DiscordComponent


class DoneTask(DiscordComponent):
    async def process(self, msg: discord.Message, content: str) -> None:
        # todo make dependency injection
        todoist = Container.apiClient
        db = Database().db['discord']

        select = db.find_one({"discord_thread_id": msg.channel.id})
        entity: TaskMsg = TaskMsg.from_dict(select)

        if todoist.close_task(entity.todoist_task_id):
            await msg.add_reaction('✅')

            if isinstance(msg.channel, discord.Thread):
                thread: discord.Thread = msg.channel
                if thread.starter_message:
                    await thread.starter_message.add_reaction('✅')
                    print("starter_message")

            channel = self.client.get_channel(entity.discord_channel_id)
            starter_msg = channel.get_partial_message(entity.discord_msg_id)
            await starter_msg.add_reaction('✅')

        else:
            await msg.channel.send("Coś poszło nie tak... Nie udało się zamknąć zadania")
