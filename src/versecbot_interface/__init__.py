from .plugin import Plugin, PluginRegistry
from .jobs import Job, JobRegistry, Watcher
from .settings import PluginSettings, JobSettings, WatcherSettings
from .version import INTERFACE_VERSION

__all__ = [
    "Plugin",
    "PluginSettings",
    "PluginRegistry",
    "registry",
    "Job",
    "JobRegistry",
    "JobSettings",
    "Watcher",
    "WatcherSettings",
    "INTERFACE_VERSION",
]

# This module provides the interface for VerseCBot plugins and jobs.
# It includes the base classes for plugins and jobs, as well as the registry
# for managing them. Plugins can define their own settings and jobs, and the
# interface provides a way to initialize and manage these components.
# The interface version is also defined here, which can be used to ensure
# compatibility between different versions of the interface and plugins.
# The `Plugin` class is the base class for all plugins, and it provides a way
# to register jobs and initialize the plugin. The `Job` class is the base class
# for all jobs, and it provides a way to define the behavior of the job.
# The `Watcher` class is a specific type of job that can monitor messages in
# Discord channels and take action based on certain conditions.
# The `PluginSettings` and `WatcherSettings` classes define the settings for
# plugins and watchers, respectively. These settings can be used to configure
# the behavior of the plugin or watcher, such as whether it is enabled and
# which channels it should monitor.
# The `JobRegistry` and `PluginRegistry` classes are used to manage the
# registered jobs and plugins, respectively. They provide methods to register
# jobs and plugins, and to initialize them when the bot starts up.
# The `INTERFACE_VERSION` constant defines the version of the interface, which
# can be used to ensure compatibility between different versions of the
# interface and plugins. This is important for maintaining stability and
# compatibility as the interface evolves over time.
# The `__all__` list defines the public API of this module, which includes
# the main classes and constants that should be accessible when this module
# is imported. This helps to encapsulate the interface and prevent
# accidental access to internal components that are not meant to be used
# directly by plugins or jobs.
# This module is designed to be extensible, allowing developers to create
# their own plugins and jobs that adhere to the defined interface. By
# following the conventions and structure provided by this interface, developers
# can create plugins that integrate seamlessly with VerseCBot, enhancing its
# functionality and providing new features for users.
