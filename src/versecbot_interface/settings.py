from pydantic import BaseModel
from pydantic_settings import SettingsConfigDict


class PluginSettings(BaseModel):
    model_config = SettingsConfigDict(extra="allow")
    enabled: bool


class JobSettings(BaseModel):
    model_config = SettingsConfigDict(extra="allow")
    enabled: bool


class WatcherSettings(JobSettings):
    channel_ids: list[int] | None
