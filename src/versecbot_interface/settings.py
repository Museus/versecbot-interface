from pydantic import BaseModel, Field
from pydantic_settings import SettingsConfigDict


class PluginSettings(BaseModel):
    model_config = SettingsConfigDict(extra="allow")
    enabled: bool


class JobSettings(BaseModel):
    model_config = SettingsConfigDict(extra="allow")
    enabled: bool


class WatcherSettings(JobSettings):
    channel_ids: list[int] | None = Field(
        default=None,
        description="List of channel IDs to watch. If None, all channels are watched.",
    )
