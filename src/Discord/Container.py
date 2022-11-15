from src.LanguageProcessor.Processor import LanguageProcessor
from src.ToDoist.ApiClient import ApiClientProvider
from src.Database.Database import Database


class Container:
    apiClientProvider: ApiClientProvider = ApiClientProvider()
    database: Database = Database()
    languageProcessor: LanguageProcessor = LanguageProcessor(
        "data/rules/pl-PL.json")


# hotfix
Container.apiClientProvider.db = Container.database
