from asyncio import Queue
from aiohttp import web
import requests

from src.config import client_id, scope, client_secret


class WebController:
    def __init__(self, queue: Queue) -> None:
        self._eventQueue = queue
        pass

    async def welcome(self, request: web.Request):
        return web.Response(text="App work correctly.\
            \nSorce code: https://github.com/goorkamateusz/ToDoistIntegration")

    async def login(self, request: web.Request):
        state = "state"  # ???
        url = f"https://todoist.com/oauth/authorize?\
            client_id={client_id}&scope={scope}&state={state}"
        return web.HTTPFound(url)

    async def access_token(self, request: web.Request):
        code = request.rel_url.query['code']
        requests.post("https://todoist.com/oauth/access_token", json={
            "client_id": client_id,
            "client_secret": client_secret,
            "code": code
        })
        return web.Response(text="Verified")

    async def payload(self, request: web.Request):
        if request.body_exists:
            await request.read()
            json = await request.json()
            await self._eventQueue.put(json)
        return web.Response(status=200)

    async def test(self, request: web.Request):
        print(request.body_exists)

        if request.body_exists:
            print(await request.json())

        return web.Response(status=200)
