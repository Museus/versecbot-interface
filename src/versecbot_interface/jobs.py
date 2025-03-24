from abc import ABC, abstractmethod
from discord import Message

from .settings import WatcherSettings
from .version import INTERFACE_VERSION


class Watcher(ABC):
    enabled: bool
    channel_id: int
    interface_version: INTERFACE_VERSION

    def __init__(self, settings: WatcherSettings, **kwargs):
        self.enabled = settings.enabled
        self.channel_id = settings.channel_id

    @abstractmethod
    def should_act(self, message: Message) -> bool:
        if not self.enabled:
            return False

        if self.channel_id and message.channel.id != self.channel_id:
            return False

        return True

    @abstractmethod
    def act(self, message: Message):
        if not self.should_act(message):
            return
