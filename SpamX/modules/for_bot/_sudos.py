import os, sys
from .. import handler, Owner, Sudos, DATABASE_URL
from SpamX import sudoser
from pyrogram import Client, filters
from pyrogram.types import Message
from RiZoeLX import Devs
from SpamX.database import users_db
from RiZoeLX.functions import get_user


@Client.on_message(filters.user(Owner) & filters.command(["addsudo"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["addsudo"], prefixes=handler))
async def rmsudo(SpamX: Client, message: Message):
    try:
       user = await get_user(SpamX, message)
    except Exception as er:
       await message.reply(user_errors(er))
       return
    if int(user.id) == Owner or int(user.id) in Devs:
       await message.reply_text("🙂🙂")
       return
    if DATABASE_URL:
       check = users_db.check_sudo(user.id)
       if check:
          await message.reply_text(f"User {user.mention} already in sudo list!")
          return
       users_db.addsudo(user.id)
       await message.reply_text(f"User {user.mention} successfully promoted as Sudo! \n\nWait for re-start ✓")
       args = [sys.executable, "-m", "SpamX"]
       os.execl(sys.executable, *args)
       quit()
    else:
       if int(user.id) in Sudos:
          await message.reply_text(f"User {user.mention} already in sudo list!")
          return
       Sudos.append(user.id)
       await message.reply_text(f"User {user.mention} successfully promoted as Sudo! \n\n**NOTE:**You didn't filled `DATABASE_URL`")

@Client.on_message(filters.user(Owner) & filters.command(["rmsudo"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["rmsudo"], prefixes=handler))
async def addsudo(SpamX: Client, message: Message):
    try:
       user = await get_user(SpamX, message)
    except Exception as er:
       await message.reply(user_errors(er))
       return
    if int(user.id) == Owner or int(user.id) in Devs:
       await message.reply_text("🙂🙂")
       return
    if DATABASE_URL:
       check = users_db.check_sudo(user.id)
       if not check:
          await message.reply_text(f"User {user.mention} not in sudo list!")
          return
       users_db.rmsudo(user.id)
       await message.reply_text(f"User {user.mention} successfully removed from Sudo! \n\nWait for re-start ✓")
       args = [sys.executable, "-m", "SpamX"]
       os.execl(sys.executable, *args)
       quit()
    else:
       if int(user.id) not in Sudos:
          await message.reply_text(f"User {user.mention} not in sudo list!")
          return
       Sudos.remove(user.id)
       await message.reply_text(f"User {user.mention} successfully removed from Sudo! \n\n**NOTE:** You didn't filled `DATABASE_URL`")

@Client.on_message(filters.user(Sudos) & filters.command(["sudos", "sudolist"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["sudos", "sudolist"], prefixes=handler))
async def sudolist(SpamX: Client, message: Message):
    sudo_reply = "**Sudo users list - SpamX** \n\n"
    if DATABASE_URL:
       data = users_db.get_all_sudos()
       for x in data:
          try:
             user = await SpamX.get_users(x.user_id)
             sudo_reply += f" × {user.mention} \n"
          except:
             sudo_reply += f" × [{x.user_id}](tg://user?id={x.user_id}) \n"
    else:
       for x in Sudos:
          try:
             user = await SpamX.get_users(x)
             sudo_reply += f" × {user.mention} \n"
          except:
             sudo_reply += f" × [{x}](tg://user?id={x}) \n"
    await message.reply_text(sudo_reply)
