import json
import os

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
