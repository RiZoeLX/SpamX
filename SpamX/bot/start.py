
import os
import sys
import asyncio
from SpamX import (SUDO_USERS, OWNER_ID, ALIVE_PIC)
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup


Pic = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/ec832fc9107fd21edfee3.jpg"
Hn = "/"
btn = InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton(
                        "• Channel •", url="https://t.me/RiZoeLX"),
                    InlineKeyboardButton(
                        "• Support •", url="https://t.me/DNHxHELL")
                ], [
                    InlineKeyboardButton(
                        "• Repo •", url="https://github.com/RiZoeLX/SpamX")
                ]]
            )
 
                   
@Client.on_message(filters.private & filters.incoming & filters.command(['start'], prefixes=Hn))
async def _start(_, ok: Message):
    msg = f"**Hello [{ok.from_user.first_name}](tg://user?id={ok.from_user.id}) !** \n\n __ • I'm SpamX An Advance Spambot__ \n\n **Click Below Buttons for More Info**"           
    if ".jpg" in Pic or ".png" in Pic:
              await ok.reply_photo(Pic, caption=msg, reply_markup=btn)
    if ".mp4" in Pic or ".MP4," in Pic:
              await ok.reply_video(Pic, caption=msg, reply_markup=btn)
