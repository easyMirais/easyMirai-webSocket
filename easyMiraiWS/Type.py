class MessageType:  # 信息类型
    @property
    def plan(self):
        return "plan"


class TargetType:  # 目标类型
    @property
    def friend(self):
        return "friend"


class ReturnType:  # 返回类型
    @property
    def Dict(self):
        return "dict"

    @property
    def json(self):
        return "json"
