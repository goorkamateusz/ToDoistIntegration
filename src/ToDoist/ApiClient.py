from typing import Dict, List
import logging
from requests import HTTPError
from todoist_api_python.api import Project, Task, TodoistAPI
from src.Database.Entities import ProjectEntity
from src.Database.Database import Database


class NotSelectedProjectError(Exception):
    pass


class ApiClient:
    def __init__(self, api: TodoistAPI, project_id: str) -> None:
        self._api: TodoistAPI = api
        self.__project_id: str | None = project_id

    @property
    def is_project_selected(self) -> bool:
        return self.__project_id is not None

    def add_task(self, content: str) -> Task:
        if self.__project_id is None:
            raise NotSelectedProjectError()
        return self._api.add_task(
            content=content, project_id=self.__project_id)

    def close_task(self, task_id: str) -> bool:
        return self._api.close_task(task_id)

    def update_task(self, task_id: str, new_content: str) -> bool:
        return self._api.update_task(task_id, content=new_content)

    def select_project(self, project_id: str) -> None:
        self.__project_id = project_id

    def add_comment(self, task_id: str, content: str) -> bool:
        return self._api.add_comment(task_id=task_id, content=content)

    def delete_task(self, task_id: str) -> bool:
        return self._api.delete_task(task_id)

    def get_tasks(self) -> List[Task]:
        return self._api.get_tasks(project_id=self.__project_id)


class ApiClientProvider:
    def __init__(self) -> None:
        self._channels: Dict[str, ApiClient] = {}
        self.db: Database

    def get_client(self, channel_id: str) -> ApiClient:
        if channel_id in self._channels:
            return self._channels[channel_id]
        else:
            return self._try_to_connect_client(channel_id)

    def _try_to_connect_client(self, channel_id: str):
        try:
            client = self._create_client(channel_id)
            if client:
                self._channels[channel_id] = client
                return client

        except HTTPError as error:
            logging.error(error)

        return None

    def _create_client(self, channel_id: str):
        project: ProjectEntity = self.db.find_one(
            ProjectEntity, {"discord_channel_id": channel_id})

        if project:
            access_token = project.todoist_token
            project_id = project.todoist_project_id
            client = self.create_client(access_token, project_id)
            return client

        return None

    def create_client(self, access_token, project_id):
        api = TodoistAPI(access_token)

        proj_id = None
        if project_id:
            proj_id = project_id

        client = ApiClient(api, proj_id)
        return client
