#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author    : SFNCO-Studio
# @Time      : 2023/5/24 20:31
# @File      : main.py
# @Project   : easyMirai-webSocket
# @Uri       : https://sfnco.com.cn/


import websocket


class Mirai:
    def __init__(self, uri: str, port: int, verifyKey: str, qq: int):
        self.uri = uri + ":" + str(port)
        self.verifyKey = verifyKey
        self.qq = qq
        pass

    def onOpen(self):
        pass

    def onMessage(self, message):
        pass

    def onClose(self):
        pass

    def start(self):
        ws = websocket.WebSocketApp(
            "ws://" + self.uri + "/all?verifyKey=" + self.verifyKey + "&qq=" + str(self.qq),
            on_open=self.onOpen,
            on_message=self.onMessage,
            on_close=self.onClose)
        ws.run_forever()


if __name__ == '__main__':
    Mirai(uri="127.0.0.1", port=8080, verifyKey="1234567890", qq=1234567890).start()
