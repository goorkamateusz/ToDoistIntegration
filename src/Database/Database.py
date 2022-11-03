from typing import Any, Dict, Type
from pymongo import MongoClient
from pymongo.results import DeleteResult
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

    def insert(self, entity: Any):
        t = type(entity)
        self._types[t].insert_one(entity.to_dict())

    def update_one(self,
                   t: Type,
                   filter: Dict[Any, Any],
                   value: Dict[Any, Any]):
        self._types[t].update_one(filter, value)

    def delete_one(self, t: Type, filter: Dict[Any, Any]) -> DeleteResult:
        return self._types[t].delete_one(filter)

    def insert_or_update(self, filter: Dict[Any, Any], entity: Any):
        t = type(entity)
        self._types[t].update_one(filter,
                                  {"$set": entity.to_dict()},
                                  upsert=True)
