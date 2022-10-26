import discord
from src.DiscordToDoist.Reactions import done_reaction
from src.Database.TaskMsg import TaskMsg
from src.DiscordToDoist.Container import Container
from src.Database.Database import Database
from src.DiscordToDoist.DiscordClient import OnMessageComponent


class DoneTask(OnMessageComponent):
    async def process(self, msg: discord.Message, content: str) -> None:
        # todo make dependency injection
        todoist = Container.apiClient

        db = Database().discord
        select = db.find_one({"discord_thread_id": msg.channel.id})
        entity: TaskMsg = TaskMsg.from_dict(select)

        if todoist.close_task(entity.todoist_task_id):
            thread = self.client.get_channel(entity.discord_thread_id)
            await thread.send(f"Zamknięto zadanie {done_reaction}")

            channel = self.client.get_channel(entity.discord_channel_id)
            starter_msg = channel.get_partial_message(entity.discord_msg_id)
            await starter_msg.add_reaction(done_reaction)

        else:
            await msg.channel.send("Coś poszło nie tak... Nie udało się zamknąć zadania")
