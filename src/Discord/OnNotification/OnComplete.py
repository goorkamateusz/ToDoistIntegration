import logging
from typing import Any, Dict
from src.Database.Entities import TaskEntity
from src.Discord.Reactions import done_reaction
from src.Discord.DiscordClient import OnNotificationComponent


class OnComplete(OnNotificationComponent):
    async def process(self, event) -> None:
        event_data: Dict[str, Any] = event["event_data"]

        id = event_data["id"]
        entity: TaskEntity = self.db.find_one(
            TaskEntity, {"todoist_task_id": id})

        if entity:
            communicate = "Zamknięto zadanie w aplikacji ToDoist"
            await self.report(entity,
                              communicate=communicate,
                              reaction=done_reaction)
            logging.info(f"Notification processed successfully | {id}")
        else:
            logging.info(f"Task not registered | {id}")
