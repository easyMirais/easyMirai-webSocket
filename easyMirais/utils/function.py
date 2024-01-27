import json
import os
from concurrent.futures import ThreadPoolExecutor

import websocket

from easyMirais.utils.loggerColor import DEBUG, INFO, WARNING, ERROR


class Logger:
    def __init__(self, logger, kitConfig: dict):
        self.Logger = logger
        self.kitConfig = kitConfig

    def debug(self, *obj):
        if self.kitConfig["echo_value"]:
            self.Logger.log("[ DEBUG", "/", self.kitConfig["kit_name"], "]:", *obj, style=DEBUG())

    def info(self, *obj):
        if self.kitConfig["echo_value"]:
            self.Logger.log("[ INFO", "/", self.kitConfig["kit_name"], "]:", *obj, style=INFO())

    def warning(self, *obj):
        if self.kitConfig["echo_value"]:
            self.Logger.log("[ WARNING", "/", self.kitConfig["kit_name"], "]:", *obj, style=WARNING())


def commandData(syncId: str = "", command: str = "", content: dict = None) -> str:
    return json.dumps(
        {
            "syncId": syncId,
            "command": command,
            "content": {
                content
            }
        }
    )


def getSession(pool_object: ThreadPoolExecutor, addr: str, bot_id: int, bot_key: str, kit_name: str):
    # websocket.enableTrace(True)
    def discoverData(ws, message):
        message = json.loads(message)["data"]
        if message["code"] == 0:
            File("./config/" + kit_name).edit("/config.json", "session", message["session"])
        ws.close()

    get_session = lambda addr_s, bot_keys, bot_ids: (
        websocket.WebSocketApp("ws://" + addr_s + "/all?verifyKey=" + bot_keys + "&qq=" + bot_ids,
                               on_message=discoverData
                               )).run_forever()
    return pool_object.submit(get_session, addr, bot_key, str(bot_id))


class File:
    def __init__(self, file_path):
        self.file_path = file_path

    def write(self, file_name: str, data: dict):
        data = json.dumps(data)
        with open(self.file_path + file_name, "w") as file:
            file.write(data)
            file.close()

    def read(self, file_name: str) -> dict:
        with open(self.file_path + file_name, "r") as file:
            data = file.read()
            file.close()
            return json.loads(data)

    def edit(self, file_name: str, key: str, value):
        data = self.read(file_name=file_name)
        data[key] = value
        self.write(file_name=file_name, data=data)
