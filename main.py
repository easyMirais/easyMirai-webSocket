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
        self.ws = None

    def onOpen(self):
        # 连接成功Mirai服务器时调用
        pass

    def onMessage(self, message):
        # 接收到消息时调用
        pass

    def onClose(self):
        # 关闭连接时调用
        pass

    def start(self):
        self.ws = websocket.WebSocketApp(
            "ws://" + self.uri + "/all?verifyKey=" + self.verifyKey + "&qq=" + str(self.qq),
            on_open=self.onOpen,
            on_message=self.onMessage,
            on_close=self.onClose)
        self.ws.run_forever()


if __name__ == '__main__':
    Mirai(uri="127.0.0.1", port=8080, verifyKey="1234567890", qq=1234567890).start()
