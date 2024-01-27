import importlib
from concurrent.futures import ThreadPoolExecutor

from rich.console import Console
import websocket

from easyMirais.utils.loadPlugins import listPlugins
from easyMirais.API import Plugins
from easyMirais.utils.function import File, Logger, getSession, startKitWebsocket


class Init:
    def __init__(self):
        self.pluginFile = []  # 存储插件文件名称
        self.pluginFunction = []  # 存储插件函数
        self.pluginStatus = []  # 存储插件状态
        self.Plugins = Plugins
        self.echo_server_log = True
        self.pool = ThreadPoolExecutor(16)
        self.logger = Logger(Console(), {"kit_name": "Server", "echo_value": self.echo_server_log})


class Mirai(Init):
    @property
    def getPluginFunction(self):
        return self.pluginFunction

    @property
    def getPluginFile(self):
        return self.pluginFile

    def _start_load_plugins(self):
        for index, loadPluginsFile in enumerate(self._loadPlugins()):
            try:
                loadPluginsFile.init(self.Plugins(self.pluginFile[index]))
            except TypeError:
                loadPluginsFile.init()
            except AttributeError:
                self.logger.warning(
                    "插件包", self.pluginFile[index], "未发现 init 函数",
                )
            except ModuleNotFoundError:
                self.logger.warning(
                    "插件包", self.pluginFile[index], "未发现 kit.py 文件",
                )
                break
            File("./config/" + self.pluginFile[index]).edit("/config.json", "kit_name", self.pluginFile[index])
            kit_config = File("./config/" + self.pluginFile[index]).read("/config.json")
            getSession(self.pool, kit_config["botURI_value"], kit_config["botID_value"], kit_config["botKey_value"],
                       kit_config["kit_name"]).result()
            self.logger.info(
                "插件包名:",
                kit_config["kit_name"],
                "QQ:",
                kit_config["botID_value"],
                "是否输出日志:",
                kit_config["echo_value"],
            )

            # try:
            #     function_list["message"] = loadPluginsFile.message(self.Plugins(self.pluginFile[index]))
            # except TypeError:
            #     self.Logger.warning(
            #         "插件包", self.pluginFile[index], "message 函数未发现正确输入参数", "*:Message"
            #     )
            # except AttributeError:
            #     self.Logger.warning(
            #         "插件包", self.pluginFile[index], "未发现 message 函数",
            #     )
            startKitWebsocket(loadPluginsFile, self.logger)

    def _loadPlugins(self):
        self.pluginFile = listPlugins()
        for pluginName in self.pluginFile:
            try:
                self.pluginFunction.append(importlib.import_module("plugins." + pluginName + ".kit"))
            except ModuleNotFoundError:
                self.logger.error(
                    "插件目录 plugins", "未发现有效 kit.py 文件",
                )

        return self.pluginFunction

    def startServer(self, echo_server_log=True):
        self.echo_server_log = echo_server_log
        return self._start_load_plugins()
