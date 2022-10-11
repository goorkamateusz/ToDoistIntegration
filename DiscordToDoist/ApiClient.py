from helpers import read_token
from todoist_api_python.api import TodoistAPI

class ApiClient:
    def __init__(self) -> None:
        self.api = self.__get_todoist_api()

    def __get_todoist_api(self) -> TodoistAPI:
        token = read_token("~token")
        api = TodoistAPI(token)

        try:
            return api
        except Exception as error:
            raise Exception(error)
