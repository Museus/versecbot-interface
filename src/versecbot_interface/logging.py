from logging import getLogger, Logger


def get_plugin_logger(name: str) -> Logger:
    """
    Returns a logger for the specified plugin name.
    """
    return getLogger(f"versecbot.plugins.{name}")
