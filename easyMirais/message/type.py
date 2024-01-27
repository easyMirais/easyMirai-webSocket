from rich.console import Console

from easyMirais.utils.function import Logger


class FriendMessageType:
    def __init__(self, send_target, kit_config):
        self.send_target = send_target
        self.log = Logger(Console(), kit_config)

    def plain(self, text):
        self.log.info(text, "->", self.send_target, "正常", "(Plain / Friend)")
        print(self.send_target, text)

    def image(self):
        pass

    def face(self):
        pass

    @property
    def poke(self):
        pass

    def dice(self):
        pass


class GroupMessageType:
    def __init__(self, send_target):
        self.send_target = send_target

    def plain(self):
        pass

    def at(self):
        pass

    def ats(self):
        pass

    @property
    def atAll(self):
        pass

    def plain(self):
        pass

    def image(self):
        pass

    def face(self):
        pass

    def poke(self):
        pass

    def dice(self):
        pass
