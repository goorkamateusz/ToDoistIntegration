import logging
from typing import Any, Dict
from src.Database.Entities import TaskEntity
from src.Discord.DiscordComponent import OnNotificationComponent
from src.Discord.Reactions import deleted_message


class OnDeleted(OnNotificationComponent):

    async def process(self, event) -> None:
        event_data: Dict[str, Any] = event["event_data"]
        task_id = event_data["id"]

        logging.info("Task deleting")

        entites = self.db.find(TaskEntity, {"todoist_task_id": task_id})

        if entites is None:
            logging.info(f"Task have been deleted yet | {task_id}")
            return

        self.db.delete_one(
            TaskEntity, {"todoist_task_id": task_id})

        for entity in entites:
            await self.report(entity, "Usunięto zadanie", deleted_message)
