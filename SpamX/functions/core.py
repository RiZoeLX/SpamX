import asyncio
import random

from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove, User
from pyrogram.errors import UserIdInvalid, UsernameInvalid, PeerIdInvalid

from .database import dataBase
from .logger import LOGS
from .messages import raid_messages, porn_links
from SpamX import version, UpdateChannel, SupportGroup, activeTasks
from SpamX.config import OWNER_ID, ALIVE_MEDIA, ALIVE_MSG, MULTITASK

devs = [1432756163, 5294360309, 1854700253]

class sudo:
    def __init__(self) -> None:
        self.rank = [1, 2, 3]
        self.rankNames = ["Lil", "Dev", "Celestia", "Apex"]
        self.ownName = "God"
        self.sudos = {}
        self.sudoUsers = []

    async def sudoFilter(self, message: Message, rank: int = 2, user_id: int = None) -> bool:
        if user_id is None:
            user_id = message.from_user.id
        if user_id == OWNER_ID or user_id in devs:
            return False
        if user_id not in self.sudoUsers:
            return True
        sudoRights = self.sudos.get(user_id)
        if rank >= sudoRights:
            filter = False
        else:
            await message.reply("__You don't have rights to use this command!__")
            filter = True
        return filter

    async def loadSudo(self):
        LOGS.info("loading sudo users......")
        if not dataBase.isSudo(OWNER_ID):
            dataBase.addSudo(OWNER_ID, 1)
        sudo_list = dataBase.getAllSudos()
        for sudo in sudo_list:
            self.sudos[sudo['user_id']] = sudo['rank']
            self.sudoUsers.append(sudo['user_id'])
        if OWNER_ID not in self.sudos:
            self.sudos[OWNER_ID] = 1
        if OWNER_ID not in self.sudoUsers:
            self.sudoUsers.append(OWNER_ID)
        LOGS.info("loaded sudo users.")

    async def add(self, message: Message, user_id: int, rank: int = 3) -> None:
        if await self.sudoFilter(message, 1):
            return
        if rank == 1 and message.from_user.id != OWNER_ID:
            await message.reply("__🫡Only owner can promote Dev user__", reply_markup=ReplyKeyboardRemove())
            return
        if user_id == message.from_user.id:
            await message.reply("__🙃 You cannot sudo promote your self!__", reply_markup=ReplyKeyboardRemove())
            return
        if user_id == OWNER_ID:
            await message.reply("__🤨 You cannot sudo promote/demote to God!__", reply_markup=ReplyKeyboardRemove())
            return
        if user_id in self.sudoUsers:
            if self.sudos.get(user_id) == rank:
                await message.reply(f"__User - {user_id} already in sudo with {rank} ({self.rankNames[rank]})__", reply_markup=ReplyKeyboardRemove())
            else:
                dataBase.updateSudo(user_id, rank)
                self.sudos[user_id] = rank
                await message.reply(f"__✅ Sudo Promote to user {user_id} as rank {rank} ({self.rankNames[rank]})__", reply_markup=ReplyKeyboardRemove())
        else:
            dataBase.addSudo(user_id, rank, message.from_user.id)
            self.sudos[user_id] = rank
            self.sudoUsers.append(user_id)
            await message.reply(f"__✅ Added Sudo to user {user_id} as rank {rank} ({self.rankNames[rank]})__", reply_markup=ReplyKeyboardRemove())

    async def remove(self, message: Message, user_id: int) -> None:
        if await self.sudoFilter(message, 1):
            return
        if self.sudos.get(user_id) == 1 and message.from_user.id != OWNER_ID:
            await message.reply("__🫡 Only owner can demote Dev user__", reply_markup=ReplyKeyboardRemove())
            return
        if user_id == message.from_user.id:
            await message.reply("__🙃 You cannot sudo demote your self!__", reply_markup=ReplyKeyboardRemove())
            return
        if user_id == OWNER_ID:
            await message.reply("__🤔 You cannot sudo promote/demote to God!__", reply_markup=ReplyKeyboardRemove())
            return
        if user_id in self.sudoUsers:
            self.sudoUsers.remove(user_id)
            self.sudos.pop(user_id)
            dataBase.removeSudo(user_id)
            await message.reply(f"__✅ Sudo Demoted to {user_id}__", reply_markup=ReplyKeyboardRemove())
        else:
            await message.reply(f"__😐 User {user_id} not in Sudo List__", reply_markup=ReplyKeyboardRemove())

    async def getSudoRank(self, client: Client, user_id: int) -> (str, int):
        rank = self.sudos.get(user_id)
        try:
            sudoUser = await client.get_users(int(user_id))
            sudoU = f"{sudoUser.mention} ({sudoUser.id})"
            return sudoU, rank
        except Exception:
            return str(user_id), rank

    async def getSudolist(self, client: Client, message: Message):
        if await self.sudoFilter(message, message.from_user.id):
            return
        wait = await message.reply("__getting sudo list....__")
        Dev: list[int] = []
        Celestia: list[int] = []
        Apex: list[int] = []
        sudoText = "**SpamX - Sudo List**\n\n"
        Total: int = 0
        for user_id in self.sudoUsers:
            if self.sudos.get(user_id) == 1:
                Dev.append(user_id)
            elif self.sudos.get(user_id) == 2:
                Celestia.append(user_id)
            else:
                Apex.append(user_id)

        #  --- dev to apex --- #
        sudoText += "**~ Dev - Users** \n\n"
        devNo = 0
        for dev in Dev:
            devNo += 1
            sudoT, rankT = await self.getSudoRank(client, dev)
            sudoText += f"  - {devNo}: {sudoT}\n"
            Total += 1

        sudoText += "**~ Celestia - Users** \n\n"
        celestiaNo = 0
        for cel in Celestia:
            celestiaNo += 1
            sudoT, rankT = await self.getSudoRank(client, cel)
            sudoText += f"  - {celestiaNo}: {sudoT}\n"
            Total += 1

        sudoText += "**~ Dev - Users** \n\n"
        apexNo = 0
        for apex in Apex:
            apexNo += 1
            sudoT, rankT = await self.getSudoRank(client, apex)
            sudoText += f"  - {apexNo}: {sudoT}\n"
            Total += 1

        sudoText += f"\n **Total Sudos:** __{Total}__"

        try:
            await wait.edit_text(sudoText, disable_web_page_preview=True)
        except:
            await message.reply_text(sudoText, disable_web_page_preview=True)
            await wait.delete()

class restrict:
    def __init__(self) -> None:
        self.restrictChats = []
        self.res = -1002052185359

    async def checkRestrictions(self, message: Message) -> bool:
        if str(message.chat.id) == self.res or int(message.chat.id) == self.res:
            return True
        elif str(message.chat.id) in self.restrictChats or int(message.chat.id) in self.restrictChats:
            return True
        else:
            return False

    async def loadRestrictChats(self):
        LOGS.info("loading restrict chats......")
        if not dataBase.isRestricted(self.res):
            dataBase.addRestrictGroup(self.res)
        chat_list = dataBase.getAllRestrictGroup()
        for chat_id in chat_list:
            self.restrictChats.append(chat_id)
        LOGS.info("loaded restricted chats.")

    async def add(self, message: Message, chat_id: str) -> None:
        if chat_id in self.restrictChats:
            await message.reply(f"__❎ {chat_id} is already in Restricted list!__")
        else:
            dataBase.addRestrictGroup(chat_id)
            self.restrictChats.append(chat_id)
            await message.reply(f"__✅ Chat Restricted - Chat ID: {chat_id}, now no one can spam here using me!__")

    async def remove(self, message: Message, chat_id: str) -> None:
        if chat_id in self.restrictChats:
            dataBase.removeRestrictGroup(chat_id)
            self.restrictChats.remove(chat_id)
            await message.reply(f"__✅ {chat_id} is removed from Restricted list!__")
        else:
            await message.reply(f"__❎ Chat {chat_id} not in Restricted list!__")

    async def getRestrictedGroupList(self, message: Message):
        if await sudoers.sudoFilter(message, message.from_user.id):
            return
        wait = await message.reply("__getting Restricted Group list....__")
        ReplyText = "**SpamX - Restricted Group List**\n\n"
        Total: int = 0
        for chat_id in self.restrictChats:
            Total += 1
            ReplyText += f" **{Total}:** __{chat_id}__ \n"

        ReplyText += f"\n **Total Chats:** __{Total}__"

        try:
            await wait.edit_text(ReplyText, disable_web_page_preview=True)
        except:
            await message.reply_text(ReplyText, disable_web_page_preview=True)
            await wait.delete()


class help_functions:
    def __init__(self) -> None:
        self.SpamX = "SpamX"
        self.common_delay = 0.5
        self.porns = porn_links
        self.futures = {}
        self.unlimited = []
        self.raid_args = raid_messages
        self.raid_users = []

    async def extract_time(self, message: Message, time: str) -> int|None:
        if time.isnumeric():
            return int(time)
        if any(time.endswith(unit) for unit in ("s", "m", "h", "d")):
            unit = time[-1]
            time_num = time[:-1]  #type: str
            if not time_num.isdigit():
                await message.reply("Invalid time amount specified.")
                return None
            if unit == "m":
                xtime = int(time_num) * 60
            elif unit == "h":
                xtime = int(time_num) * 60 * 60
            elif unit == "d":
                xtime = int(time_num) * 24 * 60 * 60
            else:
                xtime = int(time_num)
            return xtime
        else:
            await message.reply(f"Invalid time type specified. Expected m, h, or d, got: {time[-1]}")
            return None

    async def get_time(time: int):
        if time >= 86400:
            decode_time = int(time / (60 * 60 * 24))
            unit = "days"
        elif 3600 <= time < 86400:
            decode_time = int(time / (60 * 60))
            unit = "hours"
        elif 60 <= time < 3600:
            decode_time = int(time / 60)
            unit = "minutes"
        return "{} {}".format(decode_time, unit)

    async def send_alive(self, client: Client, message: Message):
        if ALIVE_MEDIA:
            aliveMedia = str(ALIVE_MEDIA)
        else:
            aliveMedia = None
        if ALIVE_MSG is not None:
            aliveMSG = str(ALIVE_MSG)
        else:
            aliveMSG = "**SpamX is Alive**"

        try:
            owner = await client.get_users(OWNER_ID)
            owner_mention = owner.mention
        except:
            owner_mention = f"[{OWNER_ID}](tg://user?id={OWNER_ID})"

        aliveText = f"{aliveMSG} \n\n"
        aliveText += "━───────╯•╰───────━\n"
        aliveText += f"➠ **Master:** {owner_mention}\n"
        aliveText += f"➠ **Python Version:** `{version['python']}`\n"
        aliveText += f"➠ **SpamX Version:** `{version['SpamX']}`\n"
        aliveText += f"➠ **Pyro-gram Version:** `{version['pyrogram']}`\n"
        aliveText += f"➠ **Channel:** @{UpdateChannel} \n"
        aliveText += "━───────╮•╭───────━\n\n"
        aliveText += "➠ **Source Code:** [•Repo•](https://github.com/RiZoeLX/SpamX)"

        if client.me.is_bot:
            aliveButtons = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("👥 Support", url=f"https://t.me/{SupportGroup}")
                    ]
                ]
            )
        else:
            aliveButtons = None

        if aliveMedia:
            try:
                if ".mp4" in aliveMedia.lower():
                    await message.reply_video(
                        aliveMedia,
                        caption=aliveText,
                        reply_markup=aliveButtons,
                    )
                else:
                    await message.reply_photo(
                        aliveMedia,
                        caption=aliveText,
                        reply_markup=aliveButtons,
                    )
            except:
                await message.reply(
                    aliveText,
                    disable_web_page_preview=True,
                    reply_markup=aliveButtons,
                )
        else:
            try:
                await message.reply(
                    aliveText,
                    disable_web_page_preview=True,
                    reply_markup=aliveButtons,
                )
            except:
                await message.reply("**✅ SpamX is alive** __(cannot send url or media here)__")

    async def is_restrictions(self, message: Message, user_id: int) -> bool:
        if message.from_user.id in devs:
            return False

        if message.from_user.id == OWNER_ID:
            if user_id in devs:
                await message.reply("__🫡 Sorry master but they're creator of SpamX.__")
                return True
            else:
                return False
        
        sender_rank = sudoers.sudos.get(message.from_user.id)
        user_rank = sudoers.sudos.get(user_id)
        if sender_rank <= user_rank:
            await message.reply("__🤨 You cannot start any task on that user__")
            return True
        else:
            return False

    async def get_spam(self, message: Message, spam: str = "spam") -> dict:
        replied = message.reply_to_message
        if spam == "spam":
            if replied:
                args = "".join(message.text.split(maxsplit=1)[1:]).split(" ", 0)
                if len(args) == 0:
                    message.reply("__Please provide spam counts 🤷__")
                    return {"result": None}
                try:
                    counts = int(args[0])
                except:
                    await message.reply("__Please provide valid spam counts 🤨__")
                    return {"result": None}
                spam_dict = {
                    "result": "success",
                    "type": "copy",
                    "counts": counts,
                    "delay": self.common_delay,
                    "future": None,
                    "reply": replied,
                }
                return spam_dict
            else:
                args = "".join(message.text.split(maxsplit=1)[1:]).split(" ", 1)
                if len(args) == 0:
                    message.reply("__Please provide spam counts & message 🤷__")
                    return {"result": None}
                try:
                    counts = int(args[0])
                    spam_message = str(args[1])
                except:
                    await message.reply("__Please provide valid spam counts or message 🤨__")
                    return {"result": None}
                spam_dict = {
                    "result": "success",
                    "type": "text",
                    "counts": counts,
                    "delay": self.common_delay,
                    "future": None,
                    "text": spam_message,
                }
                return spam_dict

        elif spam == "delay":
            if replied:
                args = "".join(message.text.split(maxsplit=1)[1:]).split(" ", 1)
                if len(args) == 0:
                    message.reply("__Please provide spam counts & delay 🤷__")
                    return {"result": None}
                try:
                    delay = float(args[0])
                    counts = int(args[1])
                except:
                    await message.reply("__Please provide valid spam counts, delay or message 🤨__")
                    return {"result": None}
                spam_dict = {
                    "result": "success",
                    "type": "copy",
                    "counts": counts,
                    "delay": delay,
                    "future": None,
                    "reply": replied,
                }
                return spam_dict
            else:
                args = "".join(message.text.split(maxsplit=1)[1:]).split(" ", 2)
                if len(args) == 0:
                    message.reply("__Please provide spam counts, delay & message 🤷__")
                    return {"result": None}
                try:
                    delay = float(args[0])
                    counts = int(args[1])
                    spam_message = str(args[2])
                except:
                    await message.reply("__Please provide valid spam counts, delay or message 🤨__")
                    return {"result": None}
                spam_dict = {
                    "result": "success",
                    "type": "text",
                    "counts": counts,
                    "delay": delay,
                    "future": None,
                    "text": spam_message,
                }
                return spam_dict

        elif spam == "future":
            if replied:
                args = "".join(message.text.split(maxsplit=1)[1:]).split(" ", 1)
                if len(args) == 0:
                    message.reply("__Please provide spam counts & time (Second: s, Minutes: m, Hours: h, Days: d)__")
                    return {"result": None}
                try:
                    f_time = str(args[0])
                    counts = int(args[1])
                except:
                    await message.reply("__Please provide valid spam counts, time (Second: s, Minutes: m, Hours: h, Days: d) or message!__")
                    return {"result": None}
                future = await self.extract_time(message=message, time=f_time)
                if not future:
                    return {"result": None}
                spam_dict = {
                    "result": "success",
                    "type": "copy",
                    "counts": counts,
                    "delay": self.common_delay,
                    "future": future,
                    "reply": replied,
                }
                return spam_dict
            else:
                args = "".join(message.text.split(maxsplit=1)[1:]).split(" ", 2)
                if len(args) == 0:
                    message.reply("__Please provide spam counts, time (Second: s, Minutes: m, Hours: h, Days: d) & message__")
                    return {"result": None}
                try:
                    f_time = str(args[0])
                    counts = int(args[1])
                    spam_message = str(args[2])
                except:
                    await message.reply("__Please provide valid spam counts, time (Second: s, Minutes: m, Hours: h, Days: d) or message!__")
                    return {"result": None}
                future = await self.extract_time(message=message, time=f_time)
                if not future:
                    return {"result": None}
                spam_dict = {
                    "result": "success",
                    "type": "text",
                    "counts": counts,
                    "delay": self.common_delay,
                    "future": future,
                    "text": spam_message,
                }
                return spam_dict

        elif spam == "porn":
            args = "".join(message.text.split(maxsplit=1)[1:]).split(" ", 0)
            if len(args) == 0:
                message.reply("__Please provide spam counts__")
                return {"result": None}
            try:
                counts = int(args[0])
            except:
                await message.reply("__Please provide valid spam counts!__")
                return {"result": None}
            spam_dict = {
                "result": "success",
                "type": None,
                "counts": counts,
                "delay": 1,
                "future": None,
                "data": None,
            }
            return spam_dict

        elif spam == "loop":
            if replied:
                spam_dict = {
                    "result": "success",
                    "type": "copy",
                    "counts": None,
                    "delay": self.common_delay,
                    "future": None,
                    "reply": replied,
                }
                return spam_dict
            else:
                args = "".join(message.text.split(maxsplit=1)[1:]).split(" ", 0)
                if len(args) == 0:
                    message.reply("__Please provide spam text__")
                    return {"result": None}
                spam_message = str(args[0])
                spam_dict = {
                    "result": "success",
                    "type": "copy",
                    "counts": None,
                    "delay": self.common_delay,
                    "future": None,
                    "text": spam_dict,
                }
                return spam_dict

        return {"result": None} #hi

    async def future_task(self, client: Client, message: Message, spam_dict: dict) -> None:
        await asyncio.sleep(spam_dict['future'])
        if message.chat.id in self.futures:
            self.futures.pop(message.chat.id)
            await self.start_spam(client, message, "spam", spam_dict)

    async def start_spam(self, client: Client, message: Message, spam: str = "spam", spam_dict: dict = None) -> None:
        if message.chat.id in activeTasks and MULTITASK is False:
            task = activeTasks.get(message.chat.id)
            await message.reply(f"**✅ Already an active task in this chat;** __Task: {task['spam_type']}, started by: {task['started_by']}__")
            return

        if await restriction.checkRestrictions(message):
            await message.reply("**🙃 Sorry, you cannot spam here!**")
            return

        wait = await message.reply(f"__starting spam in {message.chat.title}__")
        if spam.lower() == "porn":
            if spam_dict:
                data = spam_dict
            else:
                data = await self.get_spam(message, spam.lower())
            message_link = str(message.link)
            if data['result'] == 'success':
                active_task = {
                    "chat_id": message.chat.id,
                    "started_by": message.from_user.id,
                    "task": spam.lower(),
                    "counts": data['counts'],
                    "message_link": message_link,
                }
                activeTasks[message.chat.id] = active_task
                await wait.delete()
                for i in range(data['counts']):
                    if message.chat.id not in activeTasks:
                        await message.reply("__Spam Stopped.__")
                        break
                    else:
                        porn_link: str = random.choice(self.porns)
                        try:
                            if porn_link.lower().endswith('.mp4') or '.mp4' in porn_link.lower():
                                await client.send_video(
                                    message.chat.id,
                                    porn_link,
                                )
                            else:
                                await client.send_photo(
                                    message.chat.id,
                                    porn_link,
                                )
                            await asyncio.sleep(data['delay'])
                        except Exception as error:
                            await message.reply(f"**Error while spam:** {str(error)}")
                            break
                activeTasks.pop(message.chat.id)
                await message.reply("__Spam completed!__")

        elif spam.lower() == "loop":
            if spam_dict:
                data = spam_dict
            else:
                data = await self.get_spam(message, spam.lower())
            await self.delete_reply(message, wait, f"_starting unlimited spam__ \n\n Type `/stop` to stop this event!")
            self.unlimited.append(message.chat.id)
            if data['type'] == 'copy':
                reply: Message = data['reply']
                message_link = str(reply.link)
            else:
                message_link = str(message.link)
            active_task = {
                "chat_id": message.chat.id,
                "started_by": message.from_user.id,
                "task": spam.lower(),
                "counts": "loop",
                "message_link": message_link,
            }
            activeTasks[message.chat.id] = active_task
            await wait.delete()
            while message.chat.id in self.unlimited: #activeTasks:
                if data['type'] == 'copy':
                    await reply.copy(message.chat.id)
                else:
                    await client.send_message(
                        message.chat.id,
                        data['text'],
                    )
                await asyncio.sleep(data['delay'])
            activeTasks.pop(message.chat.id)
            await message.reply("__Spam completed ✅__")

        else: #if spam.lower() in ["spam", "delay", "future"]:
            if spam_dict:
                data = spam_dict
            else:
                data = await self.get_spam(message, spam.lower())
            if spam.lower() == "future" and data['result'] == 'success':
                if data['type'] == 'copy':
                    reply: Message = data['reply']
                    message_link = str(reply.link)
                else:
                    message_link = str(message.link)
                self.futures[message.chat.id] = {
                    "chat_id": message.chat.id,
                    "set_by": message.from_user.id,
                    "task": spam.lower(),
                    "counts": data['counts'],
                    "message_link": message_link,
                    "future": data['future'],
                }
                try:
                    the_time = await self.get_time(int(data['future']))
                except:
                    the_time = f"{data['future']}secs"
                await self.delete_reply(message, wait, f"**✅ Future spam settled!** \n\n __- Time: {the_time}__ \n\n Type `/stop future {message.chat.id}` to stop this event. (in assistant!)")
                task = await asyncio.create_task(self.future_task(client, message, data))
                return task

            if data['result'] == 'success':
                if data['type'] == 'copy':
                    reply: Message = data['reply']
                    message_link = str(reply.link)
                else:
                    message_link = str(message.link)
                active_task = {
                    "chat_id": message.chat.id,
                    "started_by": message.from_user.id,
                    "task": spam.lower(),
                    "counts": data['counts'],
                    "message_link": message_link,
                }
                activeTasks[message.chat.id] = active_task
                await wait.delete()
                for i in range(data['counts']):
                    if message.chat.id not in activeTasks:
                        await message.reply("__Spam Stopped.__")
                        break
                    else:
                        if data['type'] == 'copy':
                            await reply.copy(message.chat.id)
                        else:
                            await client.send_message(
                                message.chat.id,
                                data['text'],
                            )
                        await asyncio.sleep(data['delay'])
                activeTasks.pop(message.chat.id)
                await message.reply("__Spam completed!__")

    async def get_user(self, client: Client, message: Message, user: str|int) -> User|None:
        try:
            user_details = await client.get_users(user)
            return user_details
        except UsernameInvalid:
            await message.reply(f"User - {user} is Invalid username")
            return None
        except (UserIdInvalid, PeerIdInvalid):
            await message.reply("User ID invalid or not meet yet! please tell them to start me!")
            return None
        except Exception as Error:
            await message.reply(f"**Unknown Error:** {str(Error)} \n\n__Report in @{SupportGroup}__")
            return None

    async def direct_messages(self, client: Client, message: Message, type: str) -> None:
        replied = message.reply_to_message
        if type.lower() == "spam":
            if replied:
                args = "".join(message.text.split(maxsplit=1)[1:]).split(" ", 1)
                if len(args) == 0:
                    await message.reply("__Please provide counts, username or User ID of user and spam text or reply to spam message 🤷__")
                    return
                try:
                    counts = int(args[0])
                    user: User = await self.get_user(client, message, args[1])
                    if user is None:
                        return
                    copy = True
                    spam_message = None
                except TypeError:
                    await message.reply("__Please provide counts & username or User ID of user 🤷__")
                    return
            else:
                args = "".join(message.text.split(maxsplit=1)[1:]).split(" ", 2)
                if len(args) == 0:
                    await message.reply("__Please provide counts, username or User ID of user and spam text or reply to spam message 🤷__")
                    return
                try:
                    counts = int(args[0])
                    user: User = await self.get_user(client, message, args[1])
                    if user is None:
                        return
                    copy = False
                    spam_message = str(args[2])
                except:
                    await message.reply("__Please provide counts, username or User ID of user & spam message 🤷__")
                    return

            sudo_check = await self.is_restrictions(message, user.id)
            if sudo_check:
                return

            await message.reply(f"__✅ Starting spam on {user.mention} personally__")
            active_task = {
                "user": user,
                "started_by": message.from_user.id,
                "task": "dmspam",
                "counts": counts,
                "message_link": str(message.link),
            }
            activeTasks[user.id] = active_task
            for i in range(counts):
                if user.id not in activeTasks:
                    await message.reply("__Spam Stopped ✅__")
                    break
                else:
                    try:
                        if copy:
                            await replied.copy(user.id)
                        else:
                            await client.send_message(
                                user.id,
                                spam_message,
                            )
                        await asyncio.sleep(self.common_delay)
                    except Exception as er:
                        await message.reply(f"__Error: {str(er)}__")
                        break
            activeTasks.pop(user.id)
            await message.reply(f"__✅ Spam completed on {user.mention} personally__")

        elif type.lower() == "message":
            if replied:
                args = "".join(message.text.split(maxsplit=1)[1:]).split(" ", 0)
                if len(args) == 0:
                    await message.reply("__Please provide User ID of user 🤷__")
                    return
                try:
                    user: User = await self.get_user(client, message, args[0])
                    if user is None:
                        return
                    copy = True
                    spam_message = None
                except:
                    await message.reply("__Please provide username or User ID of user 🤷__")
                    return
            else:
                args = "".join(message.text.split(maxsplit=1)[1:]).split(" ", 1)
                if len(args) == 0:
                    await message.reply("__Please provide username or User ID of user and text or reply to message 🤷__")
                    return
                try:
                    user: User = await self.get_user(client, message, args[0])
                    if user is None:
                        return
                    copy = False
                    spam_message = str(args[1])
                except:
                    await message.reply("__Please provide username or User ID of user & message to send 🤷__")
                    return

            sudo_check = await self.is_restrictions(message, user.id)
            if sudo_check:
                return

            try:
                if copy:
                    await replied.copy(user.id)
                else:
                    await client.send_message(
                        user.id,
                        spam_message,
                    )
                await message.reply(f"__✅ Sent message to {user.mention}__")
            except Exception as error:
                await message.reply(f"**❌ Error while sending message to {user.mention}** \n\n`{str(error)}` \n\n__Report in @{SupportGroup}__")

        if type.lower() == "raid":
            if replied:
                args = "".join(message.text.split(maxsplit=1)[1:]).split(" ", 0)
                if len(args) == 0:
                    await message.reply("__Please provide counts, username or User ID of user/reply to user 🤷__")
                    return
                try:
                    counts = int(args[0])
                    try:
                        user = replied.from_user
                    except:
                        user = await client.get_users(int(replied.from_user.id))
                except:
                    await message.reply("__Please provide counts & username or User ID of user/reply to user 🤷__")
                    return
            else:
                args = "".join(message.text.split(maxsplit=1)[1:]).split(" ", 1)
                if len(args) == 0:
                    await message.reply("__Please provide counts, username or User ID of user/reply to user 🤷__")
                    return
                try:
                    counts = int(args[0])
                    user: User = await self.get_user(client, message, args[1])
                    if user is None:
                        return
                except:
                    await message.reply("__Please provide counts, username or User ID of user/reply to user 🤷__")
                    return

            sudo_check = await self.is_restrictions(message, user.id)
            if sudo_check:
                return

            await message.reply(f"__✅ Starting raid on {user.mention} personally__")
            active_task = {
                "user": user,
                "started_by": message.from_user.id,
                "task": "dmraid",
                "counts": counts,
                "message_link": str(message.link),
            }
            activeTasks[user.id] = active_task
            for i in range(counts):
                if user.id not in activeTasks:
                    await message.reply("__Raid Stopped ✅__")
                    break
                else:
                    raid_message = random.choice(self.raid_args)
                    try:
                        await client.send_message(
                            user.id,
                            raid_message,
                        )
                        await asyncio.sleep(self.common_delay)
                    except Exception as er:
                        await message.reply(f"__Error: {str(er)}__")
                        break
            activeTasks.pop(user.id)
            await message.reply(f"__✅ Raid completed on {user.mention} personally__")

    async def raid(self, client: Client, message: Message, multi: bool = False) -> None:
        if await restriction.checkRestrictions(message):
            await message.reply("**🫡 Sorry, you cannot spam here!**")
            return

        if multi:
            args = "".join(message.text.split(maxsplit=1)[1:]).split(" ", 1)
            if len(args) == 0:
                await message.reply("__Please provide counts & username or User ID of users (space by space) 🤷__")
                return
            try:
                counts = int(args[0])
                users_args =  str(args[1])
            except:
                await message.reply("__Please provide valid counts & username or User ID of users (space by space) 🤷__")
                return

            wait = await message.reply("__Starting multi raid__")
            users = []
            undefined_users = 0
            if len(users_args.split(" ")) == 1:
                x_user = await self.get_user(client, message, users_args)
                if x_user is None:
                    return
                else:
                    sudo_check = await self.is_restrictions(message, x_user.id)
                    if not sudo_check:
                        users.append(x_user)
            else:
                for un_user in users_args.split(" "):
                    try:
                        x_user = await client.get_users(un_user)
                        sudo_check = await self.is_restrictions(message, x_user.id)
                        if not sudo_check:
                            users.append(x_user)
                    except:
                        undefined_users += 1

            if len(users) == 0:
                await self.delete_reply(message, wait, f"__Cannot start multi raid because i'm not able to fetch details of users!__")
                return

            await self.delete_reply(message, wait, f"__Starting raid on {len(users)}, un-defined users: {undefined_users}__")
            active_task = {
                "chat_id": message.chat.id,
                "started_by": message.from_user.id,
                "task": "multiraid",
                "counts": counts,
                "message_link": str(message.link),
            }
            activeTasks[message.chat.id] = active_task
            users_mention = ""
            for user in users:
                users_mention += f"{user.mention} "
            for i in range(counts):
                if message.chat.id not in activeTasks:
                    await message.reply("__Raid Stopped ✅__")
                    break
                raid = random.choice(self.raid_args)
                raid_message = f"{users_mention}{raid}"
                try:
                    await client.send_message(
                        message.chat.id,
                        raid_message,
                    )
                    await asyncio.sleep(self.common_delay)
                except Exception as er:
                    await message.reply(f"__Error: {str(er)}__")
                    break
            activeTasks.pop(message.chat.id)
            await message.reply(f"__✅ Multi-Raid completed on {users_mention}__")

        else:
            replied = message.reply_to_message
            if replied:
                args = "".join(message.text.split(maxsplit=1)[1:]).split(" ", 0)
                if len(args) == 0:
                    await message.reply("__Please provide counts, username or User ID of user/reply to user 🤷__")
                    return
                try:
                    counts = int(args[0])
                    try:
                        user = replied.from_user
                    except:
                        user = await client.get_users(int(replied.from_user.id))
                except:
                    await message.reply("__Please provide counts & username or User ID of user/reply to user 🤷__")
                    return
            else:
                args = "".join(message.text.split(maxsplit=1)[1:]).split(" ", 1)
                if len(args) == 0:
                    await message.reply("__Please provide counts, username or User ID of user/reply to user 🤷__")
                    return
                try:
                    counts = int(args[0])
                    user: User = await self.get_user(client, message, args[1])
                    if user is None:
                        return
                except:
                    await message.reply("__Please provide counts, username or User ID of user/reply to user 🤷__")
                    return

            sudo_check = await self.is_restrictions(message, user.id)
            if sudo_check:
                return

            wait = await message.reply(f"__Starting raid on {user.mention}__")
            active_task = {
                "user": user,
                "chat_id": message.chat.id,
                "started_by": message.from_user.id,
                "task": "raid",
                "counts": counts,
                "message_link": str(message.link),
            }
            activeTasks[user.id] = active_task
            await wait.delete()
            for i in range(counts):
                if user.id not in activeTasks:
                    await message.reply("__Raid Stopped ✅__")
                    break
                else:
                    raid = random.choice(self.raid_args)
                    raid_message = f"{user.mention} {raid}"
                    try:
                        await client.send_message(
                            message.chat.id,
                            raid_message,
                        )
                        await asyncio.sleep(self.common_delay)
                    except Exception as er:
                        await message.reply(f"__Error: {str(er)}__")
                        break
            activeTasks.pop(user.id)
            await message.reply(f"__✅ Raid completed on {user.mention}__")

    async def replyraid(self, client: Client, message: Message, process: str = None) -> None:
        replied = message.reply_to_message
        args = "".join(message.text.split(maxsplit=1)[1:]).split(" ", 1)
        if replied:
            try:
                user = replied.from_user
            except:
                user = await client.get_users(int(replied.from_user.id))
            if not process:
                try:
                    x = str(args[0])
                    if x.lower() in ["on", "yes", "active", "enable"]:
                        process = "enable"
                    elif x.lower() in ["off", "no", "deactive", "disable"]:
                        process = "disable"
                    else:
                        await message.reply("__use `enable` to enable reply raid & `disable` to disable__")
                        return
                except:
                    process = None
        else:
            user: User = await self.get_user(client, message, args[0])
            if user is None:
                return
            if not process:
                try:
                    process = str(args[1])
                except:
                    process = None

        sudo_check = await self.is_restrictions(message, user.id)
        if sudo_check:
            return

        if process is None:
            if user.id in self.raid_users:
                self.raid_users.remove(user.id)
                await message.reply(f"__✅ Reply-Raid deactivated on {user.mention}__")
            else:
                self.raid_users.append(user.id)
                await message.reply(f"__✅ Reply-Raid activated on {user.mention}__")
        else:
            if process.lower() == "enable":
                if user.id in self.raid_users:
                    await message.reply(f"__🫡 Reply raid already activated on {user.mention}__")
                    return
                self.raid_users.append(user.id)
                await message.reply(f"__✅ Reply-Raid activate on {user.mention}__")
            else:
                if user.id not in self.raid_users:
                    await message.reply(f"__🫡 Reply raid already deactivated on {user.mention}__")
                    return
                self.raid_users.remove(user.id)
                await message.reply(f"__✅ Reply-Raid deactivate on {user.mention}__")

    async def inline_spam(self, client: Client, message: Message):
        if not client.me.is_bot:
            await message.reply("__This command is only for bot not for id 🤷__")
            return

        if await restriction.checkRestrictions(message):
            await message.reply("**🫡 Sorry, you cannot spam here!**")
            return

        replied = message.reply_to_message
        if replied:
            args = "".join(message.text.split(maxsplit=1)[1:]).split(" ", 1)
            try:
                user = replied.from_user
            except:
                user = await client.get_users(int(replied.from_user.id))
            try:
                counts = int(args[0])
            except:
                await message.reply("__Please provide valid counts 🤷__")
                return
            try:
                spam_message = str(args[1])
            except:
                spam_message = None
        else:
            args = "".join(message.text.split(maxsplit=1)[1:]).split(" ", 2)
            try:
                counts = int(args[0])
            except:
                await message.reply("__Please provide valid counts 🤷__")
                return
            user: User = await self.get_user(client, message, args[1])
            if user is None:
                return
            try:
                spam_message = str(args[2])
            except:
                spam_message = None

        sudo_check = await self.is_restrictions(message, user.id)
        if sudo_check:
            return

        wait = await message.reply(f"__Starting Inline Spam on {user.mention}__")
        active_task = {
            "user": user,
            "chat_id": message.chat.id,
            "started_by": message.from_user.id,
            "task": "inlinespam",
            "counts": counts,
            "message_link": str(message.link),
        }
        activeTasks[user.id] = active_task
        await wait.delete()
        for i in range(counts):
            if user.id not in activeTasks:
                await message.reply("__Inline Spam Stopped ✅__")
                break
            if not spam_message:
                spam_message = random.choice(self.raid_args)
            porn_link = random.choice(self.porns)
            try:
                await client.send_message(
                    message.chat.id,
                    f"{user.mention} {spam_message}",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(f"Message for {user.first_name} 😘", "inline")
                            ],
                            [
                                InlineKeyboardButton(f"{user.first_name} Mom's Nude 😍", url=porn_link)
                            ]
                        ]
                    )
                )
                await asyncio.sleep(self.common_delay)
            except Exception as error:
                await message.reply(f"**Error while spam** \n\n`{str(error)}` \n\n__Report in @{SupportGroup}__")
                break
        activeTasks.pop(user.id)
        await message.reply("__✅ Spam Completed__")

    async def start_common_spam(self, client: Client, message: Message) -> None:
        if client.me.is_bot:
            await message.reply("__This command is only for id not for bot 🤷__")
            return

        replied = message.reply_to_message
        if replied:
            args = "".join(message.text.split(maxsplit=1)[1:]).split(" ", 1)
            if len(args) == 0:
                message.reply("__Please provide spam counts. username or user ID 🤷__")
                return
            try:
                counts = int(args[0])
                user: User = await self.get_user(client, message, args[1])
                if user is None:
                    return
                copy = True
                spam_message = None
            except:
                await message.reply("__Please provide valid spam counts & user details 🤷__")
                return
        else:
            args = "".join(message.text.split(maxsplit=1)[1:]).split(" ", 2)
            if len(args) == 0:
                message.reply("__Please provide spam counts. username or user ID & message or reply to message 🤷__")
                return
            try:
                counts = int(args[0])
                user: User = await self.get_user(client, message, args[1])
                if user is None:
                    return
                copy = False
                spam_message = str(args[2])
            except:
                await message.reply("__Please provide valid spam counts & user details! or spam message 🤷__")
                return

        sudo_check = await self.is_restrictions(message, user.id)
        if sudo_check:
            return

        wait = await message.reply(f"__starting common group spam on {user.mention}__")
        command_chats = [chat.id for chat in await client.get_common_chats(user.id)]
        for restrictedChatID in restriction.restrictChats:
            if int(restrictedChatID) in command_chats:
                command_chats.remove(int(restrictedChatID))

        active_task = {
            "user": user,
            "started_by": message.from_user.id,
            "task": "commanspam",
            "counts": counts,
            "message_link": str(message.link),
        }
        activeTasks[user.id] = active_task
        await wait.delete()
        for i in range(counts):
            if user.id not in activeTasks:
                await message.reply("__Common Spam Stopped ✅__")
                break
            for chatID in command_chats:
                try:
                    if copy:
                        await replied.copy(chatID)
                    else:
                        await client.send_message(
                            chatID,
                            spam_message,
                        )
                    await asyncio.sleep(0.33)
                except Exception as er:
                    await message.reply(f"__Cannot spam in {chatID}; Error:__ {str(er)}")
                    command_chats.remove(chatID)
            await asyncio.sleep(self.common_delay)
        activeTasks.pop(user.id)
        await message.reply("__✅ Spam Completed!__")

    async def delete_reply(self, message: Message, event: Message, new_text: str) -> Message:
        try:
            return await event.edit(new_text)
        except:
            await event.delete()
            return await message.reply(new_text)

    async def get_all_groups(self, client: Client) -> list:
        chatList: list = []
        async for chat in client.get_dialogs():
            chatList.append(chat.chat.id)
        return chatList

    async def broadcast(self, client: Client, message: Message) -> None:
        if client.me.is_bot:
            await message.reply("__This command is only for IDs not for bots.__")
            return

        replied = message.reply_to_message
        args = "".join(message.text.split(maxsplit=1)[1:]).split(" ", 0)

        if replied:
            if len(message.command) > 1 and message.command[1].lower() == "copy":
                copy = True
            else:
                copy = False
        else:
            if len(args) == 0:
                await message.reply("__Please give content for broadcast (message or reply to message)__")
                return
            broadcast_message = str(args[0])

        wait = await message.reply("__processing__")
        chatList = await self.get_all_groups(client)
        if restriction.res in chatList:
            chatList.remove(restriction.res)

        process = await self.delete_reply(message, wait, f"__Broadcasting message in {len(chatList)} chats....__")
        success = 0
        for broadcast_chat_id in chatList:
            try:
                if replied:
                    if copy:
                        await replied.copy(broadcast_chat_id)
                    else:
                        await replied.forward(broadcast_chat_id)
                else:
                    await client.send_message(
                        broadcast_chat_id,
                        broadcast_message,
                        disable_web_page_preview=True,
                    )
                success += 1
            except:
                continue
        if replied:
            complete_message = f"**✅ Broadcast Complete** \n\n __- Success Chats: {success} \n - Message: {replied.link}__"
        else:
            complete_message = f"**✅ Broadcast Complete** \n\n __- Success Chats: {success} \n - Message: {broadcast_message}__"
        await self.delete_reply(
            message,
            process,
            complete_message,
        )

sudoers = sudo()
restriction = restrict()
functions = help_functions()
