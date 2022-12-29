"""
    © RiZoeLX
    SpamX
"""

from pyrogram import Client, filters
from pyrogram.types import Message
from .. import Sudos, Owner, handler, DATABASE_URL
from SpamX.database import gban_db
from RiZoeLX import Devs
from RiZoeLX.functions import get_user, get_id
from SpamX.core import user_errors

@Client.on_message(filters.user(Sudos) & filters.command(["info"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["info"], prefixes=handler))
async def _info(SpamX: Client, e: Message):
   try:
      user = await get_user(SpamX, e)
   except Exception as eror:
      await e.reply_text(user_errors(eror))
      return 
   msg = "**User Info** \n\n"
   msg += f"**First Name:** {user.first_name} \n"
   if user.last_name:
     msg += f"**Last Name:** {user.last_name} \n"
   msg += f"**User ID:** `{user.id}` \n"
   if user.username:
     msg += f"**Username:** @{user.username} \n"
   msg += f"**Permit link** [link](tg://user?id={user.id}) \n"
   if int(user.id) in Devs:
     msg += "**Rank:** Dev of SpamX-"
     await e.reply_text(msg)
     return 
   if int(user.id) == int(Owner):
     msg += "**Rank:** Owner"
     await e.reply_text(msg)
     return 
   if int(user.id) in Sudos:
     msg += "**Rank:** Sudo"
     await e.reply_text(msg)
     return 
   if DATABASE_URL:
     if gban_db.check(user.id):
        msg += "**User in Gbanned list!"
     await e.reply_text(msg)


@Client.on_message(filters.user(Sudos) & filters.command(["id"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["id"], prefixes=handler))
async def _id(SpamX: Client, e: Message):
   await get_id(SpamX, e)
