import time

from platform import python_version

from SpamX.functions.database import dataBase
from SpamX.config import PING_MSG

from pyrogram import __version__


# --- start time --- #
StartTime = time.time()

# --- versions --- #
version = {
    "SpamX": "v2.0",
    "pyrogram": __version__,
    "python": python_version(),
}

UpdateChannel = "RiZoeL_X"
SupportGroup = "RiZoeLXSupport"

activeTasks: dict = {}
dataBase = dataBase

#  --- etx
if PING_MSG:
    pingMSG = str(PING_MSG)
else:
    pingMSG = "SpamX"