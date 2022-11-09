from VoiceBot.VoiceInput import VoiceInput
from VoiceBot.VoiceOutput import VoiceOutput
from src.ToDoist.ApiClient import ApiClient

if __name__ == "__main__":
    input = VoiceInput()

    text: str = input.get_text()
    print(text)
