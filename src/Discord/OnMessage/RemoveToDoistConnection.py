import logging
import discord
from src.Database.Entities import ProjectEntity
from src.Discord.DiscordClient import OnMessageComponent


class RemoveToDoistConnection(OnMessageComponent):
    """ Remove ToDoist connection
    """
    
    async def process(self, msg: discord.Message, content: str) -> None:
        result = self.db.delete_one(
            ProjectEntity, {"discord_channel_id": msg.channel.id})

        if result.deleted_count > 0:
            await msg.reply("Usunięto token")
        else:
            await msg.reply("Nie podłączono aplikacji na tym kanale")
