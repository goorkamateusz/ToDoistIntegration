from helpers import read_token
from todoist_api_python.api import TodoistAPI


class ProjectService:
    def __init__(self, api: TodoistAPI, project_id: str):
        self.api = api
        self.project_id = project_id


class ApiClient:
    def __init__(self) -> None:
        self._api = ApiClient.__get_todoist_api()
        self._selected_project: ProjectService = None

    def select_project(self) -> None:
        raise NotImplemented()

    @staticmethod
    def __get_todoist_api() -> TodoistAPI:
        token = read_token("~token")
        api = TodoistAPI(token)

        try:
            return api
        except Exception as error:
            raise Exception(error)
