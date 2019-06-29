#!/usr/bin/python

from flask import request
from flask import Flask
from flask_api import FlaskAPI
from fancodes import *
import os

AUTH_CODE = os.getenv("AUTH_CODE")

app = FlaskAPI(__name__)

# Handles simple cases where 'the' is added
def map_fan_name(fan_name):
    if 'dining room' in fan_name:
        return 'dn'
    elif 'living room' in fan_name:
        return 'lv'
    elif '3' in fan_name or 'three' in fan_name:
        return 'br3'
    elif '2' in fan_name or 'two' in fan_name:
        return 'br2'
    elif 'all' in fan_name:
        return 'all'

def transmit_all(command_code):
    for fan_code in fan_ids.values():
        transmit_code(fan_code + command_code)
        time.sleep(0.4)

@app.route('/fan/', methods=["GET", "POST"])
def api_fan_control():
    if request.method == "POST" and request.data.get("auth") == AUTH_CODE:
        fan = map_fan_name(request.data.get("fan"))
        print(fan)
        command_code = commands[request.data.get("command").strip()]
        if fan == 'all':
            transmit_all(command_code)
            return {'code': 'all'}
        code = fan_ids[fan] + command_code
        if request.data.get("count"):
            count = int(request.data.get("count")) - 1
            for _ in range(count):
                transmit_code(code)
                time.sleep(1)
        transmit_code(code)
        return {'code': code}
    return {}

if __name__ == "__main__":
    app.run()
