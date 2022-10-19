from todoist_api_python.api import Project, TodoistAPI
from src.config_priv import todoist_token


class ApiClient:
    def __init__(self) -> None:
        self._api = ApiClient.__get_todoist_api()
        self._selected_project: Project = None
        self.select_project()

    def select_project(self) -> None:
        p: Project = None
        proj = next(p for p in self._api.get_projects()
                    if p.name == "Todoist_Integration_TEST")
        self._selected_project = proj

    def add_task(self, content: str) -> None:
        self._api.add_task(
            content=content, project_id=self._selected_project.id)

    @staticmethod
    def __get_todoist_api() -> TodoistAPI:
        api = TodoistAPI(todoist_token)

        try:
            return api
        except Exception as error:
            raise Exception(error)
