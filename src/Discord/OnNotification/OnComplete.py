import logging
import discord
from typing import Any, Dict
from src.Database.TaskMsg import TaskMsg
from src.Discord.Reactions import done_reaction
from src.Discord.DiscordClient import OnNotificationComponent


class OnComplete(OnNotificationComponent):
    async def process(self, event) -> None:
        event_data: Dict[str, Any] = event["event_data"]

        id = event_data["id"]
        select = self.db.find_one({"todoist_task_id": id})

        if select:
            record: TaskMsg = TaskMsg.from_dict(select)

            channel = self.client.get_channel(record.discord_channel_id)
            msg = channel.get_partial_message(record.discord_msg_id)

            await msg.add_reaction(done_reaction)

            logging.info(f"Notification processed successfully | {id}")
            return

        logging.info(f"Task not registered | {id}")
