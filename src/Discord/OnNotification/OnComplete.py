import logging
from typing import Any, Dict
from src.Database.TaskEntity import TaskEntity
from src.Discord.Reactions import done_reaction
from src.Discord.DiscordClient import OnNotificationComponent


class OnComplete(OnNotificationComponent):
    async def process(self, event) -> None:
        event_data: Dict[str, Any] = event["event_data"]

        id = event_data["id"]
        select = self.db_tasks.find_one({"todoist_task_id": id})

        if select:
            entity: TaskEntity = TaskEntity.from_dict(select)
            communicate = "Zamknięto zadanie w aplikacji ToDoist"
            await self.report(entity,
                              communicate=communicate,
                              reaction=done_reaction)
            logging.info(f"Notification processed successfully | {id}")
        else:
            logging.info(f"Task not registered | {id}")
