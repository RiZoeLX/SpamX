from pyrogram import Client, filters 
from pyrogram.types import Message
from config import OWNER_ID, HNDLR
import asyncio

@Client.on_message(filters.user(OWNER_ID) & filters.command(["scrape", "inviteall"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["scrape", "inviteall"], prefixes=HNDLR))
async def inviteall(client: Client, message: Message):
    Msg = await message.reply_text(f"Gime Title also\n ex: {HNDLR}inviteall @chatlink")
    text = message.text.split(" ", 1)
    queryy = text[1]
    chat = await client.get_chat(queryy)
    tgchat = message.chat
    """ Plugin Credits Zaid Userbot """
    await client.join_chat(chat.username)
    await Msg.edit_text(f"inviting users from {chat.username}")
    async for member in client.iter_chat_members(chat.id):
        user= member.user
        zxb= ["online", "offline" , "recently", "within_week"]
        if user.status in zxb:
           try:
            await client.add_chat_members(tgchat.id, user.id)
           except Exception as e:
            mg= await client.send_message("me", f"error-   {e}")
            await asyncio.sleep(0.3)
            await mg.delete()
