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

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["raid"], prefixes=HNDLR))
async def raid(xspam: Client, e: Message):  
      Rizoel = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(Rizoel) == 2:
        counts = int(Rizoel[0])
        if not counts:
          await e.reply_text(f"Gime raid Counts or use `{HNDLR}.uraid` for Unlimited raid!")
          return
        hm = Rizoel[1]
        if not hm:
          await e.reply_text("you need to specify an user! Reply to any user or gime id/username")
          return
        try:
           user = await xspam.get_users(Rizoel[1])
        except:
           await e.reply_text("**Error:** User not found!")
           return
      elif e.reply_to_message:
        counts = int(Rizoel[0])
        try:
           user = await xspam.get_users(e.reply_to_message.from_user.id)
        except:
           user = e.reply_to_message.from_user 
      else:
        await e.reply_text(usage)
        return
      if int(e.chat.id) in GROUP:
         await e.reply_text("**Sorry !! i Can't Spam Here.**")
         return
      if int(user.id) in RiZoeLX:
         await e.reply_text("I can't raid on @RiZoeLX's Owner")
         return
      if int(user.id) == OWNER_ID:
         await e.reply_text("This guy is Owner Of these Bots.")
         return
      if int(user.id) in SUDO_USERS:
         if e.from_user.id != OWNER_ID:
           await e.reply_text("This guy is a sudo users.")
           return
      mention = user.mention
      for _ in range(counts): 
         raid_text = f"{mention} {choice(RAID)}"
         await xspam.send_message(e.chat.id, raid_text)
         await asyncio.sleep(0.3)

      if LOGS_CHANNEL:
         try:
            await xspam.send_message(LOGS_CHANNEL, f"started Raid By User: {e.from_user.id} \n\n On User: {mention} \n Chat: {e.chat.id} \n Counts: {counts}")
         except Exception as a:
            print(a)
            pass


RUSERs = []

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["rraid", "replyraid"], prefixes=HNDLR))
async def rraid(xspam: Client, e: Message):
      global RUSERs
      Rizoel = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 1)
      if Rizoel:
         try:
            user = await xspam.get_users(Rizoel[0]) 
         except:
            await e.reply_text("**Error:** User not found!")
            return
      elif e.reply_to_message:
         try:
            user = await xspam.get_users(e.reply_to_message.from_user.id)
         except:
            user = e.reply_to_message.from_user
      else:
         await e.reply_text("You need to specify an user!")
         return
      if int(e.chat.id) in GROUP:
         await e.reply_text("**Sorry !! i Can't Spam Here.**")
         return
      if int(user.id) in RiZoeLX:
         await e.reply_text("I can't raid on @RiZoeLX's Owner")
         return
      elif int(user.id) == OWNER_ID:
         await e.reply_text("This guy is Owner Of these Bots.")
         return
      elif int(user.id) in SUDO_USERS:
         await e.reply_text("This guy is a sudo users.")
         return
      else:
         RUSERs.append(user.id)
         mention = user.mention
         await e.reply_text(f"Reply Raid Activated Successfully On User {mention}")
      if LOGS_CHANNEL:
         try:
            await xspam.send_message(LOGS_CHANNEL, f"Activated Reply Raid By User: {e.from_user.id} \n\n On User: {mention} \n Chat: {e.chat.id}")
         except Exception as a:
             print(a)
             pass


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["draid", "dreplyraid"], prefixes=HNDLR))
async def draid(xspam: Client, e: Message):
      global RUSERs
      Rizoel = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 1)
      if Rizoel:
         try:
            user = await xspam.get_users(Rizoel[0]) 
         except:
            await e.reply_text("**Error:** User not found!")
            return
      elif e.reply_to_message:
         try:
            user = await xspam.get_users(e.reply_to_message.from_user.id)
         except:
            user = e.reply_to_message.from_user
      else:
         await e.reply_text("You need to specify an user!")
         return
      if int(e.chat.id) in GROUP:
         await e.reply_text("**Sorry !! i Can't Spam Here.**")
         return
      if int(user.id) in RiZoeLX:
         await e.reply_text("I can't raid on @RiZoeLX's Owner")
         return
      elif int(user.id) == OWNER_ID:
         await e.reply_text("This guy is Owner Of these Bots.")
         return
      elif int(user.id) in SUDO_USERS:
         await e.reply_text("This guy is a sudo users.")
         return
      else:
         RUSERs.remove(user.id)
         mention = user.mention
         await e.reply_text(f"Reply Raid Activated Successfully On User {mention}")
      if LOGS_CHANNEL:
         try:
            await xspam.send_message(LOGS_CHANNEL, f" Deactivated Reply Raid By User: {e.from_user.id} \n\n User: {mention} \n Chat: {e.chat.id}")
         except Exception as a:
             print(a)
             pass


@Client.on_message(filters.all)
async def watcher(_, msg: Message):
    global RUSERs
    id = msg.from_user.id
    if int(msg.chat.id) in GROUP:
       return
    if int(id) in RUSERs:
       reply = choice(REPLYRAID)
       await msg.reply_text(reply)
       
