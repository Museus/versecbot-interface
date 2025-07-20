from abc import ABC, abstractmethod
from discord import Message

from .settings import WatcherSettings
from .version import INTERFACE_VERSION


class Job(ABC):
    name: str
    interface_version: INTERFACE_VERSION

    @abstractmethod
    def initialize(self, *args, **kwargs):
        """This method is called when the bot is starting up. Use this to set up any necessary state."""


class Watcher(Job):
    def __init__(self, settings: WatcherSettings, **kwargs):
        self.enabled = settings.enabled
        self.channel_ids = settings.channel_ids

    @abstractmethod
    def should_act(self, message: Message) -> bool:
        if not self.enabled:
            return False

        if self.channel_ids and message.channel.id not in self.channel_ids:
            return False

        return True

    @abstractmethod
    def act(self, message: Message):
        if not self.should_act(message):
            return


class JobRegistry:
    interface_version: INTERFACE_VERSION
    watchers: dict[str, Watcher]

    def __init__(self):
        self.watchers = {}

    def register(self, job: Job):
        if issubclass(job, Watcher):
            if job.name in self.watchers:
                raise ValueError(f"Watcher with name {job.name} is already registered.")

            self.watchers[job.name] = job

    def initialize_all(self):
        for job in self.jobs.values():
            job.initialize()
