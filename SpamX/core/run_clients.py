
# Versions

from .clients import *
from SpamX.config import *

from .version import __version__
from RiZoeLX import __version__ as rizoelx_vr
from pyrogram import __version__ as pyro_vr
import platform

from RiZoeLX.functions import start_spamX
from pyrogram import idle

def Run_SpamX():
    if CLIENT:
       if ":" in CLIENT:
         start_spamX(RiZoeL, "token")
       else:
         start_spamX(RiZoeL, "session")

    if CLIENT2:
       if ":" in CLIENT2:
         start_spamX(RiZoeL2, "token")
       else:
         start_spamX(RiZoeL2, "session")
         
    if CLIENT3:
       if ":" in CLIENT3:
         start_spamX(RiZoeL3, "token")
       else:
         start_spamX(RiZoeL3, "session")
         
    if CLIENT4:
       if ":" in CLIENT4:
         start_spamX(RiZoeL4, "token")
       else:
         start_spamX(RiZoeL4, "session")
         
    if CLIENT5:
       if ":" in CLIENT5:
         start_spamX(RiZoeL5, "token")
       else:
         start_spamX(RiZoeL5, "session")
         
    if CLIENT6:
       if ":" in CLIENT6:
         start_spamX(RiZoeL6, "token")
       else:
         start_spamX(RiZoeL6, "session")
         
    if CLIENT7:
       if ":" in CLIENT7:
         start_spamX(RiZoeL7, "token")
       else:
         start_spamX(RiZoeL7, "session")
         
    if CLIENT8:
       if ":" in CLIENT8:
         start_spamX(RiZoeL8, "token")
       else:
         start_spamX(RiZoeL8, "session")
         
    if CLIENT9:
       if ":" in CLIENT9:
         start_spamX(RiZoeL9, "token")
       else:
         start_spamX(RiZoeL9, "session")

    if CLIENT10:
       if ":" in CLIENT10:
         start_spamX(RiZoeL10, "token")
       else:
         start_spamX(RiZoeL10, "session")
         
    if CLIENT11:
       if ":" in CLIENT11:
         start_spamX(RiZoeL11, "token")
       else:
         start_spamX(RiZoeL11, "session")
         
    if CLIENT12:
       if ":" in CLIENT12:
         start_spamX(RiZoeL12, "token")
       else:
         start_spamX(RiZoeL12, "session")
         
    if CLIENT13:
       if ":" in CLIENT13:
         start_spamX(RiZoeL13, "token")
       else:
         start_spamX(RiZoeL13, "session")
         
    if CLIENT14:
       if ":" in CLIENT14:
         start_spamX(RiZoeL14, "token")
       else:
         start_spamX(RiZoeL14, "session")
         
    if CLIENT15:
       if ":" in CLIENT15:
         start_spamX(RiZoeL15, "token")
       else:
         start_spamX(RiZoeL15, "session")
         
    if CLIENT16:
       if ":" in CLIENT16:
         start_spamX(RiZoeL16, "token")
       else:
         start_spamX(RiZoeL16, "session")
         
    if CLIENT17:
       if ":" in CLIENT17:
         start_spamX(RiZoeL17, "token")
       else:
         start_spamX(RiZoeL17, "session")
         
    if CLIENT18:
       if ":" in CLIENT18:
         start_spamX(RiZoeL18, "token")
       else:
         start_spamX(RiZoeL18, "session")
         
    if CLIENT19:
       if ":" in CLIENT19:
         start_spamX(RiZoeL19, "token")
       else:
         start_spamX(RiZoeL19, "session")

    if CLIENT20:
       if ":" in CLIENT20:
         start_spamX(RiZoeL20, "token")
       else:
         start_spamX(RiZoeL20, "session")
    
    print(f"SpamX - [INFO]: Python Version - {platform.python_version()}")
    print(f"SpamX - [INFO]: SpamX Version - {__version__}")
    print(f"SpamX - [INFO]: pyRiZoeLX Version - {rizoelx_vr}")
    print(f"SpamX - [INFO]: Pyrogram Version - {pyro_vr}")
    print(""" \n\n
     ╒═══════════════════════════╕
      Your SpamX has been Deployed!!
      Visit @RiZoeLX for updates!
     ╘═══════════════════════════╛
    """)
    idle()
