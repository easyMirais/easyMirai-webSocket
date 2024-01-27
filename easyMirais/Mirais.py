import importlib
from concurrent.futures import ThreadPoolExecutor
import time

from rich.console import Console
from rich.progress import track
from websocket import WebSocketApp

from easyMirais.utils.loadPlugins import listPlugins
from easyMirais.utils.loggerColor import DEBUG, INFO, WARNING, ERROR
from easyMirais.API import Plugins
from easyMirais.utils.function import File
from easyMirais.utils.function import Logger


class Init:
    def __init__(self):
        self.pluginFile = []  # 存储插件文件名称
        self.pluginFunction = []  # 存储插件函数
        self.pluginStatus = []  # 存储插件状态
        self.Logger = Console()
        self.Plugins = Plugins
        self.echo_server_log = True


class Mirai(Init):
    @property
    def getPluginFunction(self):
        return self.pluginFunction

    @property
    def getPluginFile(self):
        return self.pluginFile

    def _start(self):
        for index, loadPluginsFile in enumerate(self._loadPlugins()):
            try:
                loadPluginsFile.init(self.Plugins(self.pluginFile[index]))
            except TypeError:
                loadPluginsFile.init()
            except AttributeError:
                self.pluginStatus[0] = False
                Logger(self.Logger, {"kit_name": "Server", "echo_value": self.echo_server_log}).warning(
                    "插件", loadPluginsFile, "未发现 init 函数",
                )
            File("./config/" + self.pluginFile[index]).edit("/config.json", "kit_name", self.pluginFile[index])
            kit_config = File("./config/" + self.pluginFile[index]).read("/config.json")
            Logger(self.Logger, {"kit_name": "Server", "echo_value": self.echo_server_log}).info(
                "插件名:",
                kit_config["kit_name"],
                "QQ:",
                kit_config["botID_value"],
                "是否输出日志:",
                kit_config["echo_value"],
            )
            # WebSocketApp(url=)

    def _loadPlugins(self):
        self.pluginFile = listPlugins()
        for pluginName in self.pluginFile:
            self.pluginFunction.append(importlib.import_module("plugins." + pluginName + ".kit"))
        return self.pluginFunction

    def _readPluginsFile(self):
        pass

    def startServer(self, echo_server_log=True):
        self.echo_server_log = echo_server_log
        return self._start()
