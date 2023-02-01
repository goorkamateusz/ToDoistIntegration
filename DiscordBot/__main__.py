import sys
import logging
from logging.handlers import RotatingFileHandler
from DiscordBot.config import logging_file
from DiscordBot.Database.MongoDbClientProvider import MongoDbClientProvider


def config_logging():
    formatter = logging.Formatter(fmt='%(asctime)s %(levelname)s %(message)s')

    stream = logging.StreamHandler(sys.stdout)
    stream.setFormatter(formatter)
    stream.setLevel(logging.INFO)
    logging.getLogger().addHandler(stream)

    if logging_file:
        file = RotatingFileHandler(
            filename=logging_file, maxBytes=500 * 1024, encoding='utf-8')
        file.setFormatter(formatter)
        file.setLevel(logging.INFO)
        logging.getLogger().addHandler(file)


if __name__ == "__main__":
    config_logging()
    MongoDbClientProvider().try_to_start_connection()

    # hotfix
    from DiscordBot.Discord.Container import Container
    from DiscordBot.Discord.DiscordBot import main
    Container.apiClientProvider.db = Container.database

    logging.info("App started")
    logging.info("-" * 60)

    main()

    logging.info("App stopped")
    logging.info("-" * 60)
