from rich.console import Console


def DEBUG():
    return "#8fffa1"


def INFO():
    return "#8fd4ff"


def ERROR():
    return "#ff8f8f"


def WARNING():
    return "#fff18f"


class Logger:
    def __init__(self, kitConfig: dict):
        self.Logger = Console()
        self.kitConfig = kitConfig

    def debug(self, *obj):
        if self.kitConfig["echo_value"]:
            self.Logger.log(
                "[ DEBUG", "/", self.kitConfig["kit_name"], "]:", *obj, style=DEBUG()
            )

    def info(self, *obj):
        if self.kitConfig["echo_value"]:
            self.Logger.log(
                "[ INFO", "/", self.kitConfig["kit_name"], "]:", *obj, style=INFO()
            )

    def warning(self, *obj):
        if self.kitConfig["echo_value"]:
            self.Logger.log(
                "[ WARNING",
                "/",
                self.kitConfig["kit_name"],
                "]:",
                *obj,
                style=WARNING()
            )

    def error(self, *obj):
        if self.kitConfig["echo_value"]:
            self.Logger.log(
                "[ ERROR", "/", self.kitConfig["kit_name"], "]:", *obj, style=ERROR()
            )
