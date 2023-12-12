import asyncio

from easyMiraiWS.Mirais import Mirai
from easyMiraiWS.Type import MessageType, TargetType, ReturnType

targetType: TargetType = TargetType()  # 定义发送目标类型
messageType: MessageType = MessageType()  # 定义消息类型
returnType: ReturnType = ReturnType()  # 返回值类型


def run(func):  # 启动服务
    asyncio.get_event_loop().run_until_complete(func())


def sleep(delay: int):  # 延时
    asyncio.sleep(delay)
