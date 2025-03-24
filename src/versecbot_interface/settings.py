from pydantic import BaseModel
from pydantic_settings import SettingsConfigDict

from .version import INTERFACE_VERSION


class PluginSettings(BaseModel):
    interface_version: INTERFACE_VERSION

    model_config = SettingsConfigDict(extra="allow")
    enabled: bool


class WatcherSettings(PluginSettings):
    interface_version: INTERFACE_VERSION

    enabled: bool
    channel_id: int | None
