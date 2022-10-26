from pymongo import MongoClient

from src.config import connection_string


class Database:
    def __init__(self):
        client = MongoClient(connection_string)
        self.db: Database = client.get_database("todoist")
        self.discord = self.db['discord']
