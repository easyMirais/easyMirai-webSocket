from websocket import WebSocketApp

from easyMirais.message.target import MessageTarget

from easyMirais.logger.logger import Logger
from easyMirais.file.file import File


class ServerConfig:
    def __init__(self, file_name: str):
        self._botKey_value = ""
        self._botSession_value = ""
        self._botURI_value = ""
        self._file = File("./config/" + file_name)

    @property
    def log(self):
        return Logger(self._file.read("/config.json"))


class Init(ServerConfig):
    def setURI(self, bot_uri: str = "ws://127.0.0.1:8080"):
        self._file.edit("/config.json", "botURI_value", bot_uri)

    def setID(self, bot_id: int = 0) -> None:
        self._file.edit("/config.json", "botID_value", bot_id)

    def setKey(self, bot_key: str = "") -> None:
        self._file.edit("/config.json", "botKey_value", bot_key)

    def echoLog(self, is_echo: bool = True) -> None:
        self._file.edit("/config.json", "echo_value", is_echo)

    @property
    def botID(self) -> int:
        return self._file.read("/config.json")["botID_value"]

    @property
    def botURI(self) -> str:
        return self._botURI_value


class Plugins(Init):
    @property
    def session(self) -> str:
        return self._file.read("/config.json")["session"]

    def get(self):
        pass

    def set(self):
        print("set function")

    def other(self):
        print("other option")


class Message(Plugins):
    def __init__(self, file_name: str, ws: WebSocketApp, message):
        super().__init__(file_name)
        self.ws = ws
        self.message = message

    @property
    def send(self) -> MessageTarget:
        return MessageTarget(kit_config=self._file.read("/config.json"), ws=self.ws)

    pass


class Open(Plugins):
    def __init__(self, file_name: str, ws: WebSocketApp):
        super().__init__(file_name)
        self.ws = ws

    pass


class ReCall(Plugins):
    def __init__(self, file_name: str, ws: WebSocketApp, message):
        super().__init__(file_name)
        self.ws = ws
        self.message = message

    pass
