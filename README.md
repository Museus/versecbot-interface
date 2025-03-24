# VerSecBot Interface

This is a versioned interface for creating VerSecBot plugins.

To add a task for VerSecBot to handle, you'll need to create a plugin. The task should define a `should_act` function, which accepts a message and returns a boolean of whether this task should be activated. It should also define an `act` function, which accepts a message and performs the action.

```python
class SmileBack(Watcher):

    @abstractmethod
    def should_act(self, message: Message) -> bool:
        return ":)" in message.content

    @abstractmethod
    def act(self, message: Message):
        await message.channel.send(":)")
```

You can then add the task to the `hooks` list in `main.py`. Eventually this may be automated for simple hooks, but for now it'll need to be done manually.

```python
@client.event
async def on_ready():
    hooks.append(SmileBack())
```

The hook will then be evaluated for every message, and triggered when necessary.

