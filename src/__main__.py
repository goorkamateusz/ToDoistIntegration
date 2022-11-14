from src.Discord.DiscordBot import main
from src.config import logging_file
import logging
from logging.handlers import RotatingFileHandler
import sys


def config_logging():
    formatter = logging.Formatter(fmt='%(asctime)s %(levelname)s %(message)s')

    stream = logging.StreamHandler(sys.stdout)
    stream.setFormatter(formatter)
    logging.getLogger().addHandler(stream)

    if logging_file:
        file = RotatingFileHandler(
            filename=logging_file, maxBytes=500 * 1024, encoding='utf-8')
        file.setFormatter(formatter)
        logging.getLogger().addHandler(file)

        logging.getLogger().setLevel(logging.INFO)


if __name__ == "__main__":
    config_logging()

    logging.info("App started")
    logging.info("-" * 60)

    main()

    logging.info("App stopped")
    logging.info("-" * 60)
