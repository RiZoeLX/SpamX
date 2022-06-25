# RiZoeL X - Telegram Projects
# (c) 2022 - 2023 RiZoeL
# Don't Kang Bitch -!



import os
import sys
import asyncio
from random import choice
from SpamX import (OWNER_ID, HNDLR, SUDO_USERS, LOGS_CHANNEL)
from pyrogram import Client, filters
from pyrogram.types import Message
from SpamX.data import *

Usage = f"**❌ Wrong Usage ❌** \n Type: `{HNDLR}help dm`"

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["dmraid"], prefixes=HNDLR))
async def dmraid(xspam: Client, e: Message):
      """ Module: Dm Raid """
      Rizoel = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(Rizoel) == 2:
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
              counts = int(Rizoel[0])
              await e.reply_text("⚜️ Dm Raid Strated Successfully ⚜️")
              for _ in range(counts):
                    reply = choice(RAID)
                    msg = f"{reply}"
                    await xspam.send_message(id, msg)
                    await asyncio.sleep(0.10)
      elif e.reply_to_message:
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
              counts = int(Rizoel[0])
              await e.reply_text("⚜️ Dm Raid Strated Successfully ⚜️")
              for _ in range(counts):
                    reply = choice(RAID)
                    msg = f"{reply}"
                    await xspam.send_message(id, msg)
                    await asyncio.sleep(0.10)
      else:
          await xspam.reply_text(Usage)
      if LOGS_CHANNEL:
         try:
            await c.send_message(LOGS_CHANNEL, f"started DM Raid By User: {e.from_user.id} \n\n On User: {id} \n Counts: {counts}")
         except:
            await c.send_message(OWNER_ID, "Add Me In Logs Group")
            pass
         
@Client.on_message(filters.user(SUDO_USERS) & filters.command(["dm"], prefixes=HNDLR))
async def dm(xspam: Client, e: Message):
      Rizoel = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(Rizoel) == 2:
          ok = await xspam.get_users(Rizoel[0])
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
              msg = str(Rizoel[1])
              await e.reply_text("🔸 Message Delivered 🔸")
              await xspam.send_message(id, msg)
      elif e.reply_to_message:
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
              msg = str(Rizoel[0])
              await e.reply_text("🔸 Message Delivered 🔸️")
              await xspam.send_message(id, msg)
      else:
          await xspam.reply_text(Usage)
      if LOGS_CHANNEL:
         try:
            await c.send_message(LOGS_CHANNEL, f"Direct Message By User: {e.from_user.id} \n\n On User: {id}")
         except:
            await c.send_message(OWNER_ID, "Add Me In Logs Group")
            pass



@Client.on_message(filters.user(SUDO_USERS) & filters.command(["dmspam"], prefixes=HNDLR))
async def dmspam(xspam: Client, e: Message):
      Rizoel = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
      Rizoelop = Rizoel[1:]
      if len(Rizoelop) == 2:
          msg = str(Rizoelop[1])
          ok = await xspam.get_users(Rizoel[0])
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
              counts = int(Rizoelop[0])
              await e.reply_text("☢️ Dm Spam Strated ☢️")
              for _ in range(counts):
                    await xspam.send_message(id, msg)
                    await asyncio.sleep(0.10)
      elif e.reply_to_message:
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
              counts = int(Rizoel[0])
              msg = str(Rizoelop[0])
              await e.reply_text("☢️ Dm Spam Strated ☢️")
              for _ in range(counts):
                    await xspam.send_message(id, msg)
                    await asyncio.sleep(0.10)
      else:
          await xspam.reply_text(Usage)
      if LOGS_CHANNEL:
         try:
            await c.send_message(LOGS_CHANNEL, f"started DM Spam By User: {e.from_user.id} \n\n On User: {id} \n Counts: {counts} \n Message: {msg}")
         except:
            await c.send_message(OWNER_ID, "Add Me In Logs Group")
            pass
