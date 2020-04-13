from globals.globals import *
import aiohttp_jinja2
from globals.functions import *

routes = web.RouteTableDef()
routes.static('/static', "static/")
sample_admin = {
    "login": "admin",
    "password": "admin"
}


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


@routes.route('*', "/home")
@aiohttp_jinja2.template("home.jinja2")
async def home(request: web.Request):
    pass


@routes.route('*', "/insert")
@aiohttp_jinja2.template("insert.jinja2")
async def insert(request: web.Request):
    pass


@routes.route('*', "/settings")
@aiohttp_jinja2.template("settings.jinja2")
async def settings(request: web.Request):
    pass


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

