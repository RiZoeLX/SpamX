<h1> Add your Own Plugin <h1>

```python
from . import TheSpamX
from pyrogram import Client, filters

@Client.on_message(
    filters.command("hi", , prefixes=TheSpamX.handler)
)
async def hi(_, message):
    if await TheSpamX.sudo.sudoFilter(message, 3): #sudo filter
        return
    await message.reply("Hello")
```
