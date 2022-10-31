from src.ToDoist.ApiClient import ApiClientProvider
from src.Database.Database import Database


class Container:
    apiClientProvider: ApiClientProvider = ApiClientProvider()
    database: Database = Database()
