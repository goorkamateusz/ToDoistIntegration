import logging
import discord
from src.Database.Entities import ProjectEntity
from src.Discord.DiscordClient import OnMessageComponent


class SelectToDoistProject(OnMessageComponent):
    """ Select ToDoist project to channel
    """

    async def process(self, msg: discord.Message, content: str) -> None:
        channel = msg.channel
        filter = {"discord_channel_id": channel.id}
        project: ProjectEntity = self.db.find_one(ProjectEntity, filter)

        if not project:
            await msg.reply(
                "Najpierw połącz aplikację ToDoist poprzez komendę:\n\
`!todoist <api token>`")
            return

        client = self.todoist.get_client(channel.id)
        projects = client._api.get_projects()

        selected_proj = next((p for p in projects if p.name == content), None)

        if not selected_proj:
            await msg.reply(
                "Nie znaleziono wybranego projektu. Spróbuj jeszcze raz.")
            return

        self.db.update_one(
            ProjectEntity,
            filter,
            {"$set": {"todoist_project_id": selected_proj.id}})

        client.select_project(selected_proj.id)

        await msg.reply("Połączono projekt")
