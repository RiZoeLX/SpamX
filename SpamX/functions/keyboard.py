from pyrogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

start_keyboard = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton("🔹 Manage Clients 🔹")
        ],
        [
            KeyboardButton("❓Help"),
            KeyboardButton("Other ↗️")
        ]
    ],
    placeholder="Please Select",
    resize_keyboard=True,
)

manage_clients_keyboard = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton("🔸 Get All Clients 🔸")
        ],
        [
            KeyboardButton("➕ Add Client"),
            KeyboardButton("Remove Client ➖")
        ],
        [
            KeyboardButton("🔐 Get Access Of Client")
        ],
        [
            KeyboardButton("Home 🏠")
        ]
    ],
    placeholder="Please Select",
    resize_keyboard=True,
)

other_keyboard = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton("↗️ Join All"),
            KeyboardButton("Leave All ↙️")
        ],
        [
            KeyboardButton("👥 Sudo Users"),
            KeyboardButton("Active Tasks ℹ️")
        ],
        [
            KeyboardButton("🔒 Restrictions")
        ],
        [
            KeyboardButton("Home 🏠")
        ]
    ],
    placeholder="Please Select",
    resize_keyboard=True,
)

sudo_keyboard = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton("🔸 Get All Sudos 🔸")
        ],
        [
            KeyboardButton("➕ Add Sudo"),
            KeyboardButton("Remove Sudo ➖")
        ],
        [
            KeyboardButton("Remove All ☑️")
        ],
        [
            KeyboardButton("🔙")
        ]
    ],
    placeholder="Please Select",
    resize_keyboard=True,
)

restriction_keyboard = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton("🔸 Get All Restricted Chats 🔸")
        ],
        [
            KeyboardButton("➕ Add Chat"),
            KeyboardButton("Remove Chat ➖")
        ],
        [
            KeyboardButton("🔙")
        ]
    ],
    resize_keyboard=True,
)

# --- funcs --- #
def btn(text, value, type="callback_data") -> InlineKeyboardButton:
    return InlineKeyboardButton(text, **{type: value})

def gen_inline_keyboard(collection: list, row: int = 2) -> list[list[InlineKeyboardButton]]:
    keyboard = []
    for i in range(0, len(collection), row):
        kyb = []
        for x in collection[i : i + row]:
            button = btn(*x)
            kyb.append(button)
        keyboard.append(kyb)
    return keyboard

# ---- Inline ---- #
help_buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🔹 Basic", "help:basic"),
            InlineKeyboardButton("Spam 🔹", "help:spam")
        ],
        [
            InlineKeyboardButton("🔹 DirectMessage (DM)", "help:direct"),
            InlineKeyboardButton("Raid 🔹", "help:Raid")
        ],
        [
            InlineKeyboardButton("🔹 Profile", "help:profile"),
            InlineKeyboardButton("Extra 🔹", "help:extra")
        ],
        [
            InlineKeyboardButton("🗑️", "client:close")
        ]
    ]
)

reboot_button = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Reboot 🔄", "help:reboot")
        ]
    ]
)