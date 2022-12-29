from SpamX.config import *
from pyrogram import Client

"""Starting all clients"""
   
if  ":" in CLIENT:
   RiZoeL = Client('SpamX', api_id=API_ID, api_hash=API_HASH, bot_token=CLIENT, plugins=dict(root="SpamX.modules.for_bot"))
   print("SpamX - [INFO]: Bot token 1 Found")
else:
   RiZoeL = Client('CLIENT', api_id = API_ID, api_hash = API_HASH, session_string=CLIENT, plugins=dict(root="SpamX.modules.for_id"))
   print("SpamX - [INFO]: Client 1 Found")


if CLIENT2:
   if ":" in CLIENT2:
      RiZoeL2 = Client('SpamX2', api_id=API_ID, api_hash=API_HASH, bot_token=CLIENT2, plugins=dict(root="SpamX.modules.for_bot"))
      print("SpamX - [INFO]: Bot token 2 Found")
   else:
      RiZoeL2 = Client('CLIENT2', api_id = API_ID, api_hash = API_HASH, session_string=CLIENT2, plugins=dict(root="SpamX.modules.for_id"))
      print("SpamX - [INFO]: Client 2 Found")
else:
   RiZoeL2 = None
         
   
if CLIENT3:
   if ":" in CLIENT3:
     RiZoeL3 = Client('SpamX3', api_id=API_ID, api_hash=API_HASH, bot_token=CLIENT3, plugins=dict(root="SpamX.modules.for_bot"))
     print("SpamX - [INFO]: Bot token 3 Found")
   else:
     RiZoeL3 = Client('CLIENT3', api_id = API_ID, api_hash = API_HASH, session_string=CLIENT3, plugins=dict(root="SpamX.modules.for_id"))
     print("SpamX - [INFO]: Client 3 Found")
else:
   RiZoeL3 = None
         

if CLIENT4:
   if ":" in CLIENT4:
      RiZoeL4 = Client('SpamX4', api_id=API_ID, api_hash=API_HASH, bot_token=CLIENT4, plugins=dict(root="SpamX.modules.for_bot"))
      print("SpamX - [INFO]: Bot token 4 Found")
   else:
      RiZoeL4 = Client('CLIENT4', api_id = API_ID, api_hash = API_HASH, session_string=CLIENT4, plugins=dict(root="SpamX.modules.for_id"))
      print("SpamX - [INFO]: Client 4 Found")
else:
   RiZoeL4 = None
         

if CLIENT5:
   if ":" in CLIENT5:
      RiZoeL5 = Client('SpamX5', api_id=API_ID, api_hash=API_HASH, bot_token=CLIENT5, plugins=dict(root="SpamX.modules.for_bot"))
      print("SpamX - [INFO]: Bot token 5 Found")
   else:
      RiZoeL5 = Client('CLIENT5', api_id = API_ID, api_hash = API_HASH, session_string=CLIENT5, plugins=dict(root="SpamX.modules.for_id"))
      print("SpamX - [INFO]: Client 5 Found")
else:
   RiZoeL5 = None
           

if CLIENT6:
   if ":" in CLIENT6:
      RiZoeL6 = Client('SpamX6', api_id=API_ID, api_hash=API_HASH, bot_token=CLIENT6, plugins=dict(root="SpamX.modules.for_bot"))
      print("SpamX - [INFO]: Bot token 6 Found")
   else:
      RiZoeL6 = Client('CLIENT6', api_id = API_ID, api_hash = API_HASH, session_string=CLIENT6, plugins=dict(root="SpamX.modules.for_id"))
      print("SpamX - [INFO]: Client 6 Found")
else:
   RiZoeL6 = None
             

if CLIENT7:
   if ":" in CLIENT7:
      RiZoeL7 = Client('SpamX7', api_id=API_ID, api_hash=API_HASH, bot_token=CLIENT7, plugins=dict(root="SpamX.modules.for_bot"))
      print("SpamX - [INFO]: Bot token 7 Found")
   else:
      RiZoeL7 = Client('CLIENT7', api_id = API_ID, api_hash = API_HASH, session_string=CLIENT7, plugins=dict(root="SpamX.modules.for_id"))
      print("SpamX - [INFO]: Client 7 Found")
else:
   RiZoeL7 = None
             

if CLIENT8:
    if ":" in CLIENT8:
      RiZoeL8 = Client('SpamX8', api_id=API_ID, api_hash=API_HASH, bot_token=CLIENT8, plugins=dict(root="SpamX.modules.for_bot"))
      print("SpamX - [INFO]: Bot token 8 Found")
    else:
      RiZoeL8 = Client('CLIENT8', api_id = API_ID, api_hash = API_HASH, session_string=CLIENT8, plugins=dict(root="SpamX.modules.for_id"))
      print("SpamX - [INFO]: Client 8 Found")
else:
   RiZoeL8 = None
             

if CLIENT9:
   if ":" in CLIENT9:
      RiZoeL9 = Client('SpamX9', api_id=API_ID, api_hash=API_HASH, bot_token=CLIENT9, plugins=dict(root="SpamX.modules.for_bot"))
      print("SpamX - [INFO]: Bot token 9 Found")
   else:
      RiZoeL9 = Client('CLIENT9', api_id = API_ID, api_hash = API_HASH, session_string=CLIENT9, plugins=dict(root="SpamX.modules.for_id"))
      print("SpamX - [INFO]: Client 9 Found")
else:
   RiZoeL9 = None
             

if CLIENT10:
   if ":" in CLIENT10:
      RiZoeL10 = Client('SpamX10', api_id=API_ID, api_hash=API_HASH, bot_token=CLIENT10, plugins=dict(root="SpamX.modules.for_bot"))
      print("SpamX - [INFO]: Bot token 10 Found")
   else:
      RiZoeL10 = Client('CLIENT10', api_id = API_ID, api_hash = API_HASH, session_string=CLIENT10, plugins=dict(root="SpamX.modules.for_id"))
      print("SpamX - [INFO]: Client 10 Found")
else:
   RiZoeL10 = None             

if CLIENT11:
   if ":" in CLIENT11:
      RiZoeL11 = Client('SpamX11', api_id=API_ID, api_hash=API_HASH, bot_token=CLIENT11, plugins=dict(root="SpamX.modules.for_bot"))
      print("SpamX - [INFO]: Bot token 11 Found")
   else:
      RiZoeL11 = Client('CLIENT11', api_id = API_ID, api_hash = API_HASH, session_string=CLIENT11, plugins=dict(root="SpamX.modules.for_id"))
      print("SpamX - [INFO]: Client 11 Found")
else:
   RiZoeL11 = None
             

if CLIENT12:
   if ":" in CLIENT12:
      RiZoeL12 = Client('SpamX12', api_id=API_ID, api_hash=API_HASH, bot_token=CLIENT12, plugins=dict(root="SpamX.modules.for_bot"))
      print("SpamX - [INFO]: Bot token 12 Found")
   else:
      RiZoeL12 = Client('CLIENT12', api_id = API_ID, api_hash = API_HASH, session_string=CLIENT12, plugins=dict(root="SpamX.modules.for_id"))
      print("SpamX - [INFO]: Client 12 Found")
else:
   RiZoeL12 = None
             

if CLIENT13:
   if ":" in CLIENT13:
      RiZoeL13 = Client('SpamX13', api_id=API_ID, api_hash=API_HASH, bot_token=CLIENT13, plugins=dict(root="SpamX.modules.for_bot"))
      print("SpamX - [INFO]: Bot token 13 Found")
   else:
      RiZoeL13 = Client('CLIENT13', api_id = API_ID, api_hash = API_HASH, session_string=CLIENT13, plugins=dict(root="SpamX.modules.for_id"))
      print("SpamX - [INFO]: Client 13 Found")
else:
      RiZoeL13 = None
             

if CLIENT14:
   if ":" in CLIENT14:
      RiZoeL14 = Client('SpamX14', api_id=API_ID, api_hash=API_HASH, bot_token=CLIENT14, plugins=dict(root="SpamX.modules.for_bot"))
      print("SpamX - [INFO]: Bot token 14 Found")
   else:
      RiZoeL14 = Client('CLIENT14', api_id = API_ID, api_hash = API_HASH, session_string=CLIENT14, plugins=dict(root="SpamX.modules.for_id"))
      print("SpamX - [INFO]: Client 14 Found")
else:
   RiZoeL14 = None
             

if CLIENT15:
   if ":" in CLIENT15:
      RiZoeL15 = Client('SpamX15', api_id=API_ID, api_hash=API_HASH, bot_token=CLIENT15, plugins=dict(root="SpamX.modules.for_bot"))
      print("SpamX - [INFO]: Bot token 15 Found")
   else:
      RiZoeL15 = Client('CLIENT15', api_id = API_ID, api_hash = API_HASH, session_string=CLIENT15, plugins=dict(root="SpamX.modules.for_id"))
      print("SpamX - [INFO]: Client 15 Found")
else:
   RiZoeL15 = None
             

if CLIENT16:
   if ":" in CLIENT16:
      RiZoeL16 = Client('SpamX16', api_id=API_ID, api_hash=API_HASH, bot_token=CLIENT16, plugins=dict(root="SpamX.modules.for_bot"))
      print("SpamX - [INFO]: Bot token 16 Found")
   else:
      RiZoeL16 = Client('CLIENT16', api_id = API_ID, api_hash = API_HASH, session_string=CLIENT16, plugins=dict(root="SpamX.modules.for_id"))
      print("SpamX - [INFO]: Client 16 Found")
else:
   RiZoeL16 = None
             

if CLIENT17:
   if ":" in CLIENT17:
      RiZoeL17 = Client('SpamX17', api_id=API_ID, api_hash=API_HASH, bot_token=CLIENT17, plugins=dict(root="SpamX.modules.for_bot"))
      print("SpamX - [INFO]: Bot token 17 Found")
   else:
      RiZoeL17 = Client('CLIENT17', api_id = API_ID, api_hash = API_HASH, session_string=CLIENT17, plugins=dict(root="SpamX.modules.for_id"))
      print("SpamX - [INFO]: Client 17 Found")
else:
   RiZoeL17 = None
             

if CLIENT18:
   if ":" in CLIENT18:
      RiZoeL18 = Client('SpamX18', api_id=API_ID, api_hash=API_HASH, bot_token=CLIENT18, plugins=dict(root="SpamX.modules.for_bot"))
      print("SpamX - [INFO]: Bot token 18 Found")
   else:
      RiZoeL18 = Client('CLIENT18', api_id = API_ID, api_hash = API_HASH, session_string=CLIENT18, plugins=dict(root="SpamX.modules.for_id"))
      print("SpamX - [INFO]: Client 18 Found")
else:
   RiZoeL18 = None
           

if CLIENT19:
   if ":" in CLIENT19:
      RiZoeL19 = Client('SpamX19', api_id=API_ID, api_hash=API_HASH, bot_token=CLIENT19, plugins=dict(root="SpamX.modules.for_bot"))
      print("SpamX - [INFO]: Bot token 19 Found")
   else:
      RiZoeL19 = Client('CLIENT19', api_id = API_ID, api_hash = API_HASH, session_string=CLIENT19, plugins=dict(root="SpamX.modules.for_id"))
      print("SpamX - [INFO]: Client 19 Found")
else:
   RiZoeL19 = None
        

if CLIENT20:
   if ":" in CLIENT20:
      RiZoeL20 = Client('SpamX20', api_id=API_ID, api_hash=API_HASH, bot_token=CLIENT20, plugins=dict(root="SpamX.modules.for_bot"))
      print("SpamX - [INFO]: Bot token 20 Found")
   else:
      RiZoeL20 = Client('CLIENT20', api_id = API_ID, api_hash = API_HASH, session_string=CLIENT20, plugins=dict(root="SpamX.modules.for_id"))
      print("SpamX - [INFO]: Client 20 Found")
else:
   RiZoeL20 = None

