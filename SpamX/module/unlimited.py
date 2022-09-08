
import os
import sys
import asyncio
import re
from random import choice
from SpamX import (HNDLR, SUDO_USERS, OWNER_ID, LOGS_CHANNEL)
from pyrogram import Client, filters
from pyrogram.types import Message
from SpamX.data import *


WORD = [ "AJA", "TERI", "MAA", "KI", "CHUT", "FAAD", "DUNGA", "HIJDE", "TERA", "BAAP", "HU", "KIDXX", "SPEED", "PAKAD", "BHEN KE LAUDE", "AA BETA", " ADITYA", "AAGYA", "TERI", "MAA ", "CHODNE", "AB", "TERI ", "MAA", "CHUDEGI", "KUTTE", "KI", "TARAH", "BETA", "TERI", "MAA", "KE", "BHOSDE", "ME", "JBL", "KE", "SPEAKER", "DAAL", "KAR", "BASS", "BOOSTED", "SONG", "SUNUNGA", "PURI", "RAAT", "LAGATAR", "TERI", "MAA", "KE", "SATH", "SEX", "KARUNGA🔥", "TERI", "MAA", "KE", "BOOBS", "DABAUNGA","XXX","TERI","MAA","KAA","CHUT","MARU","RANDI","KEE","PILEE","TERI","MAA","KAA","BHOSDAA","MARU","SUAR","KEE","CHODE","TERI","MAAA","KEEE","NUDES","BECHUNGA","RANDI","KEE","PILLE","TERI","MAAA","CHODU","SUAR","KEEE","PILEE","TERIII","MAAA","DAILYY","CHUDTTI","HAII","MADHARCHOD","AUKAT","BANAA","LODE","TERAA","BAAP","HUU","TERI","GFF","KAA","BHOSDAA","MARUU","MADHARCHOD","TERI ","NANAI","KAA","CHUTT","MARU","TERII","BEHEN","KAAA","BHOSDAA","MARU","RANDII","KEEE","CHODE","TERI","DADI","KAAA","BOOR","GARAM","KARR","TERE","PUREE","KHANDAN","KOOO","CHODUNGAA","BAAP","SEE","BAKCHODI","KAREGAA","SUARR","KEEE","PILLEE","NAAK","MEEE","NETAA","BAAP","KOO","KABHII","NAAH","BOLNAA","BETAA","CHUSS","LEEE","MERAA","LODAA","JAISE","ALUU","KAAA","PAKODAA","TERI","MAAA","BEHEN","GFF","NANI","DIIN","RAAT","SOTEE","JAGTEE","PELTAA","HUUU","LODEE","CHAAR","CHAWNII","GHODEE","PEEE","TUMM","MEREE","LODEE","PEE","TERI","MAA","KAAA","BOOBS","DABATA HU",]


usage = f"** ❌ Wrong Usage ❌** \n Type `{HNDLR}help extra`"
unlimited = False 

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["uspam"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["uspam"], prefixes=HNDLR))
async def fastspam(xspam: Client, e: Message):
    global unlimited
    unlimited = True
    if int(e.chat.id) in GROUP:
           return await e.reply_text("**Sorry !! i Can't Spam Here.**")
    msg = str(e.text[6:])
    if re.search(Owners.lower(), msg.lower()):
         return await e.reply("**Sorry !!** I can't Spam On @RiZoeLX's owner")
    try:
       while unlimited == True:
           await xspam.send_message(e.chat.id, msg)
    except Exception as ex:
           print(ex)
           await e.reply_text(f" Error -! \n\n {ex}")
           
    if LOGS_CHANNEL:
         try:
            await xspam.send_message(LOGS_CHANNEL, f"started Unlimited Spam By User: {e.from_user.id} \n\n Chat: {e.chat.id} \n Spam Message: {msg}")
         except Exception as a:
             print(a)
             pass



@Client.on_message(filters.user(SUDO_USERS) & filters.command(["uraid"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["uraid"], prefixes=HNDLR))
async def raid(xspam: Client, e: Message):
      global unlimited
      unlimited = True
      Rizoel = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 1)
      if len(Rizoel) == 1:
          if int(e.chat.id) in GROUP:
               return await e.reply_text("**Sorry !! i Can't Spam Here.**")
          ok = await xspam.get_users(Rizoel[0])
          id = ok.id
          if int(id) in RiZoeLX:
                text = f"I can't raid on @RiZoeLX's Owner"
                await e.reply_text(text)
          elif int(id) == OWNER_ID:
                text = f"This guy is the Owner Of these Bots."
                await e.reply_text(text)
          elif int(id) in SUDO_USERS:
                text = f"This guy is sudo user."
                await e.reply_text(text)
          else:
              fname = ok.first_name
              mention = f"[{fname}](tg://user?id={id})"
              try:
                 while unlimited == True:
                     reply = choice(RAID)
                     msg = f"{mention} {reply}"
                     await xspam.send_message(e.chat.id, msg)
              except Exception as f:
                  print(f)
                  await e.reply_text(f" Error -! \n\n {f}")
                  
      elif e.reply_to_message:
          #msg_id = e.reply_to_message.message_id
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
                text = f"This guy the Owner Of these Bots."
                await e.reply_text(text)
          elif int(id) in SUDO_USERS:
                text = f"This guy is sudo user."
                await e.reply_text(text)
          else:
              fname = ok.first_name
              mention = f"[{fname}](tg://user?id={id})"
              try:
                 while unlimited == True:
                     reply = choice(RAID)
                     msg = f"{mention} {reply}"
                     await xspam.send_message(e.chat.id, msg)
              except Exception as f:
                  print(f)
                  await e.reply_text(f" Error -! \n\n {f}")
      else:
          await e.reply_text(usage)
      if LOGS_CHANNEL:
         try:
            await xspam.send_message(LOGS_CHANNEL, f"started Raid By User: {e.from_user.id} \n\n On User: {mention} \n Chat: {e.chat.id}")
         except Exception as a:
             print(a)
             pass
           

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["abuse", "gali"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["abuse", "gali"], prefixes=HNDLR))
async def abuse(xspam: Client, e: Message): 
     sex = e.text[7:]
     if sex:
          counts = int(sex)
          if int(e.chat.id) in GROUP:
              return await e.reply_text("**Sorry !! i Can't Spam Here.**")
          for _ in range(counts):
              msg = choice(WORD)
              await xspam.send_message(e.chat.id, msg)
              await asyncio.sleep(0.001)
     else:
          global unlimited
          unlimited = True
          if int(e.chat.id) in GROUP:
               return await e.reply_text("**Sorry !! i Can't Spam Here.**")
          try:
             while unlimited == True:
                 msg = choice(WORD)
                 await xspam.send_message(e.chat.id, msg)
          except Exception as ex:
              print(ex)
              await e.reply_text(f" Error -! \n\n {ex}")


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["stop"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["stop"], prefixes=HNDLR))
async def spam(_, e: Message):
       global unlimited
       unlimited = False
       await e.reply_text("Stopped Unlimited Spam/Raid/abuse -;")
