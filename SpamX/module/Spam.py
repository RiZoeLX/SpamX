# RiZoeL X - Telegram Projects
# (c) 2022 - 2023 RiZoeL
# Don't Kang Bitch -!



import os
import sys
import asyncio
import re
from random import choice
from SpamX import (HNDLR, SUDO_USERS, OWNER_ID, LOGS_CHANNNEL)
from pyrogram import Client, filters
from pyrogram.types import Message
from SpamX.data import *


usage = f"** ❌ Wrong Usage ❌** \n Type `{HNDLR}help spam`"


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["spam"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["spam"], prefixes=HNDLR))
async def spam(xspam: Client, e: Message): 
    Rizoel = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 1)
    if len(Rizoel) == 2:
       counts = int(Rizoel[0])
       if int(e.chat.id) in GROUP:
            return await e.reply_text("**Sorry !! i Can't Spam Here.**")
       msg = str(Rizoel[1])
       if re.search(Owners.lower(), msg.lower()):
            return await e.reply("**Sorry !!** I can't Spam On @RiZoeLX's owner")
       if e.reply_to_message:
          reply_to_id = e.reply_to_message.message_id
          for _ in range(counts):
              await xspam.send_message(e.chat.id, msg, reply_to_message_id=reply_to_id)
              await asyncio.sleep(0.1)
          return
       for _ in range(counts):
           await xspam.send_message(e.chat.id, msg)
           await asyncio.sleep(0.1)
    else:
        await xspam.reply(usage)
    if LOGS_CHANNEL:
         try:
            await c.send_message(LOGS_CHANNEL, f"started Spam By User: {e.from_user.id} \n\n Chat: {e.chat.id} \n Counts: {counts} \n Spam Message: {msg}")
         except:
            await c.send_message(OWNER_ID, "Add Me In Logs Group")
            pass



@Client.on_message(filters.user(SUDO_USERS) & filters.command(["delayspam"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["delayspam"], prefixes=HNDLR))
async def delayspam(xspam: Client, e: Message): 
    Rizoel = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
    Rizoelop = Rizoel[1:]
    if len(Rizoelop) == 2:
       counts = int(Rizoelop[0])
       if int(e.chat.id) in GROUP:
            return await e.reply_text("**Sorry !! i Can't Spam Here.**")
       msg = str(Rizoelop[1])
       if re.search(Owners.lower(), msg.lower()):
            return await e.reply("**Sorry !!** I can't Spam On @RiZoeLX's owner")
       sleeptime = float(Rizoel[0])
       if e.reply_to_message:
          reply_to_id = e.reply_to_message.message_id
          for _ in range(counts):
              await xspam.send_message(e.chat.id, msg, reply_to_message_id=reply_to_id)
              await asyncio.sleep(sleeptime)
          return
       for _ in range(counts):
           await xspam.send_message(e.chat.id, msg)
           await asyncio.sleep(sleeptime)
    else:
        await xspam.reply(usage)   
    if LOGS_CHANNEL:
         try:
            await c.send_message(LOGS_CHANNEL, f"started Delay Spam By User: {e.from_user.id} \n\n Chat: {e.chat.id} \n Counts: {counts} \n Spam Message: {msg} \n Delay Time: {sleeptime}")
         except:
            await c.send_message(OWNER_ID, "Add Me In Logs Group")
            pass



@Client.on_message(filters.user(SUDO_USERS) & filters.command(["pornspam"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["pornspam"], prefixes=HNDLR))
async def pornspam(xspam: Client, e: Message): 
    counts = e.command[1]
    if not counts:
        return await e.reply_text(usage)
    if int(e.chat.id) in GROUP:
         return await e.reply_text("**Sorry !! i Can't Spam Here.**")
    rizoel = "**#Pornspam**"
    count = int(counts)
    for _ in range(count):
         prn = choice(PORM)
         if ".jpg" in prn or ".png" in prn:
              await xspam.send_photo(e.chat.id, prn, caption=rizoel)
              await asyncio.sleep(0.4)
         if ".mp4" in prn or ".MP4," in prn:
              await xspam.send_video(e.chat.id, prn, caption=rizoel)
              await asyncio.sleep(0.4)
    if LOGS_CHANNEL:
         try:
            await c.send_message(LOGS_CHANNEL, f"started Porn Spam By User: {e.from_user.id} \n Chat: {e.chat.id} \n Counts: {count}")
         except:
            await c.send_message(OWNER_ID, "Add Me In Logs Group")
            pass



@Client.on_message(filters.user(SUDO_USERS) & filters.command(["raid"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["raid"], prefixes=HNDLR))
async def raid(xspam: Client, e: Message):  
      Rizoel = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(Rizoel) == 2:
          counts = int(Rizoel[0])
          if int(e.chat.id) in GROUP:
               return await e.reply_text("**Sorry !! i Can't Spam Here.**")
          ok = await xspam.get_users(Rizoel[1])
          id = ok.id
          if int(id) in RiZoeLX:
                text = f"I can't raid on @RiZoeLX's Owner"
                await e.reply_text(text)
          elif int(id) == OWNER_ID:
                text = f"This guy is Owner Of this Bots."
                await e.reply_text(text)
          elif int(id) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply_text(text)
          else:
              fname = ok.first_name
              mention = f"[{fname}](tg://user?id={id})"
              for _ in range(counts):
                    reply = choice(RAID)
                    msg = f"{mention} {reply}"
                    await xspam.send_message(e.chat.id, msg)
                    await asyncio.sleep(0.10)
      elif e.reply_to_message:
          #msg_id = e.reply_to_message.message_id
          counts = int(Rizoel[0])
          if int(e.chat.id) in GROUP:
               return await e.reply_text("**Sorry !! i Can't Spam Here.**")
          #RiZoeL = xspam.get_messages(e.chat.id, msg_id)
          user_id = e.reply_to_message.from_user.id
          ok = await xspam.get_users(user_id)
          id = ok.id
          if int(id) in RiZoeLX:
                text = f"I can't raid on @RiZoeLX's Owner"
                await e.reply_text(text)
          elif int(id) == OWNER_ID:
                text = f"This guy is Owner Of this Bots."
                await e.reply_text(text)
          elif int(id) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply_text(text)
          else:
              fname = ok.first_name
              mention = f"[{fname}](tg://user?id={id})"
              for _ in range(counts):
                    reply = choice(RAID)
                    msg = f"{mention} {reply}"
                    await xspam.send_message(e.chat.id, msg)
                    await asyncio.sleep(0.10)
      else:
          await xspam.reply(usage)
      if LOGS_CHANNEL:
         try:
            await c.send_message(LOGS_CHANNEL, f"started Raid By User: {e.from_user.id} \n\n On User: {mention} \n Chat: {e.chat.id} \n Counts: {counts}")
         except:
            await c.send_message(OWNER_ID, "Add Me In Logs Group")
            pass

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["fspam", "fastspam"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["fspam", "fastspam"], prefixes=HNDLR))
async def spam(xspam: Client, e: Message):
    warn = await e.reply_text("**Note:** Don't Blame to @RiZoeLX If IDs Get ban -!")
    await asyncio.sleep(3)
    await warn.delete()
    Rizoel = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 1)
    if len(Rizoel) == 2:
       counts = int(Rizoel[0])
       if int(e.chat.id) in GROUP:
            return await e.reply_text("**Sorry !! i Can't Spam Here.**")
       msg = str(Rizoel[1])
       if re.search(Owners.lower(), msg.lower()):
            return await e.reply("**Sorry !!** I can't Spam On @RiZoeLX's owner")
       if e.reply_to_message:
          reply_to_id = e.reply_to_message.message_id
          for _ in range(counts):
              await xspam.send_message(e.chat.id, msg, reply_to_message_id=reply_to_id)
              await asyncio.sleep(0.002)
          return
       for _ in range(counts):
           await xspam.send_message(e.chat.id, msg)
           await asyncio.sleep(0.002)
    else:
        await xspam.reply(usage)
    if LOGS_CHANNEL:
         try:
            await c.send_message(LOGS_CHANNEL, f"started Fast Spam By User: {e.from_user.id} \n\n Chat: {e.chat.id} \n Counts: {counts} \n Spam Message: {msg}")
         except:
            await c.send_message(OWNER_ID, "Add Me In Logs Group")
            pass

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["hang"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["hang"], prefixes=HNDLR))
async def pornspam(xspam: Client, e: Message): 
    counts = e.command[1]
    if not counts:
        return await e.reply_text(usage)
    if int(e.chat.id) in GROUP:
         return await e.reply_text("**Sorry !! i Can't Spam Here.**")
    rizoel = ""
    count = int(counts)
    for _ in range(count):
         await xspam.send_message(e.chat.id, rizoel)
         await asyncio.sleep(0.3)
    if LOGS_CHANNEL:
         try:
            await c.send_message(LOGS_CHANNEL, f"started Hang Spam By User: {e.from_user.id} \n\n Chat: {e.chat.id} \n Counts: {count}")
         except:
            await c.send_message(OWNER_ID, "Add Me In Logs Group")
            pass
