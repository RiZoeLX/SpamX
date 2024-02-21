import datetime
import io
import os
import sys
import traceback
import subprocess

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import MessageTooLong

from . import TheSpamX
from SpamX.functions.messages import start_message
from SpamX.functions.keyboard import (
    start_keyboard,
    manage_clients_keyboard,
    other_keyboard,
    sudo_keyboard,
    restriction_keyboard,
    reboot_button,
)


@Client.on_message(
    filters.private & filters.command("start")
)
async def start_bot(_, message: Message):
    if await TheSpamX.sudo.sudoFilter(message, 3):
        return
    if len(message.command) > 1:
        deep_cmd = message.text.split(None, 1)[1]
        if deep_cmd.lower() == "reboot":
            if await TheSpamX.sudo.sudoFilter(message, 1):
                return
            await message.reply(
                "__Click below button to reboot the SpamX!__",
                reply_markup=reboot_button,
            )
            return
        if deep_cmd.lower() == "help":
            await TheSpamX.help(message.chat.id)
            return
    await message.reply(
        start_message.format(message.from_user.mention),
        reply_markup=start_keyboard,
    )

@Client.on_message(
    filters.private & filters.regex("Home 🏠")
)
async def start_home(_, message: Message):
    if await TheSpamX.sudo.sudoFilter(message, 3):
        return
    await message.reply(
        start_message.format(message.from_user.mention),
        reply_markup=start_keyboard,
    )

@Client.on_message(
    filters.private & filters.regex("❓Help")
)
async def help_key(_, message: Message):
    if await TheSpamX.sudo.sudoFilter(message, 3):
        return
    await TheSpamX.help(message.chat.id)

@Client.on_message(
    filters.private & filters.command("help")
)
async def help_cmd(_, message: Message):
    if await TheSpamX.sudo.sudoFilter(message, 3):
        return
    await TheSpamX.help(message.chat.id)

@Client.on_message(
    filters.private & filters.command(["reboot", "restart"]) | filters.regex("Restart|Reboot")
)
async def reboot(_, message: Message):
    if await TheSpamX.sudo.sudoFilter(message, 1):
        return
    await message.reply(
        "__Click below button to reboot the SpamX!__",
        reply_markup=reboot_button,
    )

@Client.on_message(
    filters.command("ping")
)
async def pinging(_, message: Message):
    if await TheSpamX.sudo.sudoFilter(message, 3):
        return
    start = datetime.datetime.now()
    #u_time = int(int(time.time()) - int(TheSpamX.startTime))
    #uptime = await TheSpamX.functions.get_time(time=u_time)
    pong_msg = await message.reply("**Pong !!**")
    end = datetime.datetime.now()
    ms = (end-start).microseconds / 1000
    try:
        await pong_msg.edit_text(f"⌾ {TheSpamX.pingMsg} ⌾ \n\n ༝ ᴘɪɴɢ: `{ms}` ᴍs \n ༝ ᴠᴇʀsɪᴏɴ: `{TheSpamX.versions['SpamX']}`")
    except:
        await pong_msg.edit_text(f"⌾ {TheSpamX.pingMsg} ⌾ \n\n ༝ ᴘɪɴɢ: `{ms}` ᴍs \n ༝ ᴠᴇʀsɪᴏɴ: `{TheSpamX.versions['SpamX']}`")
        await pong_msg.delete()

@Client.on_message(
    filters.regex("🔹 Manage Clients 🔹") & filters.private #& filters.user(TheSpamX.sudo.sudoUsers)
)
async def manage_clients(_, message: Message):
    if await TheSpamX.sudo.sudoFilter(message, 3):
        return
    await message.reply(
        "**🔹 Please select 🔹**",
        reply_markup=manage_clients_keyboard,
    )

@Client.on_message(
    filters.regex("Other ↗️|🔙") & filters.private #& filters.user(TheSpamX.sudo.sudoUsers)
)
async def other_(_, message: Message):
    if await TheSpamX.sudo.sudoFilter(message, 3):
        return
    await message.reply(
        "**🔹 Please select 🔹**",
        reply_markup=other_keyboard,
    )

@Client.on_message(
    filters.regex("👥 Sudo Users") & filters.private #& filters.user(TheSpamX.sudo.sudoUsers)
)
async def sudo_users(_, message: Message):
    if await TheSpamX.sudo.sudoFilter(message):
        return
    await message.reply(
        "**🔸 SpamX - Sudo Panel (Please select)**",
        reply_markup=sudo_keyboard,
    )

@Client.on_message(
    filters.regex("🔒 Restrictions") & filters.private
)
async def restrictions(_, message: Message):
    if await TheSpamX.sudo.sudoFilter(message):
        return
    await message.reply(
        "**🔸 SpamX - Restriction Chat Panel (Please select)**",
        reply_markup=restriction_keyboard,
    )

async def aexec(code, client, message):
    exec(
        "async def __aexec(client, message): "
        + "".join(f"\n {l_}" for l_ in code.split("\n"))
    )
    return await locals()["__aexec"](client, message)

@Client.on_message(
    filters.command("eval") #& filters.user(TheSpamX.sudo.sudoUsers)
)
async def runeval(client: Client, message: Message):
    if await TheSpamX.sudo.sudoFilter(message, 1):
        return
    if len(message.command) < 2:
        return await message.reply_text("❎ No python code provided! (client: Client, message: message)")

    reply_to = message.reply_to_message or message

    code = message.text.split(" ", 1)[1].strip()
    run = await message.reply_text("`running...`")

    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None

    try:
        await aexec(code, client, message)
    except Exception:
        exc = traceback.format_exc()

    evaluation = ""
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr

    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success"

    heading = f"**Eval:**\n```python\n{code}```\n\n"
    output = f"**Output:**\n`{evaluation.strip()}`"
    final_output = heading + output

    try:
        await reply_to.reply_text(final_output, disable_web_page_preview=True)
    except MessageTooLong:
        with io.BytesIO(str.encode(output)) as out_file:
            out_file.name = "eval.txt"
            await reply_to.reply_document(out_file, caption=heading)

    await run.delete()

@Client.on_message(
    filters.command("update") & filters.private
)
async def updateSpamX(SpamX: Client, message: Message):
    if await TheSpamX.sudo.sudoFilter(message, 1):
        return
    try:
        out = subprocess.check_output(["git", "pull"]).decode("UTF-8")
        if "already up to date" in str(out).lower():
            await message.reply_text("Its already up-to date!")
            return
        await message.reply_text(f"```{out}```")
    except Exception as e:
        await message.reply_text(str(e))
        return
    await message.reply_text("**Updated with main branch, restarting now.**")
    args = [sys.executable, "-m", "SpamX"]
    os.execl(sys.executable, *args)
    quit()

@Client.on_message(
    filters.command("setvar") & filters.private
)
async def setvar(SpamX: Client, message: Message):
    if await TheSpamX.sudo.sudoFilter(message, 1):
        return
    args = "".join(message.text.split(maxsplit=1)[1:]).split(" ", 1)
    if len(args) == 2:
        check_var = str(args[0])
        if check_var.upper() in ["HANDLER", "PING_MSG", "ALIVE_MSG", "ALIVE_MEDIA", "MULTITASK"]:
            var = check_var
        else:
            await message.reply_text(f"Wrong variable! All Variables given below 👇\n\n `HANDLER`, `PING_MSG`, `ALIVE_MSG`, `MULTITASK`, `ALIVE_MEDIA` \n\n © @{TheSpamX.updateChannel}")
            return
        value = str(args[1])
        try:
            os.system(f"dotenv set {var} {value}")
            await message.reply_text("**success ✓ wait for re-start**")
            args = [sys.executable, "-m", "SpamX"]
            os.execl(sys.executable, *args)
            quit()
        except Exception as error:
            await message.reply_text(f"Error: {error} \n\n Report in @{TheSpamX.supportGroup}")
    else:
        await message.reply_text(f"**Wrong Usage** \n Syntax: {TheSpamX.handler}setvar (var name) (value)")