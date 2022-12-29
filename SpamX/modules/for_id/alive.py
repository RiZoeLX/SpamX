""" © RiZoeLX 2022 - 2023
   (\_/)
   ( • .•)
   />❤️ 
"""
import os, sys, asyncio, psutil, cpuinfo, platform
from .. import Sudos, handler, Alive, __version__, Owner, DATABASE_URL
from pyrogram import Client, filters
from pyrogram.types import Message
from SpamX.database import users_db, raid_db, gban_db

from pyrogram import __version__ as pyrogram_vr
from RiZoeLX import Devs, __version__ as rizoelx_vr


@Client.on_message(filters.user(Sudos) & filters.command(["alive"], prefixes=handler))
async def alive(SpamX: Client, message: Message):       
    if ".jpg" in Alive.Pic or ".png" in Alive.Pic:
       await SpamX.send_photo(
             message.chat.id, 
             Alive.Pic, 
             caption=Alive.msg)
    if ".mp4" in Alive.Pic or ".MP4," in Alive.Pic:
       await SpamX.send_video(message.chat.id, 
             Alive.Pic, 
             caption=Alive.msg)

      
@Client.on_message(filters.me & filters.command(["alive"], prefixes=handler))
async def alive_me(SpamX: Client, message: Message):       
    await message.delete()
    if ".jpg" in Alive.Pic or ".png" in Alive.Pic:
       await SpamX.send_photo(
             message.chat.id, 
             Alive.Pic, 
             caption=Alive.msg)
    if ".mp4" in Alive.Pic or ".MP4," in Alive.Pic:
       await SpamX.send_video(message.chat.id, 
             Alive.Pic, 
             caption=Alive.msg)


@Client.on_message(filters.user(Sudos) & filters.command(["SpamX", "Spamx", "spamx"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["SpamX", "Spamx", "spamx"], prefixes=handler))
async def SpamX_(SpamX: Client, message: Message):
    user = message.from_user
    Mai = await SpamX.get_me()
    chat = message.chat
    info = await message.reply_text("processing......")
    spamx_reply = "**__SpamX by RiZoeLX;__** \n\n"
    spamx_reply += "<=======================> \n"

    try:
        diskTotal = int(psutil.disk_usage('/').total / (1024 * 1024 * 1024))
        diskUsed = int(psutil.disk_usage('/').used / (1024 * 1024 * 1024))
        diskPercent = psutil.disk_usage('/').percent
        disk = f"{diskUsed}GB / {diskTotal}GB ({diskPercent}%)"
    except:
        disk = "Unknown"
    spamx_reply += f"**Disk:** {disk} \n"

    try:
        ramTotal = int(psutil.virtual_memory().total / (1024 * 1024))
        ramUsage = int(psutil.virtual_memory().used / (1024 * 1024))
        ramUsagePercent = psutil.virtual_memory().percent
        ram = f"{ramUsage}MB / {ramTotal} MB ({ramUsagePercent}%)"
    except:
        ram = "Unknown"
    spamx_reply += f"**Ram:** {ram} \n"

    try:
        cpuInfo = cpuinfo.get_cpu_info()['brand_raw']
        cpuUsage = psutil.cpu_percent(interval=1)
        cpu = f"{cpuInfo} ({cpuUsage}%)"
    except:
        cpu = "Unknown"
    spamx_reply += f"**CPU:** {cpu} \n"

    try:
        os = f"{platform.system()} - {platform.release()} ({platform.machine()})"
    except:
        os = "Unknown"
    spamx_reply += f"**OS:** {os} \n"
    
    try:
        battery = f"{int(psutil.sensors_battery().percent)}%"
    except:
        battery = f"Unknown"
    spamx_reply += f"**Battery:** {battery} \n\n"
    await info.edit_text("..!......")

    spamx_reply += f"**SpamX Version:** `{__version__}` \n"
    spamx_reply += f"**Python Version:** `{platform.python_version()}` \n"
    spamx_reply += f"**pyRiZoeLX Version:** `{rizoelx_vr}` \n"
    spamx_reply += f"**Pyrogram Version:** `{pyrogram_vr}` \n\n"
    
    spamx_reply += f"**Your Name:** {user.first_name} \n"
    spamx_reply += f"**Your ID:** `{user.id}` \n"
    if user.id in Devs:
       spamx_reply += f"**Rank:** Dev of SpamX \n"
    elif user.id == Owner or user.id == Mai.id:
       spamx_reply += f"**Rank:** Owner 🔱 \n"
    else:
       spamx_reply += f"**Rank** Sudo ⚜️\n\n"
    if DATABASE_URL:
       spamx_reply += f"**Total Sudos:** `{users_db.sudo_count()}` \n"
       spamx_reply += f"**Total Gbanned users:** `{gban_db.gban_count()}` \n"
    spamx_reply += "<=======================> \n\n"
    spamx_reply += "**Source Code:** [GitHub 🐈‍⬛](https://github.com/RiZoeLX/SpamX) \n\n"
    spamx_reply += "**© @RiZoeLX** || Support: @DNHxHELL"
    
    try:
       await info.edit_text(spamx_reply, disable_web_page_preview=True)
    except:
       await info.delete()
       await message.reply_text(spamx_reply, disable_web_page_preview=True)
