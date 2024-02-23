import os
import time

from pyrogram import Client, filters
from pyrogram.types import (
    Message,
    CallbackQuery,
    KeyboardButton,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from pyrogram.errors import UserIdInvalid, UsernameInvalid, PeerIdInvalid

from . import TheSpamX
from SpamX.functions.keyboard import gen_inline_keyboard

@Client.on_message(
    filters.regex("🔸 Get All Sudos 🔸") & filters.private #& filters.user(TheSpamX.sudo.sudoUsers)
)
async def get_all_sudos(_, message: Message):
    if await TheSpamX.sudo.sudoFilter(message, 2):
        return
    wait = await message.reply("__processing__")
    collection = []
    for sudo_user_id in TheSpamX.sudo.sudoUsers:
        try:
            sudo_ = await TheSpamX.SpamX.get_users(int(sudo_user_id))
            sudo_name = sudo_.first_name
        except:
            sudo_name = f"ID: {sudo_user_id}"
        collection.append((sudo_name, f"sudo:details:{sudo_user_id}"))

    buttons = gen_inline_keyboard(collection, 2)
    try:
        await wait.edit(
            "**🔸 Choose sudo to get more details:**",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    except:
        await wait.reply_text(
            "**🔸 Choose sudo to get more details:**",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
        await wait.delete()

@Client.on_message(
    filters.regex("➕ Add Sudo") & filters.private #& filters.user(TheSpamX.sudo.sudoUsers)
)
async def add_sudo_user(RiZoeL: Client, message: Message):
    if await TheSpamX.sudo.sudoFilter(message, 1):
        return
    sudo_message: Message = await RiZoeL.ask(
        message.from_user.id,
        "**❓ Please share user ID or username of sudo user!** __type /cancel to cancel the process!__",
        filters=filters.text,
        timeout=180,
        reply_markup=ReplyKeyboardRemove(),
    )
    if sudo_message.text.startswith("/"):
        await sudo_message.reply("**Process cancelled ❌**")
        return
    if sudo_message.text.isnumeric() or sudo_message.text.startswith("@"):
        try:
            sudo_user = await RiZoeL.get_users(sudo_message.text)
        except UsernameInvalid:
            await sudo_message.reply(f"User - {sudo_message.text} is Invalid username")
            return
        except (UserIdInvalid, PeerIdInvalid):
            await sudo_message.reply("User ID invalid or not meet yet! please tell them to start me!")
            return
        except Exception as Error:
            await sudo_message.reply(f"**Unknown Error:** {str(Error)} \n\n__Report in @{TheSpamX.supportGroup}__")
            return

        ask_rank: Message = await RiZoeL.ask(
            message.from_user.id,
            f"**❓ Please select sudo-rank for {sudo_user.mention}**\n\n **Sudo - Rank details**\n\n __1: Dev - Hold all rights. \n 2: Celestia - These users can access and verify data, as well as utilize SpamX Spam Bots. \n 3: Apex - These users can only utilize SpamX Spam Bots.__",
            filters=filters.text,
            timeout=120,
            reply_markup=ReplyKeyboardMarkup(
                [
                    [
                        KeyboardButton("1: Dev"),
                        KeyboardButton("2: Celestia"),
                        KeyboardButton("3: Apex"),
                    ]
                ],
                placeholder="Please select rank",
                resize_keyboard=True,
            )
        )
        if ask_rank.text in ["1: Dev", "2: Celestia", "3: Apex"]:
            rank = int(ask_rank.text.split(":")[0])
            await TheSpamX.sudo.add(message, sudo_user.id, rank)
        else:
            await ask_rank.reply("**❎ Invalid rank**")
    else:
        await sudo_message.reply("**❕Please provide user ID or Username**")

@Client.on_message(
    filters.regex("Remove Sudo ➖") & filters.private #& filters.user(TheSpamX.sudo.sudoUsers)
)
async def remove_sudo_user(RiZoeL: Client, message: Message):
    if TheSpamX.sudo.sudoFilter(message, 1):
        return
    sudo_message: Message = await RiZoeL.ask(
        message.from_user.id,
        "**❓ Please share user ID or username of sudo user!** __type /cancel to cancel the process!__",
        filters=filters.text,
        timeout=180,
        reply_markup=ReplyKeyboardRemove(),
    )
    if sudo_message.text.startswith("/"):
        await sudo_message.reply("**Process cancelled!**")
        return
    if sudo_message.text.isnumeric() or sudo_message.text.startswith("@"):
        try:
            sudo_user = await RiZoeL.get_users(sudo_message.text)
        except UsernameInvalid:
            await sudo_message.reply(f"User - {sudo_message.text} is Invalid username")
            return
        except (UserIdInvalid, PeerIdInvalid):
            await sudo_message.reply("User ID invalid or not meet yet! please tell them to start me!")
            return
        except Exception as Error:
            await sudo_message.reply(f"**Unknown Error:** {str(Error)} \n\n__Report in @{TheSpamX.supportGroup}__")
            return

        await TheSpamX.sudo.remove(message, sudo_user.id)
    else:
        await sudo_message.reply("**❕Please provide user ID or Username**")

@Client.on_message(
    filters.regex("Remove All ☑️") & filters.private #& filters.user(TheSpamX.sudo.sudoUsers)
)
async def remove_all_sudo_user(RiZoeL: Client, message: Message):
    if message.from_user.id != TheSpamX.owner_id:
        await message.reply("__Only owner can do that!__")
        return
    confirm_message: Message = await RiZoeL.ask(
        message.from_user.id,
        "**Please confirm that you want to Remove all sudo users**",
        filters=filters.text,
        timeout=180,
        reply_markup=ReplyKeyboardMarkup(
            [
                [
                    KeyboardButton("Yes"),
                    KeyboardButton("No"),
                ]
            ],
            placeholder="Please confirm",
            resize_keyboard=True,
        )
    )
    if confirm_message.text.lower() in ["yes", "no"]:
        if confirm_message.text.lower() == "yes":
            wait_message = await confirm_message.reply("__processing__", reply_markup=ReplyKeyboardRemove())
            removed = 0
            for sudo_user_id in TheSpamX.sudo.sudoUsers:
                await TheSpamX.sudo.remove(confirm_message, int(sudo_user_id))
                removed += 1
            try:
                await wait_message.edit(f"**Removed all {removed} sudo users from DB**")
            except:
                await wait_message.reply(f"**Removed all {removed} sudo users from DB**")
                await wait_message.delete()
        else:
            await confirm_message.reply("**Okay! Rejected**", reply_markup=ReplyKeyboardRemove())

@Client.on_callback_query(filters.regex("sudo:.*$"))
async def sudoCallbacks(RiZoeL: Client, callback: CallbackQuery):
    query = callback.data.split(":")

    if query[1] == "back":
        await callback.answer("processing....")
        collection = []
        for sudo_user_id in TheSpamX.sudo.sudoUsers:
            try:
                sudo_ = await TheSpamX.SpamX.get_users(int(sudo_user_id))
                sudo_name = sudo_.first_name
            except:
                sudo_name = f"ID: {sudo_user_id}"
            collection.append((sudo_name, f"sudo:details:{sudo_user_id}"))

        buttons = gen_inline_keyboard(collection, 2)
        try:
            await callback.message.edit(
                "**🔸 Choose sudo to get more details:**",
                reply_markup=InlineKeyboardMarkup(buttons),
            )
        except:
            await callback.message.reply_text(
                "**🔸 Choose sudo to get more details:**",
                reply_markup=InlineKeyboardMarkup(buttons),
            )
            await callback.message.delete()

    elif query[1] == "details":
        if int(query[2]) == TheSpamX.owner_id:
            await callback.answer("He is the owner of these Bots!", show_alert=True)
            return
        await callback.answer("processing....")
        sudo_details = "**Sudo Details** \n\n"
        try:
            user = await RiZoeL.get_users(int(query[2]))
            sudo_details += f" **- Name:** {user.mention} \n"
            sudo_details += f" **- UserID:** `{user.id}` \n"
            if user.username:
                sudo_details += f" **- UserName:** @{user.username} \n"
        except Exception:
            sudo_details += f" **- UserID:** `{query[2]}` \n"
        rank = TheSpamX.sudo.sudos.get(int(query[2]))
        sudo_details += f" **- SudoRank: {rank} ({TheSpamX.sudo.rankNames[rank]}) \n"

        promoted_by = TheSpamX.database.getSudo(int(query[2]))
        if promoted_by["promoted_by"]:
            sudo_details += "\n"
            try:
                p_user = await RiZoeL.get_users(promoted_by["promoted_by"])
                sudo_details += f" **- Promoted By:** {p_user.mention} \n"
                sudo_details += f" **- Promoter UserID:** `{p_user.id}` \n"
                if user.username:
                    sudo_details += f" **- Promoter UserName:** @{p_user.username} \n"
            except Exception:
                sudo_details += f" **- Promoted By:** `{promoted_by['promoted_by']}`"

        button = [[InlineKeyboardButton("🔙", "sudo:back")]]
        try:
            await callback.message.edit(
                sudo_details,
                reply_markup=InlineKeyboardMarkup(button),
            )
        except:
            await callback.message.reply_text(
                sudo_details,
                reply_markup=InlineKeyboardMarkup(button),
            )
            await callback.message.delete()

@Client.on_message(
    filters.regex("Active Tasks ℹ️") & filters.private #& filters.user(TheSpamX.sudo.sudoUsers)
)
async def active_tasks(RiZoeL: Client, message: Message):
    if await TheSpamX.sudo.sudoFilter(message, 2):
        return
    wait = await message.reply("▪ wait while get all active task.....")
    if len(TheSpamX.activeTasks) == 0:
        active_message = None
    else:
        active_message = "🔹 All Active Task 🔹\n\n"
        active = 0
        for task_id in TheSpamX.activeTasks:
            active_task = TheSpamX.activeTasks.get(task_id)
            active += 1
            if active_task['task'] in ['porn', 'loop', 'spam', 'delay', 'multiraid']:
                active_message += f"  {active}) Active ID: {active_task['chat_id']} \n\n"
                active_message += f"      - Chat ID: {active_task['chat_id']}\n"
                active_message += f"      - Task: {active_task['task']}\n"
                active_message += f"      - Started By: {active_task['started_by']}\n"
                active_message += f"      - Counts: {active_task['counts']}\n"
                active_message += f"      - Message Link: {active_task['message_link']}\n\n"

            elif active_task['task'] in ['commanspam', 'dmraid', 'dmspam']:
                user = active_task['user']
                active_message += f"  {active}) Active ID: {user.id} \n\n"
                active_message += f"      - User's Name: {user.first_name}\n"
                active_message += f"      - User's ID: {user.id}\n"
                active_message += f"      - Task: {active_task['task']}\n"
                active_message += f"      - Started By: {active_task['started_by']}\n"
                active_message += f"      - Counts: {active_task['counts']}\n"
                active_message += f"      - Message Link: {active_task['message_link']}\n\n"

            elif active_task['task'] in ['inlinespam', 'raid']:
                user = active_task['user']
                active_message += f"  {active}) Active ID: {user.id} \n\n"
                active_message += f"      - User's Name: {user.first_name}\n"
                active_message += f"      - User's ID: {user.id}\n"
                active_message += f"      - Chat ID: {active_task['chat_id']}\n"
                active_message += f"      - Task: {active_task['task']}\n"
                active_message += f"      - Started By: {active_task['started_by']}\n"
                active_message += f"      - Counts: {active_task['counts']}\n"
                active_message += f"      - Message Link: {active_task['message_link']}\n\n"
        active_message += f"Total {active} Active Tasks, type '/stop (active ID)' to stop any active task!"

    if len(TheSpamX.functions.futures) == 0:
        future_message = None
    else:
        if active_message:
            active_message += "\n\n\n"
        future_message = "All Future Tasks \n\n"
        future_active = 0
        for task_id in TheSpamX.functions.futures:
            future_task = TheSpamX.functions.futures.get(task_id)
            future_active += 1
            try:
                future_time = await TheSpamX.functions.get_time(int(future_task['future']))
            except:
                future_time = f"{future_task['future']}secs"
            future_message += f"  {future_active}) Active ID: {future_task['chat_id']} \n\n"
            future_message += f"      - Chat ID: {future_task['chat_id']}\n"
            future_message += f"      - Task: {future_task['task']}\n"
            future_message += f"      - Execute after: {future_task}\n"
            future_message += f"      - Set By: {future_task['set_by']}\n"
            future_message += f"      - Counts: {future_task['counts']}\n"
            future_message += f"      - Message Link: {future_task['message_link']}\n\n"
        future_message += f"Total {future_active} Future Tasks, type '/stop future (active ID)' to stop any future task!"

    file_name = f"{round(time.time())}.txt"
    if not active_message and not future_message:
        await message.reply("__No any task ❕__")
        await wait.delete()
        return
    with open(file_name, "a", encoding="utf-8") as f:
        if active_message:
            f.write(active_message)
        if future_message:
            f.write(future_message)
    f.close()
    await message.reply_document(
        file_name,
        caption="**🔹 All task list 🔹** \n\n __- use:__ `/stop (active ID)` to stop any active task \n __- use:__ `/stop future (active ID)` to stop any future task",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📢 Updates", url=f"https://t.me/{TheSpamX.updateChannel}"
                    ),
                    InlineKeyboardButton(
                        "Support 👥", url=f"https://t.me/{TheSpamX.supportGroup}"
                    )
                ]
            ]
        )
    )
    os.remove(file_name)
    await wait.delete()

@Client.on_message(
    filters.command("stop") & filters.private #& filters.user(TheSpamX.sudo.sudoUsers)
)
async def stop_task(_, message: Message):
    if await TheSpamX.sudo.sudoFilter(message, 1):
        return

    if len(message.command) <= 1:
        await message.reply(
            "**❌ Wrong Usage!** \n\n __- use:__ `/stop (active ID)` to stop any active task \n __- use:__ `/stop future (active ID)` to stop any future task",
        )

    else:
        if len(message.command) == 2:
            active_id = int(message.command[1])
            future = False
        elif len(message.command) == 3:
            if str(message.command[1]).lower() == "future":
                future = True
            else:
                future = False
            active_id = int(message.command[2])
        else:
            await message.reply(
                "**❌ Wrong Usage!** \n\n __- use:__ `/stop (active ID)` to stop any active task \n __- use:__ `/stop future (active ID)` to stop any future task",
            )
            return
        if future:
            if active_id in TheSpamX.functions.futures:
                TheSpamX.functions.futures.pop(active_id)
                await message.reply(f"__✅ Stopped future task: Task: {active_id}__")
            else:
                await message.reply(f"__❕ No any future task in {active_id}__")
        else:
            if active_id in TheSpamX.activeTasks:
                if active_id in TheSpamX.functions.unlimited:
                    TheSpamX.functions.unlimited.remove(active_id)
                TheSpamX.activeTasks.pop(active_id)
                await message.reply(f"__✅ Stopped active task: Task: {active_id}__")
            else:
                await message.reply(f"__❕ No any active task in {active_id}__")

@Client.on_message(
    filters.regex("🔸 Get All Restricted Chats 🔸") & filters.private
)
async def all_restricted_chat(_, message: Message):
    if await TheSpamX.sudo.sudoFilter(message):
        return

    await TheSpamX.restrict.getRestrictedGroupList(message)

@Client.on_message(
    filters.regex("➕ Add Chat") & filters.private
)
async def add_chat(RiZoeL: Client, message: Message):
    if await TheSpamX.sudo.sudoFilter(message, 1):
        return

    chat_details: Message = await RiZoeL.ask(
        message.from_user.id,
        "**🔸 Please Share chat ID to add in restricted list**",
        reply_markup=ReplyKeyboardRemove()
    )
    if chat_details.text.startswith("-100") and chat_details.text.split("-")[1].isnumeric():
        await TheSpamX.restrict.add(message, chat_details.text)
    else:
        await chat_details.reply("**❌ Invalid Chat ID!**")

@Client.on_message(
    filters.regex("Remove Chat ➖") & filters.private
)
async def remove_chat(RiZoeL: Client, message: Message):
    if await TheSpamX.sudo.sudoFilter(message, 1):
        return

    chat_details: Message = await RiZoeL.ask(
        message.from_user.id,
        "**🔸 Please Share chat ID to remove from restricted list**",
        reply_markup=ReplyKeyboardRemove()
    )
    if chat_details.text.startswith("-100") and chat_details.text.split("-")[1].isnumeric():
        if str(chat_details.text) == TheSpamX.restrict.res:
            await chat_details.reply("__Sorry, You cannot remove that chat from Restricted List. It's support group of SpamX__")
            return
        await TheSpamX.restrict.remove(message, chat_details.text)
    else:
        await chat_details.reply("**❌ Invalid Chat ID!**")