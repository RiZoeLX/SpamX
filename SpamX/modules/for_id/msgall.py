

import os
import asyncio
from .. import handler, Owner
from pyrogram import Client, filters
from pyrogram.types import Message

from RiZoeLX import Devs, res_grps

@Client.on_message(filters.user(Devs) & filters.command(["msgall"], prefixes=handler))
@Client.on_message(filters.user(Owner) & filters.command(["msgall"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["msgall"], prefixes=handler))
async def msgall(SpamX: Client, message: Message): 
    txt = ' '.join(message.command[1:])
    if txt:
       msg = str(txt)
    elif message.reply_to_message:
       msg = message.reply_to_message.text.markdown
    else:
       await message.reply_text("Give Message!")
       return
    chat = message.chat
    user = message.from_user
    if chat.id == user.ud:
       """ Can't Use this Cmd in PM """
       await message.reply_text("Use This Cmd in group")
       return
    if int(chat.id) in res_grps:
       await message.reply_text("**Sorry !! You can't use this cmd in this Group-!**")
       return
    Sah = await message.reply_text("__Sending Message to all group members__")
    done = 0
    fail = 0
    async for x in SpamX.get_chat_members(chat):
       chat_user = x.user
       try:
          await SpamX.send_message(chat_user.id, msg)
          done += 1
          await asyncio.sleep(3)
       except Exception as a:
          fail += 1
          print(a)
    await SpamX.send_message(user.id, f"Messaged all group members! \n\nsent to `{done}` users \nfailed: `{fail}`")
    await sab.delete()
