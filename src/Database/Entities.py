from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class TaskEntity:
    discord_channel_id: str
    discord_msg_id: str
    discord_thread_id: str
    todoist_task_id: str


@dataclass_json
@dataclass
class ProjectEntity:
    discord_channel_id: str
    discord_channel_jump_id: str
    todoist_token: str
    todoist_project_id: str | None
