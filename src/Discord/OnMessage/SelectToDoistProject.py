import logging
import discord
from src.Database.ProjectEntity import ProjectEntity
from src.Discord.DiscordClient import OnMessageComponent


class SelectToDoistProject(OnMessageComponent):
    """ Select ToDoist project to channel
    """
    async def process(self, msg: discord.Message, content: str) -> None:
        channel = msg.channel
        project = self.db.find_one(
            ProjectEntity, {"discord_channel_id": channel.id})

        if project:
            await msg.reply("WIP")

        else:
            await msg.reply(
                "Najpierw połącz aplikację ToDoist poprzez komendę:\
                `!todoist <api token>`",
                mention_author=False
            )
