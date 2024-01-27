from rich.console import Console

from easyMirais.message.target import Message

from easyMirais.utils.function import Logger
from easyMirais.utils.function import File


class ServerConfig:
    def __init__(self, file_name: str):
        self.botKey_value = ""
        self.botSession_value = ""
        self.botURI_value = ""
        self.file = File("./config/" + file_name)
        self.Logger = Console()


class ConfigType(ServerConfig):
    def setURI(self, bot_uri: str = "ws://127.0.0.1:8080"):
        self.file.edit("/config.json", "botURI_value", bot_uri + "/all")

    def setID(self, bot_id: int) -> None:
        self.file.edit("/config.json", "botID_value", bot_id)

    def setKey(self, bot_key: str) -> None:
        self.file.edit("/config.json", "botKey_value", bot_key)

    def echoLog(self, is_echo: bool = True) -> None:
        self.file.edit("/config.json", "echo_value", is_echo)


class Type(ConfigType):
    @property
    def session(self) -> str:
        return "123"

    @property
    def botID(self) -> int:
        return self.file.read("/config.json")["botID_value"]

    @property
    def botURI(self) -> str:
        return self.botURI_value

    @property
    def log(self):
        return Logger(self.Logger, self.file.read("/config.json"))


class Plugins(Type):

    @property
    def send(self) -> Message:
        return Message(kit_config=self.file.read("/config.json"))

    def get(self):
        pass

    def set(self):
        print("set function")

    def other(self):
        print("other option")
