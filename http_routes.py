from globals.globals import *
import aiohttp_jinja2
from globals.functions import *

routes = web.RouteTableDef()
routes.static('/static', "static/")


@routes.route("*", "/admin")
@aiohttp_jinja2.template("admin.jinja2")
async def handle_admin(request: web.Request):
    user_id = get_user_id(request)
    if user_id not in cache:
        cache[user_id] = {
            "is_admin": False
        }
    if cache[user_id]["is_admin"]:
        raise web.HTTPFound('/home')
    return {
        "title": "Admin",
        "filename": "aAdmin"
    }


@routes.route("POST", "/admin_auth")
async def auth(request: web.Request):
    user_id = get_user_id(request)
    if user_id in cache:
        if cache[user_id]["is_admin"]:
            return web.json_response({"ok": True, "message": "Your are logged in"})
        data = await request.json()
        if data["login"] == sample_admin["login"] and\
                data["password"] == sample_admin["password"]:
            cache[user_id]["is_admin"] = True
            return web.json_response({"ok": True, "message": "Your are logged in"})
    return web.json_response({"ok": False, "message": "Login or password is invalid"})


@routes.route('*', "/events")
@aiohttp_jinja2.template("events.jinja2")
async def events(request: web.Request):
    return {
        "title": "Events",
        "filename": "events",
        "additional": ["grid"]
    }


@routes.route('*', "/help_requests")
@aiohttp_jinja2.template("help_requests.jinja2")
async def help_requests(request: web.Request):
    return {
        "title": "Help requests",
        "filename": "help_requests",
        "additional": ["grid"]
    }


@routes.route('*', "/insert")
@aiohttp_jinja2.template("insert.jinja2")
async def insert(request: web.Request):
    return {
        "title": "Insert",
        "filename": "insert",
        "additional": ["form"]
    }


@routes.route('*', "/settings")
@aiohttp_jinja2.template("settings.jinja2")
async def settings(request: web.Request):
    return {
        "title": "Settings",
        "filename": "settings",
        "additional": ["form"]
    }


@routes.route('*', "/statistics")
@aiohttp_jinja2.template("statistics.jinja2")
async def statistics(request: web.Request):
    return {
        "title": "Statistics",
        "filename": "statistics"
    }


@routes.route('*', "/logout")
async def logout(request: web.Request):
    user_id = get_user_id(request)
    cache[user_id] = {
        "is_admin": False
    }
    return web.HTTPFound("/admin")


@routes.route("*", "/")
async def other(request):
    raise web.HTTPFound('/admin')

