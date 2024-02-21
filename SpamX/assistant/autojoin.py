
from pyrogram import Client, filters
from pyrogram.types import Message, ReplyKeyboardRemove

from . import TheSpamX

@Client.on_message(
    filters.regex("↗️ Join All") & filters.private #& filters.user(TheSpamX.sudo.sudoUsers)
)
async def join_all(client: Client, message: Message):
    if await TheSpamX.sudo.sudoFilter(message):
        return
    if len(TheSpamX.clients) == 0:
        await message.reply("__❎ You have 0 clients__")
        return
    chat: Message = await client.ask(
        message.from_user.id,
        "**❓ Share the username or invite link of chat where you want to join with all clients!**",
        filters=filters.text,
        timeout=120,
        reply_markup=ReplyKeyboardRemove(),
    )
    if chat.text.startswith("/") or " " in chat.text:
        await chat.reply("__Process cancelled__")
        return
    wait = await message.reply("__processing__")
    if "+" in chat.text and (chat.text.startswith("https://t.me") or chat.text.startswith("t.me")):
        join_link = str(chat.text)
    else:
        if chat.text.startswith("https://t.me") or chat.text.startswith("t.me"):
            join_link = str(chat.text.split("t.me")[1])
        else:
            join_link = str(chat.text)

    joined = 0
    group = None
    for client in TheSpamX.clients:
        try:
            group = await client.join_chat(join_link)
            joined += 1
        except:
            continue
    if group:
        Text = f"__✅ Joined by {joined} clients in {group.title} ({group.id})__"
    else:
        Text = f"__✅ Joined by {joined} clients in {join_link}__"
    await message.reply(Text, disable_web_page_preview=True)
    await wait.delete()

@Client.on_message(
    filters.regex("Leave All ↙️") & filters.private #& filters.user(TheSpamX.sudo.sudoUsers)
)
async def leave_all(client: Client, message: Message):
    if await TheSpamX.sudo.sudoFilter(message):
        return
    if len(TheSpamX.clients) == 0:
        await message.reply("__❎ You have 0 clients__")
        return
    chat: Message = await client.ask(
        message.from_user.id,
        "**❓ Share the username or Chat ID of chat where you want to Leave with all clients!**",
        filters=filters.text,
        timeout=120,
        reply_markup=ReplyKeyboardRemove(),
    )
    if chat.text.startswith("/") or " " in chat.text:
        await chat.reply("__Process cancelled__")
        return
    wait = await message.reply("__processing__")
    if "+" in chat.text and (chat.text.startswith("https://t.me") or chat.text.startswith("t.me")):
        await message.reply("__Please provide chat ID of chat!__")
        return
    else:
        if chat.text.startswith("https://t.me") or chat.text.startswith("t.me"):
            leave_chat = str(chat.text.split("t.me")[1])
        else:
            leave_chat = str(chat.text)

    leaved = 0
    for client in TheSpamX.clients:
        try:
            await client.leave_chat(leave_chat)
            leaved += 1
        except:
            continue
    Text = f"__✅ {leave_chat} Leaved by {leaved} clients__"
    await message.reply(Text, disable_web_page_preview=True)
    await wait.delete()