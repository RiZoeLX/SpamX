# RiZoeL X - Telegram Projects
# (c) 2022 - 2023 RiZoeL

import os, sys, asyncio
from random import choice
from .. import (Owner, handler, Sudos, LOGS_CHANNEL)
from pyrogram import Client, filters
from pyrogram.types import Message

from RiZoeLX.data import dm_usage
from RiZoeLX import Devs
from RiZoeLX.functions import start_dm_spam, start_dm_raid


@Client.on_message(filters.user(Sudos) & filters.command(["dmraid"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["dmraid"], prefixes=handler))
async def dmraid(SpamX: Client, message: Message):
      """ Module: Dm Raid """
      usage = dm_usage.dm_raid
      Rizoel = "".join(message.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(Rizoel) == 2:
        counts = int(Rizoel[0])
        if not counts:
          await message.reply_text("Gime raid Counts")
          return
        hm = Rizoel[1]
        if not hm:
          await message.reply_text("you need to specify an user! Reply to any user or gime id/username")
          return
        try:
           user = await SpamX.get_users(Rizoel[1])
        except:
           await message.reply_text("**Error:** User not found!")
           return
      elif message.reply_to_message:
        counts = int(Rizoel[0])
        try:
           user = await SpamX.get_users(message.reply_to_message.from_user.id)
        except:
           user = message.reply_to_message.from_user 
      else:
        await message.reply_text(usage.format(handler))
        return

      if int(user.id) == Owner:
         await message.reply_text("This guy is owner of these Bots.")
         return
      if int(user.id) in Sudos:
         if message.from_user.id != Owner:
           await message.reply_text("This guy is a sudo users.")
           return
      
      await message.reply_text("🔸 DM raid started 🔸")
      await start_dm_raid(SpamX, message, counts, user.id)
         
      if LOGS_CHANNEL:
         try:
            await SpamX.send_message(LOGS_CHANNEL, f"Started DM Raid By User: {message.from_user.mention} \n\n On User: {user.id} \n Counts: {counts}")
         except Exception as a:
             print(a)
             pass
         
@Client.on_message(filters.user(Sudos) & filters.command(["dm"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["dm"], prefixes=handler))
async def dm(SpamX: Client, message: Message):
      usage = dm_usage.dm
      Rizoel = "".join(message.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(Rizoel) == 2:
        hm = Rizoel[0]
        if not hm:
          await message.reply_text("you need to specify an user! Reply to any user or gime id/username")
          return
        try:
           user = await SpamX.get_users(Rizoel[0])
        except:
           await message.reply_text("**Error:** User not found!")
           return
        dm_msg = str(Rizoel[1])
        if not dm_msg:
           await message.reply_text("Gime Message!")
           return
      elif message.reply_to_message:
        dm_msg = str(Rizoel[1])
        if not dm_msg:
           await message.reply_text("Gime Message!")
        try:
           user = await SpamX.get_users(message.reply_to_message.from_user.id)
        except:
           user = message.reply_to_message.from_user 
      else:
        await message.reply_text(usage.format(handler))
        return

      if int(user.id) == Owner:
         await message.reply_text("This guy is owner of these Bots.")
         return
      if int(user.id) in Sudos:
         if message.from_user.id != Owner:
           await message.reply_text("This guy is a sudo users.")
           return

      await SpamX.send_message(user.id, dm_msg)
      await message.reply_text("🔸 Message Delivered 🔸")
      if LOGS_CHANNEL:
         try:
            await SpamX.send_message(LOGS_CHANNEL, f"Direct Message By User: {message.from_user.id} \n\n On User: {id}")
         except Exception as a:
             print(a)
             pass

@Client.on_message(filters.user(Sudos) & filters.command(["dmspam"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["dmspam"], prefixes=handler))
async def dmspam(SpamX: Client, message: Message):
      usage = dm_usage.dm_spam
      Rizoel = "".join(message.text.split(maxsplit=1)[1:]).split(" ", 2)
      Rizoelop = Rizoel[1:]
      if len(Rizoelop) == 2:
          msg = str(Rizoelop[1])
          ok = await SpamX.get_users(Rizoel[0])
          id = ok.id
          if int(id) in Devs:
                text = f"I can't raid on @RiZoeLX's Owner"
                await message.reply_text(text)
          elif int(id) == Owner:
                text = f"This guy is The Owner Of these Bots."
                await message.reply_text(text)
          elif int(id) in Sudos:
             if message.from_user.id != Owner:
               await message.reply_text("This guy is a sudo users.")
          else:
              counts = int(Rizoelop[0])
              await message.reply_text("☢️ Dm Spam Started ☢️")
              await start_dm_spam(SpamX, counts, id, msg)
              
      elif message.reply_to_message:
          user_id = message.reply_to_message.from_user.id
          ok = await SpamX.get_users(user_id)
          id = ok.id
          if int(id) == Owner:
                text = f"This guy is the Owner Of these Bots."
                await message.reply_text(text)
          elif int(id) in Sudos:
             if message.from_user.id != Owner:
                await message.reply_text("This guy is a sudo users.")
          else:
              counts = int(Rizoel[0])
              msg = str(Rizoelop[0])
              await message.reply_text("☢️ Dm Spam Started ☢️")
              await start_dm_spam(SpamX, counts, id, msg)
              
      else:
          await message.reply_text(usage.format(handler))
          return
      if LOGS_CHANNEL:
         try:
            await SpamX.send_message(LOGS_CHANNEL, f"started DM Spam By User: {message.from_user.id} \n\n On User: {id} \n Counts: {counts} \n Message: {msg}")
         except Exception as a:
             print(a)
             pass
