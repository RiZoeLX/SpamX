
# RiZoeL X - Telegram Projects
# (c) 2022 - 2023 RiZoeL
# Don't Kang Bitch -!



from SpamX import (OWNER_ID, HNDLR, SUDO_USERS, LOGS_CHANNEL)
from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["join"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["join"], prefixes=HNDLR))
async def join(xspam: Client, e: Message):
    chat = e.text[6:]
    if chat.isnumeric():
        return await e.reply_text("Can't join a chat with chat id. Give username or invite link.")
    try:
      await xspam.join_chat(chat)
      await e.reply_text("**Join Successfully ✅ **")
    except Exception as ex:
        await e.reply_text(f"**ERROR:** \n\n{str(ex)}")
    if LOGS_CHANNEL:
         try:
            await c.send_message(LOGS_CHANNEL, f"Joined New Chat \n\n Chat: {chat} \n Cmd By User: {e.from_user.id}")
         except:
            await c.send_message(OWNER_ID, "Add Me In Logs Group")
            pass

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["leave"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["leave"], prefixes=HNDLR))
async def leave(xspam: Client, e: Message):
    rizoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
    if len(e.text) > 7:
        chat = rizoel[0]
        try:
           await xspam.leave_chat(chat)
           await e.reply_text("**Left Successfully ✅ **")
        except Exception as ex:
           await e.reply_text(f"**ERROR:** \n\n{str(ex)}")
    else:
        chat = e.chat.id
        ok = e.from_user.id
        if int(chat) == int(ok):
            return await e.reply_text(f"Usage: {HNDLR}leave <chat username or id> or {HNDLR}leave (type in Group for Direct leave)")
        if int(chat) == -1001321613309:
              return e.reply_text("**Error**")
        try:
           await xspam.leave_chat(chat)
           await e.reply_text("**Left Successfully ✅ **")
        except Exception as ex:
           await e.reply_text(f"**ERROR:** \n\n{str(ex)}")
        if LOGS_CHANNEL:
           try:
              await c.send_message(LOGS_CHANNEL, f"Leaved Chat \n\n Chat: {chat} \n Cmd By User: {e.from_user.id}")
           except:
              await c.send_message(OWNER_ID, "Add Me In Logs Group")

