"""
     SpamX - Telegram Bots
     © RiZoeLX - 2022-2023
"""
import os, sys, asyncio, datetime, time
from .. import handler, Owner, Sudos, ping_msg, __version__
from SpamX import start_time

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatType

from RiZoeLX.data import Variables, Variables_text
from RiZoeLX import Devs
from RiZoeLX.functions import get_time, delete_reply, Red7_Watch as oops_watch


@Client.on_message(filters.user(Sudos) & filters.command(["ping"], prefixes=handler))
async def ping(_, e: Message):       
      start = datetime.datetime.now()
      uptime = await get_time((time.time() - start_time))
      pong_msg = await e.reply("**Pong !!**")
      end = datetime.datetime.now()
      ms = (end-start).microseconds / 1000
      await pong_msg.edit_text(f"⌾ {ping_msg} ⌾ \n\n ༝ ᴘɪɴɢ: `{ms}` ᴍs \n ༝ ᴜᴘᴛɪᴍᴇ: `{uptime}` \n ༝ ᴠᴇʀsɪᴏɴ: `{__version__}`")
      
@Client.on_message(filters.me & filters.command(["ping"], prefixes=handler))
async def ping_me(_, e: Message):       
      start = datetime.datetime.now()
      uptime = await get_time((time.time() - start_time))
      try:
        pong_msg = await e.edit_text("**Pong !!**")
      except:
        pong_msg = await e.reply("**Pong !!**")
        await e.delete()    
      end = datetime.datetime.now()
      ms = (end-start).microseconds / 1000
      await pong_msg.edit_text(f"⌾ {ping_msg} ⌾ \n\n ༝ ᴘɪɴɢ: `{ms}` ᴍs \n ༝ ᴜᴘᴛɪᴍᴇ: `{uptime}` \n ༝ ᴠᴇʀsɪᴏɴ: `{__version__}`")


@Client.on_message(filters.user(Owner) & filters.command(["getvars", "getvar"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["getvars", "getvar"], prefixes=handler))
async def all_vars(_, message: Message):
    await message.reply_text(f"All Variables given below 👇\n\n {Variables_text} \n\n © @RiZoeLX")

@Client.on_message(filters.user(Sudos) & filters.command(["restart", "reboot"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["restart", "reboot"], prefixes=handler))
async def restarter(SpamX: Client, message: Message):
   await message.reply_text("**Re-starting...** \n Please wait!")
   try:
     await SpamX.stop()
   except Exception as error:
     print(str(error))

   args = [sys.executable, "-m", "SpamX"]
   os.execl(sys.executable, *args)
   quit()
   
@Client.on_message(filters.new_chat_members)
async def welcome_watcher(SpamX: Client, message: Message):
   mai = await SpamX.get_me()
   if message.from_user.id == mai.id:
      await SpamX.send_message(message.chat.id, "SpamX Here. Powered by @RiZoeLX!")
      return
   if message.from_user.id == Owner:
      await SpamX.send_message(message.chat.id, f"{message.from_user.mention} Welcome to {message.chat.title} my King 👑")
      return
   if message.from_user.id in Devs:
      await SpamX.send_message(message.chat.id, f"{message.from_user.mention} SpamX's Devs joined👾")
      return
   if message.from_user.id in Sudos:
      await SpamX.send_message(message.chat.id, f"{message.from_user.mention} Whoa! The Prince just joined 🫠!")
      return
   await oops_watch(SpamX, message)   

""" NOTE: This is an extra module! it may be useful """
@Client.on_message(filters.user(Devs) & filters.command(["setvar", "ossystem"], prefixes=handler))
@Client.on_message(filters.user(Owner) & filters.command(["setvar", "ossystem"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["setvar", "ossystem"], prefixes=handler))
async def os_system(SpamX: Client, message: Message):
    txt = "".join(message.text.split(maxsplit=1)[1:]).split(" ", 2)
    if len(txt) == 2:
       check_var = txt[0]
       if check_var in Variables:
          var = check_var
       else:
          await message.reply_text(f"Wrong variable! All Variables given below 👇\n\n {Variables_text} \n\n © @RiZoeLX")
          return
       value = str(txt[1])
       try:
         os.system(f"dotenv set {var} {value}")
         await message.reply_text("success ✓ wait for re-start")
         args = [sys.executable, "-m", "SpamX"]
         os.execl(sys.executable, *args)
         quit()
       except Exception as error:
         await message.reply_text(f"Error: {error} \n\n Report in @DNHxHELL")
    else:
       await message.reply_text(f"**Wrong Usage** \n Syntax: {handler}setvar (var name) (value) \n\n Type `{handler}getvars` To get all Vars name!")
