import importlib
from concurrent.futures import ThreadPoolExecutor
import time

from rich.console import Console

from easyMirais.utils.loadPlugins import listPlugins
from easyMirais.API import Plugins
from easyMirais.utils.function import File, getSession
from easyMirais.utils.function import Logger


class Init:
    def __init__(self):
        self.pluginFile = []  # 存储插件文件名称
        self.pluginFunction = []  # 存储插件函数
        self.pluginStatus = []  # 存储插件状态
        self.Plugins = Plugins
        self.echo_server_log = True
        self.pool = ThreadPoolExecutor(16)
        self.Logger = Logger(Console(), {"kit_name": "Server", "echo_value": self.echo_server_log})


class Mirai(Init):
    @property
    def getPluginFunction(self):
        return self.pluginFunction

    @property
    def getPluginFile(self):
        return self.pluginFile

    def _start_load_plugins(self):
        for index, loadPluginsFile in enumerate(self._loadPlugins()):
            kit_config = File("./config/" + self.pluginFile[index]).read("/config.json")
            getSession(self.pool, kit_config["botURI_value"], kit_config["botID_value"], kit_config["botKey_value"],
                       kit_config["kit_name"]).result()
            try:
                loadPluginsFile.init(self.Plugins(self.pluginFile[index]))
            except TypeError:
                loadPluginsFile.init()
            except AttributeError:
                self.Logger.warning(
                    "插件包", self.pluginFile[index], "未发现 init 函数",
                )
            except ModuleNotFoundError:
                self.Logger.warning(
                    "插件包", self.pluginFile[index], "未发现 kit.py 文件",
                )
            File("./config/" + self.pluginFile[index]).edit("/config.json", "kit_name", self.pluginFile[index])
            kit_config = File("./config/" + self.pluginFile[index]).read("/config.json")
            self.Logger.info(
                "插件包名:",
                kit_config["kit_name"],
                "QQ:",
                kit_config["botID_value"],
                "是否输出日志:",
                kit_config["echo_value"],
            )

    def _loadPlugins(self):
        self.pluginFile = listPlugins()
        for pluginName in self.pluginFile:
            self.pluginFunction.append(importlib.import_module("plugins." + pluginName + ".kit"))
        return self.pluginFunction

    def _readPluginsFile(self):
        pass

    def startServer(self, echo_server_log=True):
        self.echo_server_log = echo_server_log
        return self._start_load_plugins()
