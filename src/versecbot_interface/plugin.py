from abc import ABC
from discord import Intents
from typing import Type

from .jobs import Job, JobRegistry, Watcher
from .version import INTERFACE_VERSION


class Plugin(ABC):
    name: str
    jobs: JobRegistry
    intents: list[Intents]
    interface_version: INTERFACE_VERSION

    def __init__(self):
        self.jobs = JobRegistry()

    def __init_subclass__(cls):
        super().__init_subclass__()

    def assign_job(self, job: Type[Job]):
        """Assign a job to this plugin."""
        if not isinstance(job, Job):
            raise TypeError(f"{job} is not a subclass of Job")

        self.jobs.register(job)

    def get_watchers(self) -> list[Type[Watcher]]:
        """Get all message watchers assigned to this plugin."""
        print(
            DeprecationWarning(
                "get_watchers is deprecated, use get_message_watchers instead."
            )
        )
        return [watcher for watcher in self.jobs.watchers.message.values()]

    def get_message_watchers(self) -> list[Type[Watcher]]:
        """Get all message watchers assigned to this plugin."""
        return [watcher for watcher in self.jobs.watchers.message.values()]

    def get_reaction_watchers(self) -> list[Type[Watcher]]:
        """Get all reaction watchers assigned to this plugin."""
        return [watcher for watcher in self.jobs.watchers.reaction.values()]

    def get_pollers(self) -> list[Type[Watcher]]:
        """Get all watchers assigned to this plugin."""
        return [watcher for watcher in self.jobs.watchers.values()]

    def initialize(self, *args, **kwargs):
        """This method is called when the bot is starting up. Use this to set up any necessary state."""
        self.jobs.initialize_all()


class PluginRegistry:
    plugins: dict[str, Plugin]

    def __init__(self):
        self.plugins: dict[str, Plugin] = {}

    def register(self, plugin: Plugin):
        self.plugins[plugin.name] = plugin()
