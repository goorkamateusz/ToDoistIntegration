import pyttsx3 as tts


class VoiceOutput:
    def __init__(self) -> None:
        self.engine: tts.Engine = tts.init()
        self.engine.setProperty('rate', 150)
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[0].id)

    def speak(self, text: str) -> None:
        print(text)
        self.engine.say(text)
        self.engine.runAndWait()
