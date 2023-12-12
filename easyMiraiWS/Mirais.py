import json

import websockets
from easyMiraiWS.Type import MessageType, TargetType, ReturnType


# from easyMiraiWS.sendFunction.type import SendTypeFunction

class SendTypeFunction:
    def __init__(self, session: str):
        self.session = session

    async def friend(self, target: int):  # 向好友发送消息
        return "123"


class Mirai:
    def __init__(self, uri: str, port: int, verifyKey: str, qq: int):
        self._uri = "ws://" + uri + ":" + str(port) + "/"
        self._verifyKey = verifyKey
        self._qq = str(qq)
        self.syncId = ""
        self._session = ""
        self._botStart = False  # 机器人是否初始化、

    def _deCodeJson(self, payload: str) -> dict:
        # 解析JSON函数
        return json.loads(payload)

    def _ws(self, addr: str) -> websockets.connect:  # 创建连接函数
        return websockets.connect(self._uri + addr)  # 创建ws连接

    async def _detectBotStatus(self):  # 检测机器人初始化状态
        if not self._botStart:  # 如果没有进行初始化
            await self._start()  # 进行机器人初始化

    async def _request(self, addr: str, payload: str = "") -> dict:  # 请求函数
        async with self._ws(addr) as websocket:
            await websocket.send(payload)  # 发送请求体
            response = await websocket.recv()  # 取得响应体
            await websocket.close()  # 关闭连接
            response = self._deCodeJson(response)
        return response

    async def _start(self):  # 初始化机器人
        # 注册session
        payload = await self._request("/all?verifyKey=" + self._verifyKey + "&qq=" + self._qq)
        print(payload)  # 解析Json

    async def send(self, Target: TargetType, Message: MessageType, Payload: str,
                   Return: ReturnType = "None") -> SendTypeFunction:  # 发送函数集
        await self._detectBotStatus()  # 检测机器人是否被初始化
        return SendTypeFunction(session=self._session)
