import json


def commandBody(syncId: str = "", command: str = "", content: dict = None) -> str:
    return json.dumps({"syncId": syncId, "command": command, "content": content})
