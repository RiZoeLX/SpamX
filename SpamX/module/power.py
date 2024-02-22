import random

from . import TheSpamX

from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery

@Client.on_message(
    filters.command(
        [
            "spam",
            "bigspam",
            "timespam",
            "tspam",
            "delayspam",
            "dspam",
            "futurespam",
            "fspam",
            "pornspam",
            "pspam",
            "uspam",
            "unlimitedspam",
            "inlinespam",
            "ispam",
            "cspam",
            "commonspam",
        ],
        prefixes=TheSpamX.handler,
    )
)
async def spam_messages(client: Client, message: Message):
    if await TheSpamX.sudo.sudoFilter(message, 3):
        return
    x = message.text[1:]
    if " " in x:
        command = str(x.split(" ")[0])
    else:
        command = str(x)
    if command.lower() in ["spam", "bigspam"]:
        await TheSpamX.functions.start_spam(client, message, spam="spam")

    elif command.lower() in ["delayspam", "dspam"]:
        await TheSpamX.functions.start_spam(client, message, spam="delay")

    elif command.lower() in ["futurespam", "fspam", "timespam", "tspam"]:
        await TheSpamX.functions.start_spam(client, message, spam="future")

    elif command.lower() in ["pornspam", "pspam"]:
        await TheSpamX.functions.start_spam(client, message, spam="porn")

    elif command.lower() in ["unlimitedspam", "uspam"]:
        if await TheSpamX.sudo.sudoFilter(message):
            return
        await TheSpamX.functions.start_spam(client, message, spam="loop")

    elif command.lower() in ["inlinespam", "ispam"]:
        await TheSpamX.functions.inline_spam(client, message)

    elif command.lower() in ["commonspam", "cspam"]:
        await TheSpamX.functions.start_common_spam(client, message)

@Client.on_message(
    filters.command(
        [
            "dmspam",
            "dm",
            "message",
            "dmraid",
        ],
        prefixes=TheSpamX.handler
    )
)
async def direct_messages(client: Client, message: Message):
    if await TheSpamX.sudo.sudoFilter(message, 3):
        return
    x = message.text[1:]
    if " " in x:
        command = str(x.split(" ")[0])
    else:
        command = str(x)
    if command.lower() == "dmspam":
        await TheSpamX.functions.direct_messages(client, message, "spam")

    elif command.lower() == "dmraid":
        await TheSpamX.functions.direct_messages(client, message, "raid")

    elif command.lower() in ["dm", "message"]:
        await TheSpamX.functions.direct_messages(client, message, "message")

@Client.on_message(
    filters.command(
        [
            "raid",
            "multiraid",
            "mraid",
            "replyraid",
            "rraid",
            "areplyraid",
            "arraid",
            "dreplyraid",
            "drraid",
        ],
        prefixes=TheSpamX.handler
    )
)
async def raids(client: Client, message: Message):
    if await TheSpamX.sudo.sudoFilter(message, 3):
        return
    x = message.text[1:]
    if " " in x:
        command = str(x.split(" ")[0])
    else:
        command = str(x)
    if command.lower() == "raid":
        await TheSpamX.functions.raid(client, message)

    elif command.lower() in ["multiraid", "mraid"]:
        await TheSpamX.functions.raid(client, message, multi=True)

    elif command.lower() in ["replyraid", "rraid"]:
        await TheSpamX.functions.replyraid(client, message)

    elif command.lower() in ["areplyraid", "arraid"]:
        await TheSpamX.functions.replyraid(client, message, "enable")

    elif command.lower() in ["dreplyraid", "drraid"]:
        await TheSpamX.functions.replyraid(client, message, "disable")

@Client.on_message(
    filters.all
)
async def replayraid_watcher(_, message: Message):
    if message.from_user.id in TheSpamX.functions.raid_users:
        await message.reply(random.choice(TheSpamX.functions.raid_args))

@Client.on_message(
    filters.command("stop")
)
async def stop_uspam(_, message: Message):
    if await TheSpamX.sudo.sudoFilter(message):
        return
    if message.chat.id in TheSpamX.functions.unlimited:
        TheSpamX.functions.unlimited.remove(message.chat.id)
        await message.reply(f"__✅ Stopped Unlimited spam in {message.chat.title}!__")
        TheSpamX.activeTasks.pop(message.chat.id)
    else:
        await message.reply(f"__❎ No any active task in {message.chat.title}.__")

@Client.on_callback_query(filters.regex("inline"))
async def inlineSpamCB(_, callback: CallbackQuery):
    await callback.answer(
        str(random.choice(TheSpamX.functions.raid_args)),
        show_alert=True,
    )
