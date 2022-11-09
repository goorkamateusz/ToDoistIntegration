from VoiceBot.VoiceInput import VoiceInput
from VoiceBot.VoiceOutput import VoiceOutput
from src.LanguageProcessor.Processor import LanguageProcessor

if __name__ == "__main__":
    input = VoiceInput()
    processor = LanguageProcessor()

    text: str = input.get_text()
    print(text)
    processor.process(text)
