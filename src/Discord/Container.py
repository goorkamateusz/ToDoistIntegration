from src.ToDoist.ApiClient import ApiClient


class Logger:
    def log(self, msg: str):
        print(f"[{msg}]")


class Container:
    apiClient: ApiClient = ApiClient()
    logger = Logger()
