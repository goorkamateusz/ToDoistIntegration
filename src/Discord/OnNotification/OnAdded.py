import logging
from typing import Any, Dict
from src.Database.TaskMsg import TaskMsg
from src.Discord.DiscordComponent import OnNotificationComponent
from src.Discord.Reactions import managed_msg_reaction
from src.config import temp_channel_id


class OnAdded(OnNotificationComponent):
    async def process(self, event) -> None:
        event_data: Dict[str, Any] = event["event_data"]
        task_id = event_data["id"]

        if self.db.find_one({"todoist_task_id": task_id}):
            logging.info(f"Task have been added yet | {task_id}")
            return

        channel_id = int(temp_channel_id)
        channel = self.client.get_channel(channel_id)
        content = event_data["content"]

        msg = await channel.send(content)
        thread = await channel.create_thread(
            name=content,
            auto_archive_duration=(60 * 24),
            message=msg
        )

        entity = TaskMsg(temp_channel_id, msg.id, thread.id, task_id)

        self.db.insert_one(entity.to_dict())

        communicate = "Dodano zadanie przez aplikację"
        await self.report(entity, communicate, managed_msg_reaction)
