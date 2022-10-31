from typing import Dict
import logging
from requests import HTTPError
from todoist_api_python.api import Project, Task, TodoistAPI
from src.config import todoist_token


class ApiClient:
    def __init__(self, api: TodoistAPI, project_id: str) -> None:
        self._api: TodoistAPI = api
        self.__project_id: str = project_id

    def add_task(self, content: str) -> Task:
        return self._api.add_task(
            content=content, project_id=self.__project_id)

    def close_task(self, task_id: str) -> bool:
        return self._api.close_task(task_id)

    def update_task(self, task_id: str, new_content: str) -> bool:
        return self._api.update_task(task_id, content=new_content)


class ApiClientProvider:
    def __init__(self) -> None:
        self._channels: Dict[str, ApiClient] = {}

    def get_client(self, channel_id: str) -> ApiClient:
        if channel_id in self._channels:
            return self._channels[channel_id]
        else:
            return self._try_to_connect_client(channel_id)

    def _try_to_connect_client(self, channel_id: str):
        try:
            # todo todoist token & project
            api = TodoistAPI(todoist_token)

            proj: Project = next(p for p in api.get_projects()
                                 if p.name == "Todoist_Integration_TEST")

            client = ApiClient(api, proj.id)

            self._channels[channel_id] = client
            return client

        except HTTPError as error:
            if error.response.status_code == 403:
                return None
            else:
                logging.error(error)
