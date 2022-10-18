import os
import sys
import asyncio
import re
from random import choice
from SpamX import (HNDLR, SUDO_USERS, OWNER_ID, LOGS_CHANNEL)
from pyrogram import Client, filters
from pyrogram.types import Message
from SpamX.data import *

usage = f"** ❌ Wrong Usage ❌** \n Type `{HNDLR}help spam`"

RUSERs = []

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["rraid", "replyraid"], prefixes=HNDLR))
async def rraid(xspam: Client, e: Message):
      global RUSERs
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
              RUSERs.append(id)
              mention = f"[{fname}](tg://user?id={id})"
              msg = f"Reply Raid Activated Successfully On User {mention}"
              await e.reply_text(msg)
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
              RUSERs.append(id)
              mention = f"[{fname}](tg://user?id={id})"
              msg = f"Reply Raid Activated Successfully On User {mention}"
              await e.reply_text(msg)
      else:
          await e.reply_text(usage)
      if LOGS_CHANNEL:
         try:
            await xspam.send_message(LOGS_CHANNEL, f"Activated Reply Raid By User: {e.from_user.id} \n\n On User: {mention} \n Chat: {e.chat.id}")
         except Exception as a:
             print(a)
             pass


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["draid", "dreplyraid"], prefixes=HNDLR))
async def draid(xspam: Client, e: Message):
      global RUSERs
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
              RUSERs.remove(id)
              mention = f"[{fname}](tg://user?id={id})"
              msg = "Reply Raid Deactivated Successfully"
              await e.reply_text(msg)
      elif e.reply_to_message:
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
              RUSERs.remove(id)
              mention = f"[{fname}](tg://user?id={id})"
              msg = "Reply Raid Deactivated Successfully"
              await e.reply_text(msg)
      else:
          await e.reply_text(usage)
      if LOGS_CHANNEL:
         try:
            await xspam.send_message(LOGS_CHANNEL, f" Deactivated Reply Raid By User: {e.from_user.id} \n\n User: {mention} \n Chat: {e.chat.id}")
         except Exception as a:
             print(a)
             pass


@Client.on_message(~filters.service, group=1)
async def watcher(_, msg: Message):
    global RUSERs
    id = msg.from_user.id
    if int(id) in RUSERs:
       reply = choice(REPLYRAID)
       await msg.reply_text(reply)
       
