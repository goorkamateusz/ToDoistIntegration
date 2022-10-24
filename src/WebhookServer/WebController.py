from aiohttp import web
import requests

from src.config import client_id, scope, client_secret

routes = web.RouteTableDef()


@routes.get('/')
async def welcome(request: web.Request):
    return web.Response(text="App work correctly.\nSorce code: https://github.com/goorkamateusz/ToDoistIntegration")


@routes.get("/login")
async def login(request: web.Request):
    state = "state"  # ???
    url = f"https://todoist.com/oauth/authorize?client_id={client_id}&scope={scope}&state={state}"
    return web.HTTPFound(url)


@routes.get("/access_token")
async def access_token(request: web.Request):
    code = request.rel_url.query['code']
    requests.post("https://todoist.com/oauth/access_token", json={
        "client_id": client_id,
        "client_secret": client_secret,
        "code": code
    })
    return web.Response(text="Verified")


@routes.post("/payload")
async def payload(request: web.Request):
    r = request
    print(f"{r.method} / {r.url}")
    if r.body_exists:
        await r.read()
        json = await r.json()
    print(json)
    return web.Response(status=200)
