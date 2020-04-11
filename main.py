from aiohttp import web
import aiohttp_jinja2
import jinja2
import socketio
import os
from socket_routes import create_socket_routes
from http_routes import routes

app = web.Application()
print(socketio)
socket = socketio.AsyncServer()
socket.attach(app)
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('static/'))
PORT = os.getenv("PORT", 5000)

create_socket_routes(socket)

app.add_routes(routes)

if __name__ == "__main__":
    web.run_app(app, port=PORT)
