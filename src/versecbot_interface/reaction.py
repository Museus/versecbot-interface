from discord import Message, PartialEmoji, Member, User
from typing import Union


class VersecbotReaction:
    def __init__(
        self, *, message: Message, emoji: PartialEmoji, user: Union[Member, User]
    ):
        self.channel = message.channel
        self.message = message
        self.emoji = emoji
        self.user = user
