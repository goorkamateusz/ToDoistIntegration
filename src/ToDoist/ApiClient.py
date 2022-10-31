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
        self._api = ApiClientProvider.__get_todoist_api()
        self._selected_project: Project = None
        self.__select_project()

    def get_client(self, channel_id: str) -> ApiClient:
        # todo WIP
        return ApiClient(self._api, self._selected_project.id)

    def __select_project(self) -> None:
        proj = next(p for p in self._api.get_projects()
                    if p.name == "Todoist_Integration_TEST")
        self._selected_project = proj

    @staticmethod
    def __get_todoist_api() -> TodoistAPI:
        try:
            api = TodoistAPI(todoist_token)
            return api
        except Exception as error:
            raise Exception(error)
