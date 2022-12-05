import speech_recognition as sr


class VoiceInput:
    def __init__(self) -> None:
        self.r: sr.Recognizer = sr.Recognizer()
        self.language: str = 'pl-PL'

    def get_text(self, msg: str = "Słucham...") -> str:
        with sr.Microphone() as source:
            try:
                print(msg)
                audio = self.r.listen(source)
                text = self.r.recognize_google(audio, language=self.language)
                return text
            except Exception as e:
                print(e)
                return None
