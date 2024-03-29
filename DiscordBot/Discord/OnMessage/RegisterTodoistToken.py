import logging
import discord
from DiscordBot.Database.Entities import ProjectEntity
from DiscordBot.Discord.DiscordClient import OnMessageComponent


class RegisterToDoistToken(OnMessageComponent):
    """ Adding todoist api token to channel
    """
    
    async def process(self, msg: discord.Message, content: str) -> None:
        token = content

        channel_id = msg.channel.id
        jump_id = msg.channel.jump_url.split("/")[-1]

        project = ProjectEntity(discord_channel_id=channel_id,
                                discord_channel_jump_id=jump_id,
                                todoist_token=token,
                                todoist_project_id=None)

        self.db.insert_or_update({"discord_channel_id": msg.channel.id},
                                 project)

        await msg.reply("Dodano połączenie. \
            Wiadomość z tokenem zostanie usunięta automatycznie.")
        await msg.delete()
