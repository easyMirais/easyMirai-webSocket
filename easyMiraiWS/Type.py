class MessageType:  # 信息类型
    def plan(self, message: str):
        return "plan"


class TargetType:  # 目标类型

    def friend(self, target: int):
        return "friend"


class ReturnType:  # 返回类型
    @property
    def Dict(self):
        return "dict"

    @property
    def json(self):
        return "json"
