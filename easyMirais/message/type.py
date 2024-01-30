import time

from easyMirais.logger.logger import Logger
from easyMirais.template.template import commandBody
from websocket import WebSocketApp


class FriendMessageType:
    def __init__(self, send_target, kit_config, ws: WebSocketApp):
        self.send_target = send_target
        self.kit_config = kit_config
        self.log = Logger(kit_config)
        self.ws = ws

    def plain(self, text):
        context = {
            "sessionKey": self.kit_config["session"],
            "target": self.send_target,
            "messageChain": [
                {"type": "Plain", "text": text},
            ],
        }

        self.ws.send(
            commandBody(
                syncId="sendFriendMessagePlain",
                command="sendFriendMessage",
                content=context,
            )
        )
        self.log.info(text, "->", self.send_target, "正常", "(Plain / Friend)")

    def image(self):
        pass

    def face(self):
        pass

    @property
    def poke(self):
        pass

    def dice(self):
        pass


class GroupMessageType:
    def __init__(self, send_target):
        self.send_target = send_target

    def plain(self):
        pass

    def at(self):
        pass

    def ats(self):
        pass

    @property
    def atAll(self):
        pass

    def plain(self):
        pass

    def image(self):
        pass

    def face(self):
        pass

    def poke(self):
        pass

    def dice(self):
        pass
