from typing import Any, Dict, Type
from pymongo import MongoClient
from src.Database.Entities import ProjectEntity, TaskEntity
from src.config import connection_string


class Database:

    def __init__(self):
        client = MongoClient(connection_string)
        self.db: Database = client.get_database("todoist")
        self._tasks = self.db['tasks']
        self._projects = self.db['projects']
        self._types = {
            TaskEntity: self._tasks,
            ProjectEntity: self._projects
        }

    def find_one(self, type: Type, dict: Dict[Any, Any]):
        db = self._types[type]
        selected = db.find_one(dict)
        return type.from_dict(selected) if selected else None

    def insert(self, entity: Any, t: Type = None):
        if t is None:
            t = type(entity)
        db = self._types[t]
        db.insert_one(entity.to_dict())
