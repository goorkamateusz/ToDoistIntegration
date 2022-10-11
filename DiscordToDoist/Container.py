from ApiClient import ApiClient


class Logger:
    def log(self):
        print("logged")


class Container:
    apiClient: ApiClient = ApiClient()
    logger = Logger()
