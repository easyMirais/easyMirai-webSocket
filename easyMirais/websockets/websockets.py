import json

from concurrent.futures import ThreadPoolExecutor

from websocket import WebSocketApp

from easyMirais.API import Open, Message, ReCall
from easyMirais.file.file import File


class WebSocketFunction:
    def __init__(self, kit_name: str, func):
        self.kit_name = kit_name
        self.func = func

    def o_open(self, ws):
        self.func.open(Open(self.kit_name, ws))
        pass

    def o_message(self, ws, message):
        message = json.loads(message)
        if any("session" in d for d in message["data"]):
            if message["code"] == 0:
                File("./config/" + self.kit_name).edit("/config.json", "session", message["session"])
        else:
            if any("syncId" in d for d in message):
                if message["syncId"] == "-1":
                    self.func.message(Message(self.kit_name, ws, message["data"]))
                else:
                    self.func.recall(ReCall(self.kit_name, ws, message["data"]))
            else:
                self.func.recall(ReCall(self.kit_name, ws, message["data"]))

    def o_close(self, ws, close_status_code, close_msg):
        pass


def start_websocket_server(addr, bot_key, bot_id, kit_name, function):
    WebSocketApp("ws://" + addr + "/all?verifyKey=" + bot_key + "&qq=" + str(bot_id),
                 on_open=WebSocketFunction(kit_name, function).o_open,
                 on_message=WebSocketFunction(kit_name, function).o_message
                 ).run_forever()


def getSession(pool_object: ThreadPoolExecutor, addr, bot_id, bot_key, kit_name, function):
    # websocket.enableTrace(True)
    pool_object.submit(start_websocket_server, addr, bot_key, bot_id, kit_name, function)
