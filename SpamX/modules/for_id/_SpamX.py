""" RiZoeLX 2022 © SpamX """

import os, sys, io, random
from io import StringIO
from .. import Owner, Sudos, handler
from pyrogram import Client, filters
from pyrogram.types import Message

from SpamX import AUTO_REACT, EMOJI_LIST
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

FName = ""
LName = ""
Bio = ""

@Client.on_message(filters.user(Sudos) & filters.command(["clone"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["clone"], prefixes=handler))
async def clone_user(SpamX: Client, message: Message):
    global FName 
    global LName
    global Bio
    try:
       user = await user_only(SpamX, message, Owner, Sudos)
       if not user:
          return 
    except Exception as er:
       await message.reply(user_errors(er))
       return
    Mai = await SpamX.get_me()
    FName = Mai.first_name
    if Mai.last_name:
       LName = Mai.last_name
    siu = await SpamX.get_chat("me")
    if siu.bio:
       Bio = siu.bio
    Reply = await message.reply("cloning...")
    _bio = await SpamX.get_chat(user.id)
    if _bio.bio:
       user_bio = _bio.bio
    else:
       user_bio = None
    pic = await SpamX.download_media(user.photo.big_file_id)
    try:
       await SpamX.set_profile_photo(photo=pic)
       if user.last_name:
          await SpamX.update_profile(first_name=user.first_name, last_name=user.last_name, bio=user_bio)
       else:
          await SpamX.update_profile(first_name=user.first_name, bio=user_bio)
       await delete_reply(message, Reply, f"Now I'm {user.first_name} \n\n Note: Don't restart until you revert me!")
    except Exception as eror:
       await delete_reply(message, Reply, str(eror))

@Client.on_message(filters.user(Sudos) & filters.command(["revert"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["revert"], prefixes=handler))
async def _revert(SpamX: Client, message: Message):
    global FName 
    global LName
    global Bio
    Mai = await SpamX.get_me()
    photos = [x async for x in SpamX.get_chat_photos("me")]
    if not FName:
       await message.reply(f"Error: You didn't cloned anyone!")
       return
    user_bio = Bio
    if not user_bio:
       user_bio = "SpamX user!"
    Reply = await message.reply("reverting...")
    try:
       if LName:
          await SpamX.update_profile(first_name=FName, last_name=LName, bio=user_bio)
       else:
          await SpamX.update_profile(first_name=FName, bio=user_bio)
       await SpamX.delete_profile_photos(photos[0].file_id)
       await delete_reply(message, Reply, f"I'm Back!")
       FName = ""
       LName = ""
       Bio = ""
    except Exception as eror:
       await delete_reply(message, Reply, str(eror))


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
        await hm.edit("**Reply to an Image or text.**")
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

@Client.on_message(filters.chat(AUTO_REACT) & filters.all)
async def auto_react(_, message: Message):
   emoj = random.choice(EMOJI_LIST)
   await message.react(emoji=emoj, big=True)
