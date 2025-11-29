from abc import ABC, abstractmethod
from discord import Message
from itertools import chain
from typing import Literal

from .reaction import VersecbotReaction
from .settings import WatcherSettings, PollerSettings
from .version import INTERFACE_VERSION


WatcherType = Literal["message"] | Literal["reaction"]


class Job(ABC):
    name: str
    interface_version: INTERFACE_VERSION

    @abstractmethod
    def initialize(self, *args, **kwargs):
        """This method is called when the bot is starting up. Use this to set up any necessary state."""


class MessageWatcher(Job):
    watcher_type: WatcherType = "message"

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


class Watcher(MessageWatcher):
    """Just an alias for MessageWatcher for backward compatibility."""


class ReactionWatcher(Job):
    watcher_type: WatcherType = "reaction"

    def __init__(self, settings: WatcherSettings, **kwargs):
        self.enabled = settings.enabled
        self.channel_ids = settings.channel_ids

    @abstractmethod
    def should_act(
        self,
        reaction: VersecbotReaction,
    ) -> bool:
        if not self.enabled:
            return False

        if self.channel_ids and reaction.message.channel.id not in self.channel_ids:
            return False

        return True

    @abstractmethod
    def act(self, reaction: VersecbotReaction):
        if not self.should_act(reaction):
            return


class Poller(Job):
    def __init__(self, settings: PollerSettings, **kwargs):
        self.enabled = settings.enabled
        self.frequency_seconds = settings.frequency_seconds

    @abstractmethod
    def poll(self):
        if not self.enabled:
            return

    def start(self):
        """Start the polling loop."""
        import threading
        import time

        def poll_loop():
            while self.enabled:
                self.poll()
                time.sleep(self.frequency_seconds)

        self.thread = threading.Thread(target=poll_loop, daemon=True)
        self.thread.start()

    def stop(self):
        """Stop the polling loop."""
        self.enabled = False
        try:
            self.thread.join()
        except AttributeError:
            print("Poller thread was not started; nothing to stop.")


class WatcherRegistry:
    message: dict[str, MessageWatcher]
    reaction: dict[str, ReactionWatcher]

    def __init__(self):
        self.message = {}
        self.reaction = {}


class JobRegistry:
    interface_version: INTERFACE_VERSION
    watchers: WatcherRegistry
    pollers: dict[str, Poller]

    def __init__(self):
        self.watchers = WatcherRegistry()
        self.pollers = {}

    def register(self, job: Job):
        if isinstance(job, MessageWatcher):
            if job.name in self.watchers.message:
                raise ValueError(
                    f"Message watcher with name {job.name} is already registered."
                )

            self.watchers.message[job.name] = job

        elif isinstance(job, ReactionWatcher):
            if job.name in self.watchers.reaction:
                raise ValueError(
                    f"Reaction watcher with name {job.name} is already registered."
                )

            self.watchers.reaction[job.name] = job

        elif isinstance(job, Poller):
            if job.name in self.pollers:
                raise ValueError(f"Poller with name {job.name} is already registered.")

            self.pollers[job.name] = job

    def initialize_all(self):
        for job in chain(
            list(self.watchers.message.values()),
            list(self.watchers.reaction.values()),
            list(self.pollers.values()),
        ):
            job.initialize()
