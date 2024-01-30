import os

from easyMirais.file.file import disFile, disDir


def listPlugins() -> list[str]:
    pluginFile = []  # 存储插件函数

    disDir("plugins")
    disDir("config")

    for pluginName in os.listdir("./plugins/"):
        if not pluginName.startswith("_") and os.path.isdir(
            "./plugins/" + str(pluginName)
        ):
            disDir("config/" + str(pluginName))
            disFile(pluginName)

            pluginFile.append(str(pluginName))

    return pluginFile
