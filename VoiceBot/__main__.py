import threading
import time
from typing import Any, Dict
from VoiceBot.VoiceInput import VoiceInput
from VoiceBot.VoiceOutput import VoiceOutput
from src.LanguageProcessor.Processor import LanguageProcessor


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


if __name__ == "__main__":
    input = VoiceInput()
    processor = LanguageProcessor("data/rules/pl-PL.json")
    speech = myThread()
    speech.start()

    try:
        while True:
            speech.print = True
            output: Dict[str, Any] = input.get_text(speech)

            if output is not None:
                print(output)
                speech.print = False

                for alt in output["alternative"]:
                    commands = processor.process(alt["transcript"])

                for c in commands:
                    print(c)

    except KeyboardInterrupt:
        print('You pressed ctrl+c')
        pass

    speech.con = False
