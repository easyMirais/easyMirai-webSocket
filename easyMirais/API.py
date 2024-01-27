from rich.console import Console

from easyMirais.message.target import Message

from easyMirais.utils.function import Logger
from easyMirais.utils.function import File


class ServerConfig:
    def __init__(self, file_name: str):
        self._botKey_value = ""
        self._botSession_value = ""
        self._botURI_value = ""
        self._file = File("./config/" + file_name)
        self._Logger = Console()


class ConfigType(ServerConfig):
    def setURI(self, bot_uri: str = "ws://127.0.0.1:8080"):
        self._file.edit("/config.json", "botURI_value", bot_uri)

    def setID(self, bot_id: int = 0) -> None:
        self._file.edit("/config.json", "botID_value", bot_id)

    def setKey(self, bot_key: str = "") -> None:
        self._file.edit("/config.json", "botKey_value", bot_key)

    def echoLog(self, is_echo: bool = True) -> None:
        self._file.edit("/config.json", "echo_value", is_echo)


class Type(ConfigType):
    @property
    def session(self) -> str:
        return self._file.read("/config.json")["session"]

    @property
    def botID(self) -> int:
        return self._file.read("/config.json")["botID_value"]

    @property
    def botURI(self) -> str:
        return self._botURI_value

    @property
    def log(self):
        return Logger(self._Logger, self._file.read("/config.json"))


class Plugins(Type):

    @property
    def send(self) -> Message:
        return Message(kit_config=self._file.read("/config.json"))

    def get(self):
        pass

    def set(self):
        print("set function")

    def other(self):
        print("other option")
