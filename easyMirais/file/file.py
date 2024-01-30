import json, os

defaultConfig = {
    "botURI_value": "127.0.0.1:8080",
    "botID_value": 0,
    "botKey_value": "",
    "kit_name": "",
    "echo_value": True,
    "session": "",
}


class File:
    def __init__(self, file_path):
        self.file_path = file_path

    def write(self, file_name: str, data: dict):
        data = json.dumps(data)
        with open(self.file_path + file_name, "w") as file:
            file.write(data)
            file.close()

    def read(self, file_name: str) -> dict:
        with open(self.file_path + file_name, "r") as file:
            data = file.read()
            file.close()
            return json.loads(data)

    def edit(self, file_name: str, key: str, value):
        data = self.read(file_name=file_name)
        data[key] = value
        self.write(file_name=file_name, data=data)


def disDir(dir_name: str) -> bool:  # 检测文件夹是否存在
    if os.path.exists(dir_name):
        return True
    else:
        os.makedirs("./" + dir_name)  # 如果不存在则创建
        return False


def disFile(file_name: str) -> bool:  # 检测文件是否存在
    if os.path.exists("./config/" + file_name + "/config.json"):
        return True
    else:
        File("./config/" + file_name).write("/config.json", defaultConfig)
        return False
