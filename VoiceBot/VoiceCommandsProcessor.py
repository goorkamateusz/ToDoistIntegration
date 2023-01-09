import os
from typing import List
import difflib

from todoist_api_python.models import Task

from src.LanguageProcessor.Processor import Result
from src.ToDoist.ApiClient import ApiClientProvider
from VoiceBot.VoiceOutput import VoiceOutput


class VoiceCommandsProcessor:

    def __init__(self) -> None:
        provider = ApiClientProvider()
        self.__client = provider.create_client(
            access_token=os.getenv("voice_access_token"),
            project_id=os.getenv("voice_project_id")
        )
        self.__voice = VoiceOutput()
        self.processors = {
            "add": self.add_task,
            "select": self.select_task,
            "done": self.done_task,
            "delete": self.delete_task,
            "update": self.update_task,
        }
        self.__selected_task: Task = None

    def process(self, commands: List[Result]):
        if len(commands) == 0:
            return

        c = commands[0]

        self.__voice.speak(f"Przetwarzam polecenie: {c.text}")

        if c.command in self.processors:
            self.processors[c.command](c)

    def add_task(self, c: Result):
        self.__client.add_task(c.dict["content"])
        print("dodano zadanie")

    def select_task(self, c: Result):

        tasks = self.__client.get_tasks()
        possibilities: List[str] = [t.content for t in tasks]

        contnet = c.dict["content"]

        closes = difflib.get_close_matches(contnet, possibilities)

        if len(closes) > 0:
            closest = closes[0]
            id = possibilities.index(closest)
            self.__selected_task = tasks[id]
            self.__voice.speak(f"Wybrałeś: {closes[0]}")
        else:
            self.__voice.speak("Nie można znaleźć zadania")

    def delete_task(self, c: Result):

        if self.__selected_task is None:
            self.__voice.speak("Nie wybrałeś zadania")
            return

        self.__client.delete_task(self.__selected_task.id)
        self.__voice.speak("Usunąłeś zadanie")

    def done_task(self, c: Result):

        if self.__selected_task is None:
            self.__voice.speak("Nie wybrałeś zadania")
            return

        self.__client.close_task(self.__selected_task.id)
        self.__voice.speak("Zakończyłeś zadanie")

    def update_task(self, c: Result):

        if self.__selected_task is None:
            self.__voice.speak("Nie wybrałeś zadania")
            return

        content = c.dict["content"]
        self.__client.update_task(self.__selected_task.id, content)
        self.__voice.speak("Zedytowałeś zadanie")
