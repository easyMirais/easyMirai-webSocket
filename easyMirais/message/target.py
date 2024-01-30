from easyMirais.message.type import FriendMessageType, GroupMessageType


class MessageTarget:
    def __init__(self, kit_config: dict, ws):
        self.kit_config = kit_config
        self.ws = ws
        pass

    def friend(self, target: int) -> FriendMessageType:
        return FriendMessageType(
            send_target=target, kit_config=self.kit_config, ws=self.ws
        )

    def group(self, target: int) -> GroupMessageType:
        return GroupMessageType(send_target=target)

    def temp(self):
        pass
