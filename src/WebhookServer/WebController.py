from aiohttp import web
from discord.ext import tasks

app = web.Application()
routes = web.RouteTableDef()


@routes.get('/')
async def welcome(request):
    return web.Response(text="Hello world")

app.add_routes(routes)


@tasks.loop()
async def web_server():
    runner = web.AppRunner(app)
    print("aa")
    await runner.setup()
    print("bb")
    site = web.TCPSite(runner, host='0.0.0.0', port=5100)
    await site.start()
    print("cc")
