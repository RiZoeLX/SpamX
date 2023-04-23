# SpamX Multiple String Generator 

from pyrogram import Client
#import tgcrypto

ID = int(input(" \n Send Api Id To Generate String Sessions: "))
HASH = str(input(" \n Send Api Hash To Generate String Sessions: "))

try:
     number_to_add = int(input(" \n Enter number of accounts you want to generate string:"))
     whom = input(" \n Enter Your Username or User id so, Client can forward all sessions to you else press enter: ")
     for i in range(number_to_add):
            RiZoeL = Client(name="RiZoeL", api_id=ID, api_hash=HASH, in_memory=True)
            RiZoeL.start()
            s = RiZoeL.export_session_string()
            sess = str(s)
            if whom:
                id = RiZoeL.get_users(whom).id
                RiZoeL.send_message(id, f"**Pyrogram String Session** \n\n `{sess}` \n\n © @RiZoeLX")
            else:
                RiZoeL.send_message("me", f"**Pyrogram String Session** \n\n `{sess}` \n\n © @RiZoeLX")
       
     if whom:
           print(f"All Session has been sent to {whom}")
     else:
         print("All Sessions has been sent to saved message")
         
except Exception as a:
   print(a)    
