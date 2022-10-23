from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class TaskMsg:
    discord_msg_id: str
    discord_thread_id: str
    todoist_task_id: str
