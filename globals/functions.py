import json
import datetime


def open_json(fp):
    with open(fp, encoding="UTF8") as f:
        return json.load(f)


def get_now_msw():
    return datetime.datetime.utcnow() + datetime.timedelta(hours=3)


def text_message(text, author):
    return {
        "user_id": author,
        "type": "text",
        "message": {
            "content": text
        }
    }


def text_message_with_keyboard(text, keyboard_buttons, author):
    return {
        "user_id": author,
        "type": "keyboard",
        "message": {
            "content": text,
            "keyboard_buttons": keyboard_buttons
        }
    }


def reshape(lst, width=5):
    return [lst[d:d + width] for d in range(0, len(lst), width)]
