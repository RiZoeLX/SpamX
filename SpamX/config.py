""" RiZoeLX 2022 © SpamX """
import os
import sys
import re

from dotenv import load_dotenv
from pyrogram import Client
from RiZoeLX.functions import check_logchannel

if os.path.exists(".env"):
    load_dotenv(".env")

# -------------CONFIGS--------------------
API_ID = int(os.getenv("API_ID", ""))
if not API_ID:
   print("SpamX [INFO]: You didn't fill API_ID var!")
   sys.exit()
API_HASH = os.getenv("API_HASH", "")
if not API_HASH:
   print("SpamX [INFO]: You didn't fill API_HASH var!")
   sys.exit()
ALIVE_PIC = os.getenv("ALIVE_PIC", "")
ALIVE_MSG = os.getenv("ALIVE_MSG", "")
PING_MSG = os.getenv("PING_MSG", "")
CLIENT = os.getenv("CLIENT", None)
if not CLIENT:
   print("SpamX [INFO]: You have to fill CLIENT var!")
   sys.exit()
CLIENT2 = os.getenv("CLIENT2", None)
CLIENT3 = os.getenv("CLIENT3", None)
CLIENT4 = os.getenv("CLIENT4", None)
CLIENT5 = os.getenv("CLIENT5", None)
CLIENT6 = os.getenv("CLIENT6", None)
CLIENT7 = os.getenv("CLIENT7", None)
CLIENT8 = os.getenv("CLIENT8", None)
CLIENT9 = os.getenv("CLIENT9", None)
CLIENT10 = os.getenv("CLIENT10", None)
CLIENT11 = os.getenv("CLIENT11", None)
CLIENT12 = os.getenv("CLIENT12", None)
CLIENT13 = os.getenv("CLIENT13", None)
CLIENT14 = os.getenv("CLIENT14", None)
CLIENT15 = os.getenv("CLIENT15", None)
CLIENT16 = os.getenv("CLIENT16", None)
CLIENT17 = os.getenv("CLIENT17", None)
CLIENT18 = os.getenv("CLIENT18", None)
CLIENT19 = os.getenv("CLIENT19", None)
CLIENT20 = os.getenv("CLIENT20", None)
auto_re = os.getenv("AUTO_REACT_CHATS", None)
LOGS_CHANNEL = os.getenv("LOGS_CHANNEL", None)
if LOGS_CHANNEL:
   if check_logchannel(LOGS_CHANNEL):
      print("SpamX [INFO]: You Can't Use That Chat As A Log Channel -!")
      print("SpamX [INFO]: Change Logs Channel Id else Bot Could not be start")
      sys.exit()
    
HNDLR = os.getenv("HNDLR", None)
if not HNDLR:
   HNDLR = "."
OWNER_ID = int(os.environ.get("OWNER_ID", None))
if not OWNER_ID:
   print("SpamX [INFO]: You didn't fill OWNER_ID var!")
   sys.exit()
SUDO_USERS = os.getenv("SUDO_USERS", None)

#Optional
DATABASE_URL = os.getenv("DATABASE_URL", None)
if DATABASE_URL:
   os.system("pip3 install sqlalchemy==1.3.20")
   os.system("pip3 install psycopg2-binary") 
   if 'postgres' in DATABASE_URL and 'postgresql' not in DATABASE_URL:
      DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")

WELCOME = os.getenv("WELCOME", None)
if WELCOME:
   if re.search("off|no|disable|false".lower(), WELCOME.lower()):
      group_welcome = False 
   else:
      group_welcome = True
else:
   group_welcome = True

