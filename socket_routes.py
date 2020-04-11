import socketio
from globals.globals import *


def create_socket_routes(socket: socketio.AsyncServer):
    @socket.event
    async def connect(sid, environ):
        host = environ['REMOTE_ADDR']
        print(host, cache)
        if host in cache:
            cache[host]["sid"] = sid
            print(f"connection established with {sid} {host}")
        else:
            await socket.disconnect(sid)

    @socket.event
    def disconnect(sid):
        print(f"{sid} disconnected")

    @socket.event
    async def update(sid):
        print("update", sid)
        await change(sid, {})

    @socket.event
    async def change(sid, data):
        if not data:
            await socket.emit("change", data={
                "help_requests": db.get_all_help_requests(),
                "events": db.get_events()
            }, room=sid)
        if "add" in data:
            event = data["add"]
            db.insert_event(event['name'], event['description'])
            for i in cache:
                sid = cache[i]["sid"]
                try:
                    await update(sid)
                except:
                    pass
