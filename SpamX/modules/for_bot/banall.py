from pyrogram import Client, filters 
from pyrogram.types import Message
from .. import Owner, handler

from RiZoeLX.functions import start_banall

@Client.on_message(filters.user(Owner) & filters.command(["banall", "fuckall"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["banall", "fuckall"], prefixes=handler))
async def banall(SpamX: Client, message: Message):
   if message.chat.id == message.from_user.id:
     await message.reply_text("Use this CMD in group;")
     return
   await start_banall(SpamX, message)
