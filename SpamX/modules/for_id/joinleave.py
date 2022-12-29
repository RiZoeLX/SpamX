
# RiZoeL X - Telegram Projects
# (c) 2022 - 2023 RiZoeL
# Don't Kang Bitch -!



from .. import (handler, Sudos, LOGS_CHANNEL)
from pyrogram import Client, filters
from pyrogram.types import Message
from SpamX import join_errors, leave_errors


@Client.on_message(filters.user(Sudos) & filters.command(["join"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["join"], prefixes=handler))
async def join(SpamX: Client, e: Message):
    chat = e.text[6:]
    if chat.isnumeric():
        return await e.reply_text("Can't join a chat with chat id. Give username or invite link.")
    try:
      await SpamX.join_chat(chat)
      await e.reply_text("**Join Successfully ✅ **")
    except Exception as ex:
      await e.reply_text(join_errors(ex))
    if LOGS_CHANNEL:
         try:
             await SpamX.send_message(LOGS_CHANNEL, f"Joined New Chat \n\n Chat: {chat} \n Cmd By User: {e.from_user.id}")
         except Exception as a:
             print(a)
             pass

@Client.on_message(filters.user(Sudos) & filters.command(["leave"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["leave"], prefixes=handler))
async def leave(SpamX: Client, e: Message):
    rizoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
    if len(e.text) > 7:
        chat = rizoel[0]
        try:
           if chat in [-1001321613309, 1321613309, "@DNHxHELL"]:
              return
           await SpamX.leave_chat(chat)
           await e.reply_text("**Left Successfully ✅ **")
        except Exception as ex:
           await e.reply_text(leave_errors(ex))
    else:
        chat = e.chat.id
        ok = e.from_user.id
        if int(chat) == int(ok):
            return await e.reply_text(f"Usage: {handler}leave <chat username or id> or {handler}leave (type in Group for Direct leave)")
        if int(chat) == -1001321613309:
              return
        try:
           await SpamX.leave_chat(chat)
           await e.reply_text("**Left Successfully ✅ **")
        except Exception as ex:
           await e.reply_text(leave_errors(ex))
        if LOGS_CHANNEL:
           try:
                await SpamX.send_message(LOGS_CHANNEL, f"Leaved Chat \n\n Chat: {chat} \n Cmd By User: {e.from_user.id}")
           except Exception as a:
             print(a)
             pass
