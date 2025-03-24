from abc import ABC
from typing import Type, Literal

from .settings import PluginSettings


class Plugin(ABC):
    name: str
    settings: Type[PluginSettings]
    interface_version: Literal["0.1"]

    def __init_subclass__(cls):
        super().__init_subclass__()
        registry.register(cls)

    def initialize(self, *args, **kwargs):
        """This method is called when the bot is starting up. Use this to set up any necessary state."""


class PluginRegistry:
    interface_version: Literal["0.1"]

    def __init__(self):
        self.plugins: dict[str, Plugin] = {}

    def register(self, plugin: Plugin):
        self.plugins[plugin.name] = plugin()


registry = PluginRegistry()
