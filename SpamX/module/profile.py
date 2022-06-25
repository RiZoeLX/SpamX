# RiZoeL X - Telegram Projects
# (c) 2022 - 2023 RiZoeL
# Don't Kang Bitch -!




import os
import sys
from random import choice
from SpamX import (OWNER_ID, HNDLR, SUDO_USERS, hl, LOGS_CHANNEL)
from pyrogram import Client, filters
from pyrogram.types import Message
from SpamX.data import *

Usage = f"**❌ Wrong Usage ❌** \n Type: `{HNDLR}help owner`"

@Client.on_message(filters.user(OWNER_ID) & filters.command(["setpic"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["setpic"], prefixes=HNDLR))
async def setpic(_, e: Message):
     replied = e.reply_to_message
     if replied.video or replied.photo:
        try:
            media = await replied.download_media()
        except:
            pass
        await Client.set_profile_photo(media)
        await e.reply_text(f"**Changed profile picture successfully** ✅")
        try:
            os.remove(media)
        except Exception as e:
            print(str(e))
     else:
         await e.reply_text("Reply To Media or Video To Change Profile pic")
     if LOGS_CHANNEL:
         try:
            await c.send_message(LOGS_CHANNEL, f"Profile Pic Changed By User: {e.from_user.id}")
         except:
            await c.send_message(OWNER_ID, "Add Me In Logs Group")
            pass
      
etc_bio = "ᴜsᴇʀ ᴏғ ʀɪᴢᴏᴇʟ x sᴘᴀᴍ"

@Client.on_message(filters.user(OWNER_ID) & filters.command(["setname"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["setname"], prefixes=HNDLR))
async def setname(xspam: Client, e: Message): 
      Rizoel = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(Rizoel) == 1:
          name = str(Rizoel[0])
          try:
            await xspam.update_profile(first_name=name, bio=etc_bio)
            await e.reply_text(f"**Profile Name Changed Successfully !!** \n\n **New Name:** {name}")
          except Exception as ex:
            await e.reply_text(f"**Error !!** \n\n {ex}")
            print(ex)
      else:
          await e.reply_text(Usage)
      if LOGS_CHANNEL:
         try:
            await c.send_message(LOGS_CHANNEL, f"Name Changed By User {e.from_user.id} \n\n New Name: {name}")
         except:
            await c.send_message(OWNER_ID, "Add Me In Logs Group")
            pass

@Client.on_message(filters.user(OWNER_ID) & filters.command(["setbio"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["setbio"], prefixes=HNDLR))
async def setbio(xspam: Client, e: Message):
      Rizoel = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(Rizoel) == 1:
          xd = str(Rizoel[0])
          ok = await xspam.get_me()
          nam = ok.first_name
          nam2 = ok.last_name
          try:
             await xspam.update_profile(first_name=nam, last_name=nam2, bio=xd)
             await e.reply_text(f"**Profile Bio Changed Successfully !** \n\n **New Bio**: {xd}")
          except Exception as ex:
            await e.reply_text(f"**Error !!** \n\n {ex}")
            print(ex)
      else:
          await e.reply_text(Usage)
      if LOGS_CHANNEL:
         try:
            await c.send_message(LOGS_CHANNEL, f"Bio Changed By User: {e.from_user.id} \n\n New Bio: {xd}")
         except:
            await c.send_message(OWNER_ID, "Add Me In Logs Group")
            pass
