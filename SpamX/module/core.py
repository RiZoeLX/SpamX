from . import TheSpamX

from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(
    filters.command(["gcast", "broadcast"], prefixes=TheSpamX.handler)
)
async def broadcast(SpamX: Client, message: Message):
    if await TheSpamX.sudo.sudoFilter(message, 1):
        return

    await TheSpamX.functions.broadcast(SpamX, message)

@Client.on_message(
    filters.command('join', prefixes=TheSpamX.handler)
)
async def join(SpamX: Client, message: Message):
    try:
        group = str(message.command[1])
    except:
        await message.reply("__Please give valid join link or username of group to join.__")
        return

    wait = await message.reply("__joining.....__")
    try:
        await SpamX.join_chat(group)
        await message.reply("**✅ Joined successfully**")
    except Exception as er:
        await message.reply(f"**Error while join:** {str(er)} \n\n__Report in @{TheSpamX.supportGroup}__")
    await wait.delete()

@Client.on_message(
    filters.command(["leave", "left"], prefixes=TheSpamX.handler)
)
async def leave(SpamX: Client, message: Message):
    if len(message.command) == 1:
        group = message.chat.id
    else:
        try:
            group = message.command[1]
        except:
            await message.reply("__Please give valid join link or username of group to join.__")
            return

    if group in [TheSpamX.restrict.res, f"@{TheSpamX.supportGroup}", f"@{TheSpamX.updateChannel}", TheSpamX.supportGroup, TheSpamX.updateChannel]:
        return

    wait = await message.reply("__leaving.....__")
    try:
        await SpamX.join_chat(group)
        await message.reply("**✅ Left successfully**")
    except Exception as er:
        await message.reply(f"**Error while Leave:** {str(er)} \n\n__Report in @{TheSpamX.supportGroup}__")
    await wait.delete() 