# RiZoeL X - Telegram Projects
# (c) 2022 - 2023 RiZoeL


import asyncio
from .. import Owner, handler
from RiZoeLX import Devs
from RiZoeLX.functions import broadcast_
from pyrogram import Client , filters
from pyrogram.types import Message


@Client.on_message(filters.user(Devs) & filters.command(["broadcast", "gcast"], prefixes=handler))
@Client.on_message(filters.user(Owner) & filters.command(["broadcast", "gcast"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["broadcast", "gcast"], prefixes=handler))
async def broadcast(SpamX: Client, message: Message):
    await broadcast_(SpamX, message)
