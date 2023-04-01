
import os, sys, asyncio, re
from random import choice
from .. import (handler, Sudos, Owner, LOGS_CHANNEL)
from pyrogram import Client, filters
from pyrogram.types import Message

from RiZoeLX.data import raids, one_word, R7_ban_codes
from RiZoeLX import Devs, res_grps, res_devs
from RiZoeLX.functions import user_only

unlimited = False 

@Client.on_message(filters.user(Sudos) & filters.command(["uspam"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["uspam"], prefixes=handler))
async def uspam(SpamX: Client, e: Message):
    global unlimited
    unlimited = True
    if int(e.chat.id) in res_grps:
       await e.reply_text("**Sorry !! i Can't Spam Here.**")
       return
    msg = str(e.text[6:]) 
    if not msg:
       await e.reply("Gime Spam message bruh!")
       return
    if re.search(res_devs.lower(), msg.lower()):
       await e.reply("**Sorry !!** I can't Spam On @RiZoeLX's owner")
       return

    try:
       while unlimited == True:
           await SpamX.send_message(e.chat.id, msg)
    except Exception as ex:
           print(ex)
           await e.reply_text(f" Error -! \n\n {ex}")
           
    if LOGS_CHANNEL:
         try:
            await SpamX.send_message(LOGS_CHANNEL, f"started Unlimited Spam By User: {e.from_user.id} \n\n Chat: {e.chat.id} \n Spam Message: {msg}")
         except Exception as a:
             print(a)
             pass



@Client.on_message(filters.user(Sudos) & filters.command(["uraid"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["uraid"], prefixes=handler))
async def uraid(SpamX: Client, e: Message):
      global unlimited
      unlimited = True
      user = await user_only(SpamX, e, Owner, Sudos)
      mention = user.mention
      try:
         while unlimited == True:
           raid = choice(raids)
           raid_msg = f"{mention} {reply}"
           await SpamX.send_message(e.chat.id, raid_msg)
      except Exception as f:
           await e.reply_text(f" Error -! \n\n {f}")
           return

      if LOGS_CHANNEL:
         try:
            await SpamX.send_message(LOGS_CHANNEL, f"started Raid By User: {e.from_user.id} \n\n On User: {mention} \n Chat: {e.chat.id}")
         except Exception as a:
             print(a)
             pass
           

@Client.on_message(filters.user(Sudos) & filters.command(["abuse", "gali"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["abuse", "gali"], prefixes=handler))
async def abuse(SpamX: Client, e: Message): 
     sex = e.text[7:]
     if sex:
          counts = int(sex)
          if int(e.chat.id) in res_grps:
              return await e.reply_text("**Sorry !! i Can't Spam Here.**")
          for _ in range(counts):
              msg = choice(one_word)
              await SpamX.send_message(e.chat.id, msg)
              await asyncio.sleep(0.2)
     else:
          global unlimited
          unlimited = True
          if int(e.chat.id) in res_grps:
               return await e.reply_text("**Sorry !! i Can't Spam Here.**")
          try:
             while unlimited == True:
                 msg = choice(one_word)
                 await SpamX.send_message(e.chat.id, msg)
          except Exception as ex:
              print(ex)
              await e.reply_text(f" Error -! \n\n {ex}")


@Client.on_message(filters.user(Sudos) & filters.command(["stop"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["stop"], prefixes=handler))
async def stop(_, e: Message):
       global unlimited
       unlimited = False
       await e.reply_text("Stopped Unlimited Spam/Raid/abuse -;")

@Client.on_message(filters.user(Sudos) & filters.command(["echo", "repeat"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["echo", "repeat"], prefixes=handler))
async def echo_(SpamX: Client, message: Message):
    txt = ' '.join(message.command[1:])
    if message.reply_to_message:
        msg = message.reply_to_message.text.markdown
    elif txt:
      msg = str(txt)
    else:
        await message.reply_text(f"**Wrong Usage!** \n\n Syntax: {handler}echo (message or reply to message)")
        return

    try:
       await message.delete()
       await SpamX.send_message(message.chat.id, msg)
    except Exception as a:
       await SpamX.send_message(message.chat.id, msg)
       print(str(a))
