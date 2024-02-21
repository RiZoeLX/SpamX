from . import TheSpamX

from pyrogram import Client, filters
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from SpamX.functions.messages import helpMessages
from SpamX.functions.keyboard import help_buttons

@Client.on_callback_query(filters.regex("help:.*$"))
async def helpCallbacks(_, callback: CallbackQuery):
    query = str(callback.data.lower().split(":")[1])

    if query == "reboot":
        await callback.answer("Rebooting SpamX.....", show_alert=True)
        await callback.message.edit("__🔸 Rebooting SpamX.....__")
        await TheSpamX.reboot()

    elif query == "spam":
        await callback.message.edit(
            helpMessages.spam.format(TheSpamX.handler, TheSpamX.supportGroup),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔙", "help:back")
                    ]
                ]
            )
        )

    elif query == "raid":
        await callback.message.edit(
            helpMessages.raid.format(TheSpamX.handler, TheSpamX.supportGroup),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔙", "help:back")
                    ]
                ]
            )
        )

    elif query == "direct":
        await callback.message.edit(
            helpMessages.direct_message.format(TheSpamX.handler, TheSpamX.supportGroup),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔙", "help:back")
                    ]
                ]
            )
        )

    elif query == "basic":
        await callback.message.edit(
            helpMessages.basic.format(TheSpamX.handler, TheSpamX.supportGroup),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔙", "help:back")
                    ]
                ]
            )
        )

    elif query == "profile":
        await callback.message.edit(
            helpMessages.profile.format(TheSpamX.handler, TheSpamX.supportGroup),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔙", "help:back")
                    ]
                ]
            )
        )

    elif query == "extra":
        await callback.message.edit(
            helpMessages.extra.format(TheSpamX.handler, TheSpamX.supportGroup),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔙", "help:back")
                    ]
                ]
            )
        )

    elif query == "back":
        await callback.message.edit(
            helpMessages.start.format(TheSpamX.handler, TheSpamX.updateChannel, TheSpamX.supportGroup),
            reply_markup=help_buttons,
        )