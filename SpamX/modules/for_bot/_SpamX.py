""" RiZoeLX 2022 © SpamX """

import os, sys, io
from io import StringIO
from .. import Owner, Sudos, handler
from pyrogram import Client, filters
from pyrogram.types import Message

from SpamX.core import user_errors 
from SpamX.core.help_strings import *
from RiZoeLX.functions import user_only, delete_reply
from telegraph import Telegraph, exceptions, upload_file


@Client.on_message(filters.user(Sudos) & filters.command(["eval"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["eval"], prefixes=handler))
def _eval(SpamX: Client, message: Message):
    if message.reply_to_message:
       msg = message.reply_to_message.text.markdown
    else:
       try:
           code = message.text.split(" ", maxsplit=1)[1]
           if not code:
              message.reply_text("Gime code!")
              return
       except IndexError:
           try:
              code = message.text.split(" \n", maxsplit=1)[1]
              if not code:
                 message.reply_text("Gime code!")
                 return
           except IndexError:
              pass

    result = sys.stdout = StringIO()
    try:
        exec(code)

        message.reply_text(
            f"<b>Code:</b>\n"
            f"<code>{code}</code>\n\n"
            f"<b>Result</b>:\n"
            f"<code>{result.getvalue()}</code>"
        )
    except:
        message.reply_text(
            f"<b>Code:</b>\n"
            f"<code>{code}</code>\n\n"
            f"<b>Result</b>:\n"
            f"<code>{sys.exc_info()[0].__name__}: {sys.exc_info()[1]}</code>"
        )

telegraph = Telegraph()
r = telegraph.create_account(short_name="telegram")
auth_url = r["auth_url"]

def get_text(message: Message) -> [None, str]:
    """Extract Text From Commands"""
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None

@Client.on_message(filters.user(Sudos) & filters.command(["tg", "telegraph", "tm", "tgt"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["tg", "telegraph", "tm", "tgt"], prefixes=handler))
async def _telegraph(SpamX: Client, message: Message):
    hm = await message.reply_text("`Processing . . .`")
    if not message.reply_to_message:
        await tex.edit("**Reply to an Image or text.**")
        return
    if message.reply_to_message.media:
        doc = await message.reply_to_message.download()
        try:
            media_url = upload_file(doc)
        except exceptions.TelegraphException as exc:
            await delete_reply(message, hm, f"**ERROR:** `{exc}`")
            os.remove(doc)
            return
        await delete_reply(message, hm, f"**Uploaded on ** [Telegraph](https://telegra.ph/{media_url[0]})")
        os.remove(doc)
    elif message.reply_to_message.text:
        _title = get_text(message) if get_text(message) else SpamX.me.first_name
        _text = message.reply_to_message.text
        _text = _text.replace("\n", "<br>")
        try:
            response = telegraph.create_page(_title, html_content=_text)
        except exceptions.TelegraphException as exc:
            await delete_reply(message, hm, f"**ERROR:** `{exc}`")
            return
        await delete_reply(message, hm, f"**Uploaded as** [Telegraph](https://telegra.ph/{response['path']})")

@Client.on_message(filters.user(Sudos) & filters.command(["help"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["help"], prefixes=handler))
async def help_(_, message: Message):
   try:
       string = message.text.split(" ", maxsplit=1)[1]
   except:
       await message.reply_text(help_text)
       return 
   help_message = await help_return(string)
   await message.reply_text(str(help_message))
