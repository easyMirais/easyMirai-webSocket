import os

from easyMirais.utils.function import File

defaultConfig = {
    "botURI_value": "127.0.0.1:8080",
    "botID_value": 0,
    "botKey_value": "",
    "kit_name": "",
    "echo_value": True,
    "session": ""
}


def _disDir(dir_name: str) -> bool:  # 检测文件夹是否存在
    if os.path.exists(dir_name):
        return True
    else:
        os.makedirs("./" + dir_name)  # 如果不存在则创建
        return False


def _disFile(file_name: str) -> bool:  # 检测文件是否存在
    if os.path.exists("./config/" + file_name + "/config.json"):
        return True
    else:
        File("./config/" + file_name).write("/config.json", defaultConfig)
        return False


def listPlugins() -> list[str]:
    pluginFile = []  # 存储插件函数

    _disDir("plugins")
    _disDir("config")

    for pluginName in os.listdir("./plugins/"):
        if not pluginName.startswith("_") and os.path.isdir("./plugins/" + str(pluginName)):
            _disDir("config/" + str(pluginName))
            _disFile(pluginName)

            pluginFile.append(str(pluginName))

    return pluginFile
