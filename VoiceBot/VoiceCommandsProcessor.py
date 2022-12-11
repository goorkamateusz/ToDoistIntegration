import os
from typing import List

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
            "add": self.add_task
        }

    def process(self, commands: List[Result]):
        if len(commands) == 0:
            return

        c = commands[0]

        self.__voice.speak(c.text)

        if c.command in self.processors:
            self.processors[c.command](c)

    def add_task(self, c: Result):
        self.__client.add_task(c.dict["content"])
        print("dodano zadanie")
