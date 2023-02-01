import logging
from typing import Any, Dict, List
from DiscordBot.Database.Entities import TaskEntity, ProjectEntity
from DiscordBot.Discord.DiscordComponent import OnNotificationComponent
from DiscordBot.Discord.Reactions import managed_msg_reaction
from DiscordBot.config import thread_archive_time


class OnAdded(OnNotificationComponent):

    async def process(self, event) -> None:
        event_data: Dict[str, Any] = event["event_data"]
        task_id = event_data["id"]

        if self.db_tasks.find_one({"todoist_task_id": task_id}):
            logging.info(f"Task have been added yet | {task_id}")
            return

        project_id = event_data["project_id"]
        entities: List[ProjectEntity] = self.db.find(
            ProjectEntity, {"todoist_project_id": project_id})

        for entity in entities:
            channel = self.client.get_channel(entity.discord_channel_id)
            content = event_data["content"]

            msg = await channel.send(content)

            thread = await channel.create_thread(
                name=content,
                auto_archive_duration=thread_archive_time,
                message=msg)

            entity = TaskEntity(msg.channel.id, msg.id, thread.id, task_id)

            self.db.insert(entity)

            communicate = "Dodano zadanie przez aplikację"
            await self.report(entity, communicate, managed_msg_reaction)
