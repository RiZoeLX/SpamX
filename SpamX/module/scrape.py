from pyrogram import Client, filters 
from pyrogram.types import Message
from SpamX import OWNER_ID, HNDLR
import asyncio

@Client.on_message(filters.user(OWNER_ID) & filters.command(["scrape", "inviteall"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["scrape", "inviteall"], prefixes=HNDLR))
async def scrape_members(SpamX: Client, message: Message):
   txt = "".join(message.text.split(maxsplit=1)[1:]).split(" ", 1)
   if message.chat.id == e.from_user.id:
     await message.reply_text("Use this CMD in group;")
     return
   if txt:
      xchat = str(txt[0])
      try:
         cht = await SpamX.get_chat(xchat)
         await SpamX.join_chat(cht.username)
      except Exception as a:
         return await message.reply_text(str(a))
      await message.reply_text(f"inviting users from @{cht.username}")
      added = 0
      async for x in SpamX.get_chat_members(cht.id):
        user = x.user.id
        try:
           await SpamX.add_chat_members(message.chat.id, user)
           added += 1
           await asyncio.sleep(2)
        except Exception as a:
           print(str(a))
      return await Spamx.send_message(message.chat.id, f"**Users Added!** \nFrom chat: @{cht.username} \nTotal users added: `{added}` \n\n © @RiZoeLX")
   else:
      await message.reply_text(f"**Wrong usage** \n syntax: {HNDLR}scrape @chatlink")
