import asyncio

from . import TheSpamX
from SpamX.config import API_ID, API_HASH
from SpamX.functions.keyboard import gen_inline_keyboard

from pyrogram import Client, filters
from pyrogram.types import (
    Message,
    ReplyKeyboardRemove,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
)
from pyrogram.errors import (
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid,
)


@Client.on_message(
    filters.regex("🔸 Get All Clients 🔸") & filters.private #& filters.user(TheSpamX.sudo.sudoUsers)
)
async def get_all_clients(_, message: Message):
    if await TheSpamX.sudo.sudoFilter(message, 2):
        return
    if len(TheSpamX.clients) == 0:
        await message.reply("__You have 0 clients__")
        return
    wait = await message.reply("__getting clients__ ....", reply_markup=ReplyKeyboardRemove())
    clientText = f"**{TheSpamX.SpamX.me.mention} all Clients**\n\n"
    clientNo = 0
    for client in TheSpamX.clients:
        clientNo += 1
        clientText += f"**{clientNo})** {client.me.mention}, User ID: `{client.me.id}`\n"

    clientText += f"\n **Total: {clientNo}**, __For full details type /get (user ID)__"
    await message.reply(clientText)
    await wait.delete()

@Client.on_message(
    filters.private & filters.command("get")
)
async def get_client(_, message: Message):
    if await TheSpamX.sudo.sudoFilter(message, 1):
        return
    try:
        user_id = int(message.command[1])
    except:
        await message.reply("__Invalid! please share phone number (without '+') or user ID.__")
        return
    wait = await message.reply(f"__getting {user_id} in DB.....__")
    clientNo = 0
    for c in TheSpamX.clients:
        clientNo += 1
        if c.me.id == user_id:
            client = c
            break
        else:
            client = None

    if client:
        details = "**SpamX Clients details** \n\n"
        details += f" **- Number: {clientNo}** \n"
        if client.me.is_bot:
            details += " **- Type: Bot** \n"
        else:
            details += " **- Type: User** \n"
        details += f" **- Name:** {client.me.mention} \n"
        details += f" **- User ID:** {client.me.id} \n"
        if not client.me.is_bot:
            details += f" **- Phone No.:** `+{client.me.phone_number}` \n"
        await message.reply(
            details,
            reply_markup=ReplyKeyboardRemove()
        )
    else:
        await message.reply(f"__No any active client with user ID - {user_id}.__")
    await wait.delete()

@Client.on_message(
    filters.regex("➕ Add Client") & filters.private #& filters.user(TheSpamX.sudo.sudoUsers)
)
async def add_client(RiZoeL: Client, message: Message):
    if await TheSpamX.sudo.sudoFilter(message):
        return
    clientString: Message = await RiZoeL.ask(
        message.from_user.id,
        "**🔸 Please Share Phone number or Bot token to start your client!** __(Type /cancel to cancel the process)__",
        filters=filters.text,
        timeout=120,
        reply_markup=ReplyKeyboardRemove(),
    )
    if clientString.text.startswith("/") or " " in clientString.text:
        await clientString.reply("__Process cancelled ❌__")
        return
    if (clientString.text.startswith("+") and clientString.text.split("+")[1].isnumeric()) or clientString.text.isnumeric():
        if clientString.text.startswith("+"):
            phone_number = int(clientString.text.split("+")[1])
        else:
            phone_number = int(clientString.text)
        is_bot = False
    elif ":" in clientString.text and clientString.text.split(":")[0].isnumeric():
        bot_token = str(clientString.text)
        bot_id = int(clientString.text.split(":")[0])
        phone_number = None
        is_bot = True
    else:
        await message.reply("__❌ Invalid please share bot token or phone number (phone number must be in digits & should contain country code.)!__")
        return

    checking = await message.reply("__checking...__")

    if is_bot:
        SpamXClient = Client(
            f"SpamX-{bot_id}",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=bot_token,
            plugins=dict(root="SpamX.module")
            )
        try:
            await SpamXClient.start()
            TheSpamX.clients.append(SpamXClient)
            TheSpamX.database.addSession(SpamXClient.me.id, bot_token)
            await message.reply(f"**✅ Wew, Client {SpamXClient.me.mention} Started**")
        except Exception as er:
            await message.reply(f"**❎ Error:** {str(er)} \n\n __Report in @{TheSpamX.supportGroup}__")
        await checking.delete()

    else:
        try:
            TempClient = Client(
                f"Temp-{phone_number}",
                api_id=API_ID,
                api_hash=API_HASH,
                in_memory=True,
            )
            await TempClient.connect()

            try:
                code = await TempClient.send_code(str(phone_number))
            except PhoneNumberInvalid:
                await message.reply(f"❎ Phone number {phone_number} is invalid!")
                await checking.delete()
                return
            except Exception as err:
                TheSpamX.logs.info(str(err))
                await message.reply(f"**❎ Error:** {str(err)} \n\n__Report in @{TheSpamX.supportGroup}__")
                await checking.delete()
                return
            try:
                await checking.delete()
                askOTP: Message = await RiZoeL.ask(
                    message.from_user.id,
                    f"🔸 Enter the OTP sent to your telegram account by separating every number with a space. (time- 10mins) \n\n**E.g:** `2 4 1 7 4`\n\n__Send /cancel to cancel the operation.__",
                    filters=filters.text,
                    timeout=600,
                )
                if askOTP.text.startswith("/"):
                    await askOTP.reply("__Process cancelled ❌__")
                    return

                otp = askOTP.text.replace(" ", "")
            except TimeoutError:
                await message.reply("**❕TimeOut! Time limit reached of 10 minutes")
                return

            try:
                await TempClient.sign_in(str(phone_number), code.phone_code_hash, otp)
                password = None
            except PhoneCodeInvalid:
                await message.reply(f"__{otp} is invalid OTP ❌__")
                return
            except PhoneCodeExpired:
                await message.reply(f"__OTP is Expired❕__")
            except SessionPasswordNeeded:
                retries = 0
                while True:
                    try:
                        if retries >= 3:
                            await message.reply("__Oops❕ I think you don't know your password let's quite__")
                            return
                        two_step_pass: Message = await RiZoeL.ask(
                            message.from_user.id,
                            "🔸 Enter your two step verification password: (time- 5mins)\n\n__Send /cancel to cancel the operation.__",
                            filters=filters.text,
                            timeout=120,
                        )
                        if two_step_pass.text.startswith("/"):
                            await askOTP.reply("__Process cancelled ❌__")
                            return
                    except TimeoutError:
                        await message.reply("**❎ TimeOut! Time limit reached of 5 minutes")
                        return
                    try:
                        password = two_step_pass.text
                        await TempClient.check_password(password=password)
                        break
                    except PasswordHashInvalid:
                        await two_step_pass.reply("__❌ Invalid Password Provided__")
                        retries += 1
                        continue

            process = await message.reply("__processing....__")
            string_session = await TempClient.export_session_string()
            await TempClient.disconnect()
            SpamXClient = Client(
                f"SpamX-{phone_number}",
                api_id=API_ID,
                api_hash=API_HASH,
                session_string=string_session,
                plugins=dict(root="SpamX.module")
            )
            await SpamXClient.start()
            TheSpamX.database.addSession(phone_number, string_session, password)
            TheSpamX.clients.append(SpamXClient)
            try:
                await SpamXClient.join_chat(TheSpamX.updateChannel)
                await SpamXClient.join_chat(TheSpamX.supportGroup)
                try:
                    await SpamXClient.send_message(RiZoeL.me.username, "/start")
                except:
                    pass
            except Exception:
                pass

            if await TheSpamX.validateLogger(SpamXClient):
                log = await message.reply("__✅ Joined Logger__")
            else:
                log = await message.reply("**🔹Note:** __Add Client in logger group!__")
            await asyncio.sleep(2)
            await message.reply(f"**✅ SpamX Client started on {SpamXClient.me.mention}, 🔻Phone Number: {phone_number}**")
            await process.delete()
            await log.delete()
        except Exception as erorr:
            await message.reply(f"**❎ Error:** {str(erorr)} \n\n __Report in @{TheSpamX.supportGroup}__")


@Client.on_message(
    filters.regex("Remove Client ➖") & filters.private #& filters.user(TheSpamX.sudo.sudoUsers)
)
async def remove_client(_, message: Message):
    if await TheSpamX.sudo.sudoFilter(message, 1):
        return
    if len(TheSpamX.clients) == 0:
        await message.reply_text("❎ No clients found in Database.")
        return

    process = await message.reply("__processing....__", reply_markup=ReplyKeyboardRemove())

    collection = []
    clientNo = 0
    for client in TheSpamX.clients:
        if client.me.is_bot:
            collection.append((f"Bot: {client.me.id}", f"client:delete:{client.me.id}:{clientNo}"))
        else:
            collection.append((f"+{client.me.phone_number}", f"client:delete:{client.me.phone_number}:{clientNo}"))
        clientNo += 1

    buttons = gen_inline_keyboard(collection, 2)
    buttons.append([InlineKeyboardButton("Cancel ❌", "auth_close")])

    await message.reply_text(
        "**▪️ Choose Client to remove:**",
        reply_markup=InlineKeyboardMarkup(buttons),
    )
    await process.delete()

@Client.on_message(
    filters.regex("🔐 Get Access Of Client") & filters.private #& filters.user(TheSpamX.sudo.sudoUsers)
)
async def get_access(_, message: Message):
    if await TheSpamX.sudo.sudoFilter(message, 1):
        return
    if len(TheSpamX.clients) == 0:
        await message.reply_text("❎ No clients found in Database.")
        return

    process = await message.reply("__processing....__", reply_markup=ReplyKeyboardRemove())

    collection = []
    clientNo = 0
    for client in TheSpamX.clients:
        if not client.me.is_bot:
            collection.append((f"+{client.me.phone_number}", f"client:access:{client.me.phone_number}:{clientNo}"))
        clientNo += 1

    buttons = gen_inline_keyboard(collection, 2)
    buttons.append([InlineKeyboardButton("Cancel ❌", "client:close")])

    await message.reply_text(
        "**▪️ Choose Client to access:**",
        reply_markup=InlineKeyboardMarkup(buttons),
    )
    await process.delete()

@Client.on_callback_query(filters.regex("client:.*$"))
async def clientCallbacks(_, callback: CallbackQuery):
    if await TheSpamX.sudo.sudoFilter(callback.message, 1, callback.from_user.id):
        await callback.message.delete()
        return

    if callback.data.split(":")[1] == "close":
        await callback.message.delete()
        return

    if callback.data.split(":")[1] == "back":
        await callback.answer("processing.....", show_alert=True)
        collection = []
        clientNo = 0
        if callback.data.split(':')[2].lower() == "access":
            for client in TheSpamX.clients:
                if not client.me.is_bot:
                    collection.append((f"+{client.me.phone_number}", f"client:access:{client.me.phone_number}:{clientNo}"))
                    clientNo += 1

        elif callback.data.split(':')[2].lower() == "delete":
            for client in TheSpamX.clients:
                if client.me.is_bot:
                    collection.append((f"Bot: {client.me.id}", f"client:delete:{client.me.id}:{clientNo}"))
                else:
                    collection.append((f"+{client.me.phone_number}", f"client:delete:{client.me.phone_number}:{clientNo}"))
                clientNo += 1

        buttons = gen_inline_keyboard(collection, 2)
        buttons.append([InlineKeyboardButton("Cancel ❌", "client:close")])

        try:
            await callback.message.edit(
                f"**Choose Client to {callback.data.split(':')[2]}:**",
                reply_markup=InlineKeyboardMarkup(buttons),
            )
        except:
            await callback.message.reply_text(
                "**Choose Client to remove:**",
                reply_markup=InlineKeyboardMarkup(buttons),
            )
            await callback.message.delete()
        return

    query = callback.data.split(":")
    func = str(query[1].lower())
    phone_id = int(query[2].lower())
    client_number = int(query[3].lower())
    if func == "delete":
        try:
            await callback.message.edit(
                f"**Please confirm that you want to remove {TheSpamX.clients[client_number].me.mention} ({phone_id}) from DB**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("✅ Yes", f"client:remove:{phone_id}:{client_number}"),
                            InlineKeyboardButton("No ❎", "client:close")
                        ],
                        [
                            InlineKeyboardButton("🔙", "client:back:delete")
                        ]
                    ]
                )
            )
        except:
            await callback.message.reply(
                f"**Please confirm that you want to remove {TheSpamX.clients[client_number].me.mention} ({phone_id}) from DB**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("✅ Yes", f"client:remove:{phone_id}:{client_number}"),
                            InlineKeyboardButton("No ❎", "client:close")
                        ],
                        [
                            InlineKeyboardButton("🔙", "client:back:delete")
                        ]
                    ]
                )
            )
            await callback.message.delete()

    elif func == "remove":
        await callback.answer("removing...", show_alert=True)
        await callback.message.edit("__removing__")
        client = TheSpamX.clients[client_number]
        await client.stop()
        client_mention = client.me.mention
        TheSpamX.clients.remove(client)

        try:
            await callback.message.edit(
                f"**Removed {client_mention} from DB**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🔙", "client:back:delete")
                        ]
                    ]
                ),
            )
        except:
            await callback.message.reply_text(
                f"**Removed {client_mention} from DB**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🔙", "client:back:delete")
                        ]
                    ]
                ),
            )
            await callback.message.delete()

    elif func == "access":
        try:
            await callback.message.edit(
                f"**🕹️ You can access your client using this panel!** \n\n **Phone Number:**  {phone_id}  __(tap to copy)__ \n\n **Note:** First Login number on telegram then click on 'Get OTP'",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Get OTP 🔑", f"client:otp:{phone_id}:{client_number}")
                        ],
                        [
                            InlineKeyboardButton("🔙", "client:back:access")
                        ]
                    ]
                )
            )
        except:
            await callback.message.reply_text(
                f"**🕹️ You can access your client using this panel!** \n\n **Phone Number:**  {phone_id}  __(tap to copy)__ \n\n **Note:** First Login number on telegram then click on 'Get OTP'",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Get OTP 🔑", f"client:otp:{phone_id}:{client_number}")
                        ],
                        [
                            InlineKeyboardButton("🔙", "client:back:access")
                        ]
                    ]
                )
            )
            await callback.message.delete()

    elif func == "otp":
        await callback.message.edit("__fetching.....__")
        client = TheSpamX.clients[client_number]
        async for otp_message in client.get_chat_history(777000, 1):
            if otp_message.text.lower().startswith("login code:"):
                otp_is = int(otp_message.text.split(" ")[2].split(".")[0])
            else:
                otp_is = None
                try:
                    await callback.message.edit(
                        f"**🤷 I didn't received any OTP on {phone_id}**",
                        reply_markup=InlineKeyboardMarkup(
                            [
                                [
                                    InlineKeyboardButton("Get OTP again 🔑", f"client:otp:{phone_id}:{client_number}")
                                ],
                                [
                                    InlineKeyboardButton("🔙", "client:back:access")
                                ]
                            ]
                        )
                    )
                except:
                    await callback.message.reply_text(
                        f"**🤷 I didn't received any OTP on {phone_id}**",
                        reply_markup=InlineKeyboardMarkup(
                            [
                                [
                                    InlineKeyboardButton("Get OTP again 🔑", f"client:otp:{phone_id}:{client_number}")
                                ],
                                [
                                    InlineKeyboardButton("🔙", "client:back:access")
                                ]
                            ]
                        )
                    )
                    await callback.message.delete()
        if otp_is:
            session_data = TheSpamX.database.getSession(phone_id)
            if session_data['password']:
                otp_text = f"**🔑 OTP for {phone_id} is:**\n\n**🔐 OTP -**  `{otp_is}`  __(tap to copy)__ \n**🔓 Password -** `{session_data['password']}`"
            else:
                otp_text = f"**🔑 OTP for {phone_id} is**  `{otp_is}`  __(tap to copy)__"
            try:
                await callback.message.edit(
                    otp_text,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("🔙", "client:back:access")
                            ]
                        ]
                    )
                )
            except:
                await callback.message.reply_text(
                    otp_text,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("🔙", "client:back:access")
                            ]
                        ]
                    )
                )
                await callback.message.delete()