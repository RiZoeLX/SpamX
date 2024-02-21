import datetime
import time
import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatType, ChatMemberStatus

from . import TheSpamX

@Client.on_message(
    filters.command("ping", prefixes=TheSpamX.handler) #& filters.user(TheSpamX.sudo.sudoUsers)
)
async def ping(_, message: Message):
    if await TheSpamX.sudo.sudoFilter(message, 3):
        return
    start = datetime.datetime.now()
    #u_time = int(int(time.time()) - int(TheSpamX.startTime))
    #uptime = await TheSpamX.functions.get_time(time=u_time)
    pong_msg = await message.reply("**Pong !!**")
    end = datetime.datetime.now()
    ms = (end-start).microseconds / 1000
    try:
        await pong_msg.edit_text(f"⌾ {TheSpamX.pingMsg} ⌾ \n\n ༝ ᴘɪɴɢ: `{ms}` ᴍs \n ༝ ᴠᴇʀsɪᴏɴ: `{TheSpamX.versions['SpamX']}`")
    except:
        await pong_msg.edit_text(f"⌾ {TheSpamX.pingMsg} ⌾ \n\n ༝ ᴘɪɴɢ: `{ms}` ᴍs \n ༝ ᴠᴇʀsɪᴏɴ: `{TheSpamX.versions['SpamX']}`")
        await pong_msg.delete()

@Client.on_message(
    filters.command("alive", prefixes=TheSpamX.handler) #& filters.user(TheSpamX.sudo.sudoUsers)
)
async def alive(SpamX: Client, message: Message):
    if await TheSpamX.sudo.sudoFilter(message, 3):
        return
    await TheSpamX.functions.send_alive(SpamX, message)

@Client.on_message(
    filters.command("limit", prefixes=TheSpamX.handler) #& filters.user(TheSpamX.sudo.sudoUsers)
)
async def check_limit(SpamX: Client, message: Message):
    if await TheSpamX.sudo.sudoFilter(message, 3):
        return
    if SpamX.me.is_bot:
        return
    event = await message.reply_text("__Checking your account for Spambot...__")
    try:
        await SpamX.unblock_user("spambot")
        await SpamX.send_message("spambot", "/start")
        await asyncio.sleep(2)
        async for history in SpamX.get_chat_history("spambot", limit=1):
            await TheSpamX.functions.delete_reply(message, event, str(history.text))
    except Exception as error:
        await TheSpamX.functions.delete_reply(message, event, str(error))

@Client.on_message(
    filters.command(["help", "restart", "reboot"], prefixes=TheSpamX.handler) #& filters.user(TheSpamX.sudo.sudoUsers)
)
async def help_reboot(_, message: Message):
    if await TheSpamX.sudo.sudoFilter(message, 3):
        return
    if "reboot" or "restart" in message.text.lower():
        await message.reply(
            f"**[Click Here.](https://t.me/{TheSpamX.SpamX.me.username}?start=reboot) to reboot your SpamX!**",
            disable_web_page_preview=True,
        )
    elif "help" in message.text.lower():
        await message.reply(
            f"**[Click Here.](https://t.me/{TheSpamX.SpamX.me.username}?start=help) for help menu of SpamX!**",
            disable_web_page_preview=True,
        )

@Client.on_message(filters.command(["stats", "stat"], prefixes=TheSpamX.handler))
async def stats(SpamX: Client, message: Message):
    if SpamX.me.is_bot:
        await message.reply("__This command is only for id not for bot__")
        return
    if await TheSpamX.sudo.sudoFilter(message):
        return
    wait = await message.reply_text("collecting....")
    start = datetime.datetime.now()
    private = 0
    gc = 0
    super_gc = 0
    channel = 0
    bot = 0
    admin_gc = 0
    async for dialog in SpamX.get_dialogs():
        if dialog.chat.type == ChatType.PRIVATE:
            private += 1
        elif dialog.chat.type == ChatType.BOT:
            bot += 1
        elif dialog.chat.type == ChatType.GROUP:
            gc += 1
        elif dialog.chat.type == ChatType.SUPERGROUP:
            super_gc += 1
            admin = await dialog.chat.get_member(int(SpamX.me.id))
            if admin.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
                admin_gc += 1
        elif dialog.chat.type == ChatType.CHANNEL:
            channel += 1

    end = datetime.datetime.now()
    ms = (end - start).seconds
    stats = f"{SpamX.me.first_name}'s stats \n\n"
    stats += "------------- » «» « ------------- \n"
    stats += f"Private Messages: `{private}` \n"
    stats += f"Bots in Inbox: `{bot}` \n"
    stats += f"Total Groups: `{gc}` \n"
    stats += f"Total Super Groups: `{super_gc}` \n"
    stats += f"Total Channels: `{channel}` \n"
    stats += f"Admin in: `{admin_gc}` chats \n\n"
    stats += "------------- » «» « ------------- \n\n"
    stats += f"Time Taken `{ms}secs` \n"
    stats += f"© @{TheSpamX.updateChannel}"
    await TheSpamX.functions.delete_reply(message, wait, stats)