from asyncio import Queue
from aiohttp import web
from discord.ext import tasks
import logging

from src.WebhookServer.WebController import WebController


@tasks.loop()
async def web_server(queue: Queue):
    app = web.Application()
    controller = WebController(queue)

    app.add_routes([
        web.get("/", controller.welcome),
        web.get("/login", controller.login),
        web.get("/access_token", controller.access_token),
        web.post("/payload", controller.payload),
    ])

    runner = web.AppRunner(app)
    await runner.setup()

    site = web.TCPSite(runner, host='0.0.0.0', port=5100)
    await site.start()

    logging.info("WebServer started")
