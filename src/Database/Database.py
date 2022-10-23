from pymongo import MongoClient

from src.config import connection_string


class Database:
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

    def __init__(self):
        client = MongoClient(connection_string)
        self.db: Database = client.get_database("todoist")
