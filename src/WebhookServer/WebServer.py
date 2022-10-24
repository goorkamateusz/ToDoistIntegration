from aiohttp import web
from discord.ext import tasks

from src.WebhookServer.WebController import routes
from src.DiscordToDoist.Container import Container, Logger

app = web.Application()
app.add_routes(routes)


@tasks.loop()
async def web_server():
    logger: Logger = Container.logger
    runner = web.AppRunner(app)
    await runner.setup()

    site = web.TCPSite(runner, host='0.0.0.0', port=5100)
    await site.start()

    logger.log("WebServer started")
