import speech_recognition as sr


class VoiceInput:
    def __init__(self) -> None:
        self.r: sr.Recognizer = sr.Recognizer()
        self.language: str = 'pl-PL'

    def get_text(self, thread) -> str:
        with sr.Microphone() as source:
            try:
                thread.msg = "Słucham"
                audio = self.r.listen(source)
                thread.msg = "Przetwarzam"
                text = self.r.recognize_google(
                    audio, language=self.language, show_all=True)
                return text
            except Exception:
                return None
