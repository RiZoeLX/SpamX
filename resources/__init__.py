""" RiZoeLX 2022-2023 © SpamX """

import os, time, sys
from sys import stdout

os.system("clear")

# Color snippets
black="\033[0;30m"
red="\033[0;31m"
bred="\033[1;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
byellow="\033[1;33m"
blue="\033[0;34m"
bblue="\033[1;34m"
purple="\033[0;35m"
bpurple="\033[1;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
nc="\033[00m"

version="2.1"

ask  =     f"{green}[{white}?{green}] {yellow}"
success = f"{yellow}[{white}√{yellow}] {green}"
error  =    f"{blue}[{white}!{blue}] {red}"
info  =   f"{yellow}[{white}+{yellow}] {cyan}"
info2  =   f"{green}[{white}•{green}] {purple}"

spamx_logo = f'''
{bred}┏━━━┓━━━━━━━━━━━━━━━┏┓━┏┓━
{bblue}┃┏━┓┃━━━━━━━━━━━━━━━┃┃━┃┃━
{yellow}┃┗━┗┛┏━━┓┏━━┓━┏━━━━┓┗━━━┛━
{bpurple}┏┓━┓┃┃┏┓┃┃┏┓┃━┃┏┓┏┓┃┏━━━┓━
{bpurple}┃┗━┛┃┃┗┛┃┃┗━┗┓┃┃┃┃┃┃┃┃━┃┃━
{byellow}┗━━━┛┃━━┛┗━━━┛┗┛┗┛┗┛┗┛━┗┛━
{bblue}━━━━━┃┃━━━━━━━━━━━━━━━━━━━
{bred}━━━━━┗┛━━━━━━━━━━━━━━━━━━━
'''

def sprint(text, second):
    for line in text + '\n':
        stdout.write(line)
        stdout.flush()
        time.sleep(second)

# Clear the screen and show logo
def clear(fast=False):
    os.system("clear")
    if fast:
        print(spamx_logo)
    else:
        sprint(spamx_logo, 0.01)

evn_vars = """
API_ID=
API_HASH=
OWNER_ID=
LOGGER_ID=
DATABASE_URL=
ASSISTANT_TOKEN=
HANDLER=
PING_MSG=
ALIVE_MSG=
ALIVE_MEDIA=
MULTITASK=
"""

def setupSpamX():
    os.system("pip3 install python-dotenv[cli]")
    clear()
    print(f'    {white}SpamX Version: v2.O \n    {white}By RiZoeLX')
    
    time.sleep(2)
    api_id = input(f"{ask}Enter API_ID: ")
    if api_id:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set API_ID {api_id}")
    else:
        print(f"{error}You have to fill this variable! all process restarting..")
        time.sleep(2)
        setupSpamX()
    api_hash = input(f"\n{ask}Enter API_HASH: ")
    if api_hash:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set API_HASH {api_hash}")
    else:
        print(f"{error}You have to fill this variable! all process restarting..")
        time.sleep(2)
        setupSpamX()
    LOGGER_ID = input(f"\n{ask}Enter Chat ID or Username of LOGGER_ID or press enter: ")
    if LOGGER_ID:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set LOGGER_ID {LOGGER_ID}")
    owner_id = input(f"\n{ask}Enter OWNER_ID: ")
    if owner_id:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set OWNER_ID {owner_id}")
    else:
        print(f"{error}You have to fill this variable! all process restarting..")
        time.sleep(2)
        setupSpamX()
    ASSISTANT_TOKEN = input(f"\n{ask}Enter bot token of ASSISTANT_TOKEN: ")
    if ASSISTANT_TOKEN:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set ASSISTANT_TOKEN {ASSISTANT_TOKEN}")
    else:
        print(f"{error}You have to fill this variable! all process restarting..")
        time.sleep(2)
        setupSpamX()

    database_url = (input(f"\n{ask}Enter Mongo/Postgres database url: "))
    if database_url:
        if "mongodb" in database_url:
            print(f"{bcyan}Got it!")
            os.system(f"dotenv set DATABASE_URL {database_url}")
        else:
            print(f"{error}Need Mongo or Postgres database url! restarting...")
            time.sleep(2)
            setupSpamX()
    else:
        print(f"{error}You have to fill this variable! all process restarting..")
        time.sleep(2)
        setupSpamX()

    print(f"{bpurple}\n\nNow, next all variables are optional press enter if yiu don't wanna fill!\n")

    cmd_hndlr = input(f"\n{ask}Enter HANDLER or press enter: ")
    if cmd_hndlr:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set HANDLER {cmd_hndlr}")
    alive_media = input(f"\n{ask}Enter Alive media (telegraph link) or press enter: ")
    if alive_media:
        print(f"{bcyan}Got it!")
        os.system(f"dotenv set ALIVE_MEDIA {alive_media}")
    alive_msg = input(f"\n{ask}Enter Alive msg or press enter: ")
    if alive_msg:
        print(f"{bcyan}Got it!")
        os.system(f"dotenv set ALIVE_MSG {alive_msg}")
    ping_msg = input(f"\n{ask}Enter Ping msg or press enter: ")
    if ping_msg:
        print(f"{bcyan}Got it!")
        os.system(f"dotenv set PING_MSG {ping_msg}")

    recheck()

def recheck():
    confim = str(input(f"\n{ask}Filled ALL Vars Correctly?: y/n: "))
    if confim.lower() == "n":
        os.system("clear")
        print(f"{info}Okay! Fill Your Vars Again")
        setupSpamX()
    elif confim.lower() == "y":
        get_start()
    else:
        print(f"\n{ask}Input Must Be Y or N")
        recheck()

def get_start():
    clear(fast=True)
    confim = str(input(f"{ask}Wanna start SpamX Now?: y/n: "))
    if confim.lower() == "y":
        os.system("pip3 install python-dotenv")
        os.system("python3 -m SpamX")
    elif confim.lower() == "n":
        print(f"\n{info}Nevermind !! You Can Start It Later With by using; python3-m SpamX\n")
        exit(2)
    else:
        os.system("clear")
        print(f"{error}\nInput Must Be y or n")
        get_start()
