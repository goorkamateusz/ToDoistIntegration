from Common.LanguageProcessor.Processor import LanguageProcessor
from Common.ToDoist.ApiClient import ApiClientProvider
from DiscordBot.Database.Database import Database


class Container:
    apiClientProvider: ApiClientProvider = ApiClientProvider()
    database: Database = Database()
    languageProcessor: LanguageProcessor = LanguageProcessor(
        "data/rules/pl-PL.json")
