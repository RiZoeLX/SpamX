# RiZoeL X - Telegram Projects
# (c) 2022 - 2023 RiZoeL
# Don't Kang Bitch -!




import os
import sys
from random import choice
from SpamX import (OWNER_ID, HNDLR, SUDO_USERS, hl)
from pyrogram import Client, filters
from pyrogram.types import Message
from SpamX.data import *



@Client.on_message(filters.user(SUDO_USERS) & filters.command(["help"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["help"], prefixes=HNDLR))
async def help(_, e: Message):
        RiZoeL = e.text.split(" ")
        if len(RiZoeL) > 1:
            helping = RiZoeL[1]
            if helping.lower() == "spam":
                await e.reply(spam_help)
            elif helping.lower() == "dm":
                await e.reply(dm_help)
            elif helping.lower() == "userbot":
                await e.reply(userbot_help)
            elif helping.lower() == "leave":
                await e.reply(leave_help)
            elif helping.lower() == "extra":
                await e.reply(extra_help)
            else:
                await e.reply(help_menu)
        else:
            await e.reply(help_menu)


spam_help = f"""
**• Spam Cmds •**

**spam**: Spams a message for given counter (no Count limit)
syntax:
 {hl}spam (count) (message to spam)
 {hl}delayspam (delay time In seconds) (count) (message to spam) 
 {hl}fspam (count) (message to spam)
 {hl}pornspam (count)
 {hl}ispam (count) (username or reply to user)

**raid:** Activates raid on any individual user for given range.
syntax:
 {hl}raid (count) (username or user id)
 {hl}replyraid (username or reply to user)
 {hl}dreplyraid (username or reply to user)
 
**Hang:** Hang Message Spam
syntax:
{hl}hang (counts)


**© @jelibonvsp**
"""


dm_help = f"""
**• Dm Cmds •**

**Dm:** Dm to any individual using spam bots
command:
  {hl}dm (username or user id) (message)

**Dm Spam:** Spam in Dm of Any individual Users
command:
  {hl}dmspam (username or user id) (count)  (message to spam)

**Dm Raid:** raid in Dm of Any individual Users
command:
  {hl}dmraid (count) (username or user id)

**© @jelibonvsp**
"""

leave_help = f"""
**• Leave Cmds •**

**leave:** Leave any Public/private Group or Channel
syntax:
i) {hl}leave group Username or chat user id
ii) {hl}leave

**© @jelibonvsp**
"""

userbot_help = f"""
**• Userbot Cmds •**

- {hl}ping : To check Ping 

- {hl}alive : To check Bot Version and Other info

- {hl}restart : To Restart Your Spam Bots

**© @jelibonvsp**
"""

help_menu = f"""
**SpamX Help Menu **

**There are following categories**

`owner` : Get all owner commands and its usage
`spam` : Get all spam commands and its usage
`dm` : Get all dm commands and its usage
`join` : Get join commands and its usage
`leave` : Get leave commands and its usage
`userbot` : Get all userbot commands
`extra` : Get all extra Cmds 

**Type** {hl}help (category) **to get all syntax in that category and its usage**
**Example**: `{hl}help spam`

**© @jelibonvsp**
"""


extra_help = f"""
**• Unlimited Cmds •**

**Unlimited spam**
syntax:
 {hl}uspam (message to spam)

**Unlimited raid**
syntax:
 {hl}uraid (username or user id / reply to user)

**Abuse / One Word**
syntax:
  {hl}absue (counts)

  **Read**: if you want unlimited abuse simply type {hl}abuse -!

**stop cmd**: Simply type {hl}stop to stop spam/abuse/raid any of that 

**© @jelibonvsp**
"""
