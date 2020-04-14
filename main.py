from aiohttp import web
import aiohttp_jinja2
import jinja2
import socketio
import os
from socket_routes import create_socket_routes
from http_routes import routes
from globals.globals import *
from globals.functions import *

user_only_paths = [
    "/admin",
    "/admin_auth",
    "/static/admin.css",
    "/static/admin.js"
]


@web.middleware
async def middleware(request: web.Request, handler):
    user_id = get_user_id(request)
    path = request.path
    print(path)
    is_admin = False
    if user_id in cache:
        is_admin = cache[user_id]["is_admin"]
    if path in user_only_paths:
        if not is_admin:
            return await handler(request)
        return web.HTTPFound("/admin")
    if is_admin:
        return await handler(request)
    return web.HTTPFound("/admin")


app = web.Application(middlewares=[middleware])
print(socketio)
socket = socketio.AsyncServer()
socket.attach(app)
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('static/'))
PORT = os.getenv("PORT", 5000)

create_socket_routes(socket)

app.add_routes(routes)

if __name__ == "__main__":
    web.run_app(app, port=PORT)
