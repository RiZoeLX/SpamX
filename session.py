from pyrogram import Client
import tgcrypto

print("\n\n • Program String Generator •")
print("\n\n Enter Your Vail Details to Continue")


API_KEY = int(input("\n\nEnter API ID: "))
API_HASH = input("Enter API HASH: ")
with Client(':memory:', api_id=API_KEY, api_hash=API_HASH) as app:
    print(app.export_session_string())
    print("Your Pyrogram String Session Generated Successfully, Check Your Save Message -!")
    session = app.export_session_string()
    a = app.send_message("me", "`{}`".format(app.export_session_string()))
    app.send_message(
        chat_id=a.chat.id,
        text="**Here Is Your Pyrogram String Session, Don't Share Any Where -! \n\n © @RiZoeLX**",
        reply_to_message_id=a.message_id)
