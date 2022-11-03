import logging
from typing import Any, Dict, List
from src.Database.Entities import TaskEntity
from src.Discord.Reactions import done_reaction
from src.Discord.DiscordClient import OnNotificationComponent


class OnComplete(OnNotificationComponent):
    async def process(self, event) -> None:
        event_data: Dict[str, Any] = event["event_data"]

        id = event_data["id"]
        entities: List[TaskEntity] = self.db.find(
            TaskEntity, {"todoist_task_id": id})

        for entity in entities:
            await self.report(entity,
                              "Zamknięto zadanie w aplikacji ToDoist",
                              done_reaction)
            logging.info(f"Notification processed successfully | {id}")
