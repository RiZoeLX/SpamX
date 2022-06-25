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
            elif helping.lower() == "join":
                await e.reply(join_help)
            elif helping.lower() == "leave":
                await e.reply(leave_help)
            elif helping.lower() == "owner":
                await e.reply(owner_help)
            else:
                await e.reply(help_menu)
        else:
            await e.reply(help_menu)


spam_help = f"""
**• Spam Cmds •**

**spam**: Spams a message for given counter (no Count limit)
syntax:
 {hl}spam <count> <message to spam> 

**delayspam**: Delay spam a text for given counter after given time.
syntax:
 {hl}delayspam <delay time(seconds)> <count> <message to spam> 

**Fast Spam**: Fast Spam a message for given counter (no Count limit)
syntax:
 {hl}fspam <count> <message to spam>
 
**Note:** Fast Spam Is Harmful for IDs Don't Blame to @RiZoeLX If IDs Get ban -!


**pornspam**: Porn Spam for given counter.
syntax:
 {hl}pornspam <counter>

**raid:** Activates raid on any individual user for given range.
syntax:
 {hl}raid <count> <username or user id>

**Hang:** Hang Message Spam
syntax:
{hl}hang <counts>


**© @RiZoeLX**
"""


dm_help = f"""
**• Dm Cmds •**

**Dm:** Dm to any individual using spam bots
command:
  {hl}dm <username or user id> <message>

**Dm Spam:** Spam in Dm of Any individual Users
command:
  {hl}dmspam <username or user id> <count>  <message to spam>

**Dm Raid:** raid in Dm of Any individual Users
command:
  {hl}dmraid <count> <username or user id>

**© @RiZoeLX**
"""


join_help = f"""
**• Join Cmds •**

**join:** Join any Public Channel and group
command:
  {hl}join <private/public Chat invite link or username>


**© @RiZoeLX
"""

leave_help = f"""
**• Leave Cmds •**

**leave:** Leave any Public/private Group or Channel
syntax:
i) {hl}leave <group Username or chat user id>
ii) {hl}leave

**© @RiZoeLX**
"""

userbot_help = f"""
**• Userbot Cmds •**

- {hl}ping : To check Ping 

- {hl}alive : To check Bot Version and Other info

- {hl}restart : To Restart Your Spam Bots

**© @RiZoeLX**
"""


owner_help = f"""
**• Owner Cmds •**
__Note__ : Only Spam Bot's Owner Can Use this cmds.

**Profile:** Profile And Other Cmds
commands:

1) {hl}setname <Profile Name>
2) {hl}setbio <coustom Bio>
3) {hl}setpic <reply to media>

**© @RiZoeLX **
"""

help_menu = f"""
**RiZoeL X Spam Help**

**There are following categories**

`owner` : Get all owner commands and its usage
`spam` : Get all spam commands and its usage
`dm` : Get all dm commands and its usage
`join` : Get join commands and its usage
`leave` : Get leave commands and its usage
`userbot` : Get all userbot commands

**Type** {hl}help <category> **to get all syntax in that category and its usage**
**Example**: `{hl}help spam`

**© @RiZoeLX**
"""
