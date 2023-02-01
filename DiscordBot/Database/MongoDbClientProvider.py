import logging
from time import sleep
from typing import Any
from pymongo import MongoClient, errors
from DiscordBot.config import connection_string


class MongoDbClientProvider:
    __instance = None

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        if MongoDbClientProvider.__instance is None:
            MongoDbClientProvider.__instance = MongoDbClientProvider()
        return MongoDbClientProvider.__instance

    def __init__(self) -> None:
        self.__client = None

    def start_connection(self) -> bool:
        try:
            client = MongoClient(connection_string,
                                 serverSelectionTimeoutMS=5000)
            client.server_info()
            self.__client = client
            return True
        except Exception as err:
            logging.exception(err)
        return False

    def try_to_start_connection(self) -> None:
        print("[database]")
        print(connection_string)

        while not self.start_connection():
            sleep(2.5)

        logging.info("connected with database")

    def get_client(self) -> MongoClient:
        if self.__client is None:
            self.start_connection()
        return self.__client
