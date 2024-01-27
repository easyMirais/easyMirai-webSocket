from easyMirais.message.type import FriendMessageType, GroupMessageType


class Message:
    def __init__(self, kit_config: dict):
        self.kit_config = kit_config
        pass

    def friend(self, target: int) -> FriendMessageType:
        return FriendMessageType(send_target=target, kit_config=self.kit_config)

    def group(self, target: int) -> GroupMessageType:
        return GroupMessageType(send_target=target)

    def temp(self):
        pass
