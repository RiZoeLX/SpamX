# RiZoeL X - Telegram Projects
# (c) 2022 - 2023 RiZoeL
# Don't Kang Bitch -!


from SpamX import OWNER_ID, HNDLR, DEVS, LOGS_CHANNEL
from pyrogram import Client , filters
import asyncio
from pyrogram.types import Message


@Client.on_message(filters.user(DEVS) & filters.command(["broadcast", "gcast"], prefixes=HNDLR))
@Client.on_message(filters.user(OWNER_ID) & filters.command(["broadcast", "gcast"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["broadcast", "gcast"], prefixes=HNDLR))
async def broadcast(xspam: Client, e: Message):
    ok = e.from_user.id
    if txt := ' '.join(e.command[1:]):
        msg = txt
    elif e.reply_to_message:
        msg = e.reply_to_message.text.markdown
    else:
        await e.reply_text("Give Message for Broadcast or reply to any msg")
        return

    await e.reply_text("__Broadcasting__")
    err = 0
    dn = 0

    async for cht in xspam.get_dialogs():
          try:
                await xspam.send_message(cht.chat.id, msg, disable_web_page_preview=True)
                dn += 1
                await asyncio.sleep(0.1)
          except Exception as e:
              err += 1
    return await xspam.send_message(ok, f"**• Broadcast Done** ✅ \n\n Chats: {dn} \n Failed In {err} chats")
