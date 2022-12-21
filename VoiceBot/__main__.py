import threading
import time
from typing import Any, Dict, List
from VoiceBot.VoiceCommandsProcessor import VoiceCommandsProcessor
from VoiceBot.VoiceInput import VoiceInput
from VoiceBot.VoiceOutput import VoiceOutput
from src.LanguageProcessor.Processor import LanguageProcessor, Result


class myThread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.con: bool = True
        self.print: bool = False
        self.msg: str = "Słucham"
        self.length: int = 20

    def run(self):
        dots = 3
        while self.con:
            if self.print:
                dots = (dots + 1) % 4
                bar = ("." * dots)
                print(f"\r{self.msg}{bar}".ljust(self.length, " "), end='')
            time.sleep(0.5)


def process_alterantives(processor: LanguageProcessor, result) -> List[Result]:
    commands: List[Result] = list()
    for alternative in result["alternative"]:
        transcript = alternative["transcript"]
        print(transcript)
        command: List[Result] = processor.process(transcript)
        if command is not None:
            commands.extend(command)
    return commands


def validate_input(result):
    return isinstance(result, dict)


if __name__ == "__main__":
    input = VoiceInput()
    processor = LanguageProcessor("data/rules/pl-PL.json")
    commands_processor = VoiceCommandsProcessor()
    speech = myThread()
    speech.start()

    try:
        while True:
            speech.print = True
            result: Dict[str, Any] = input.get_text(speech)

            if validate_input(result):
                print()
                speech.print = False
                commands = process_alterantives(processor, result)
                commands_processor.process(commands)

                if commands is not None:
                    for c in commands:
                        print(c)

    except KeyboardInterrupt:
        print('You pressed ctrl+c')
        pass

    speech.con = False
