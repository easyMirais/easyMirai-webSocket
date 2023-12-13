#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author    : SFNCO-Studio
# @Time      : 2023/5/24 20:31
# @File      : main.py
# @Project   : easyMirai-webSocket
# @Uri       : https://sfnco.com.cn/
import easyMiraiWS
from easyMiraiWS import Mirai
from easyMiraiWS import targetType, messageType, returnType


async def MiraiRun():  # 运行主类
    easy_mirai = Mirai(uri="localhost", port=8080, verifyKey="123456789", qq=123456789)
    # 向好友987654321发送文字消息hello world并返回一个Dict类型的值
    message = await easy_mirai.send(targetType.Friend(987654321), messageType.Plain("Hello World"), returnType.Dict)
    print(message)
    pass


if __name__ == '__main__':
    easyMiraiWS.run(MiraiRun)
