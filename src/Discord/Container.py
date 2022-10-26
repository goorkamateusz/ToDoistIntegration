from src.ToDoist.ApiClient import ApiClient
from src.Database.Database import Database

class Container:
    apiClient: ApiClient = ApiClient()
    database: Database = Database()
