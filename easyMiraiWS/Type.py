class MessageType:  # 信息类型
    def Plain(self, message: str):
        return "Plain"


class TargetType:  # 目标类型

    def Friend(self, target: int):
        return "Friend"


class ReturnType:  # 返回类型
    @property
    def Dict(self):
        return "Dict"

    @property
    def Json(self):
        return "json"
