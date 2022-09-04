import os
import sys
import asyncio
import re
from random import choice
from SpamX import (HNDLR, SUDO_USERS)
from pyrogram import Client, filters
from pyrogram.types import Message
from SpamX.data import *

WORD = [ "AJA", "TERI", "MAA", "KI", "CHUT", "FAAD", "DUNGA", "HIJDE", "TERA", "BAAP", "HU", "KIDXX", "SPEED", "PAKAD", "BHEN KE LAUDE", "AA BETA", " ADITYA", "AAGYA", "TERI", "MAA ", "CHODNE", "AB", "TERI ", "MAA", "CHUDEGI", "KUTTE", "KI", "TARAH", "BETA", "TERI", "MAA", "KE", "BHOSDE", "ME", "JBL", "KE", "SPEAKER", "DAAL", "KAR", "BASS", "BOOSTED", "SONG", "SUNUNGA", "PURI", "RAAT", "LAGATAR", "TERI", "MAA", "KE", "SATH", "SEX", "KARUNGA🔥", "TERI", "MAA", "KE", "BOOBS", "DABAUNGA","XXX","TERI","MAA","KAA","CHUT","MARU","RANDI","KEE","PILEE","TERI","MAA","KAA","BHOSDAA","MARU","SUAR","KEE","CHODE","TERI","MAAA","KEEE","NUDES","BECHUNGA","RANDI","KEE","PILLE","TERI","MAAA","CHODU","SUAR","KEEE","PILEE","TERIII","MAAA","DAILYY","CHUDTTI","HAII","MADHARCHOD","AUKAT","BANAA","LODE","TERAA","BAAP","HUU","TERI","GFF","KAA","BHOSDAA","MARUU","MADHARCHOD","TERI ","NANAI","KAA","CHUTT","MARU","TERII","BEHEN","KAAA","BHOSDAA","MARU","RANDII","KEEE","CHODE","TERI","DADI","KAAA","BOOR","GARAM","KARR","TERE","PUREE","KHANDAN","KOOO","CHODUNGAA","BAAP","SEE","BAKCHODI","KAREGAA","SUARR","KEEE","PILLEE","NAAK","MEEE","NETAA","BAAP","KOO","KABHII","NAAH","BOLNAA","BETAA","CHUSS","LEEE","MERAA","LODAA","JAISE","ALUU","KAAA","PAKODAA","TERI","MAAA","BEHEN","GFF","NANI","DIIN","RAAT","SOTEE","JAGTEE","PELTAA","HUUU","LODEE","CHAAR","CHAWNII","GHODEE","PEEE","TUMM","MEREE","LODEE","PEE","TERI","MAA","KAAA","BOOBS","DABATA HU",]

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["abuse", "gali"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["abuse", "gali"], prefixes=HNDLR))
async def abuse(xspam: Client, e: Message): 
     counts = int(e.text[6:])
     if not counts:
          return await e.reply_text(f"**Wrong Usage** \n\n Cmd: {HNDLR}abuse (count) ")
     if int(e.chat.id) in GROUP:
          return await e.reply_text("**Sorry !! i Can't Spam Here.**")
     for _ in range(counts):
         msg = choice(WORD)
         await e.send_message(e.chat.id, msg)
         await asyncio.sleep(0.001)
