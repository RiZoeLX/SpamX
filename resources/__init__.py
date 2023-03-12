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
SUDO_USERS=
ALIVE_PIC=
ALIVE_MSG=
PING_MSG=
LOGS_CHANNEL=
DATABASE_URL=
CLIENT=
CLIENT2=
CLIENT3=
CLIENT4=
CLIENT5=
CLIENT6=
CLIENT7=
CLIENT8=
CLIENT9=
CLIENT10=
CLIENT11=
CLIENT12=
CLIENT13=
CLIENT14=
CLIENT15=
CLIENT16=
CLIENT17=
CLIENT18=
CLIENT19=
CLIENT20=
HNDLR=
"""

def SpamX_Setup():
    os.system("pip3 install python-dotenv[cli]")
    clear()
    print(f'    {white}SpamX Version: v0.5 \n    {white}By RiZoeX')
    
    time.sleep(2)
    api_id = input(f"{ask}Enter API_ID: ")
    if api_id:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set API_ID {api_id}")
    else:
        print(f"{error}You have to fill this variable! all process restarting..")
        time.sleep(2)
        SpamX_Setup()
    api_hash = input(f"\n{ask}Enter API_HASH: ")
    if api_hash:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set API_HASH {api_hash}")
    else:
        print(f"{error}You have to fill this variable! all process restarting..")
        time.sleep(2)
        SpamX_Setup()
    ALIVE_PIC = input(f"\n{ask}Enter ALIVE_PIC (Telegraph link) or press enter!: ")
    if ALIVE_PIC:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set ALIVE_PIC {ALIVE_PIC}")
    ALIVE_MSG = input(f"\n{ask}Enter ALIVE_MSG or press enter: ").replace(" ", "\ ")
    if ALIVE_MSG:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set ALIVE_MSG {ALIVE_MSG}")
    PING_MSG = input(f"\n{ask}Enter PING_MSG or press enter: ").replace(" ", "\ ")
    if PING_MSG:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set PING_MSG {PING_MSG}")
    LOGS_CHANNEL = input(f"\n{ask}Enter Chat ID or Username of LOGS_CHANNEL or press enter: ")
    if LOGS_CHANNEL:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set LOGS_CHANNEL {LOGS_CHANNEL}")
    owner_id = input(f"\n{ask}Enter OWNER_ID: ")
    if owner_id:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set OWNER_ID {owner_id}")
    else:
        print(f"{error}You have to fill this variable! all process restarting..")
        time.sleep(2)
        SpamX_Setup()
    sudo_users = input(f"\n{ask}Enter SUDO_USERS (space by space) or press enter: ").replace(" ", "\ ")
    if sudo_users:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set SUDO_USERS {sudo_users}")
    cmd_hndlr = input(f"\n{ask}Enter HNDLR or press enter: ")
    if cmd_hndlr:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set HNDLR {cmd_hndlr}")
    CLIENT = input(f"\n{ask}Enter session or bot token of CLIENT: ")
    if CLIENT:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set CLIENT {CLIENT}")
    else:
        print(f"{error}You have to fill this variable! all process restarting..")
        time.sleep(2)
        SpamX_Setup()
    CLIENT2 = input(f"\n{ask}Enter session or bot token of CLIENT2 or press enter: ")
    if CLIENT2:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set CLIENT2 {CLIENT2}")
    CLIENT3 = input(f"\n{ask}Enter session or bot token of CLIENT3 or press enter: ")
    if CLIENT3:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set CLIENT3 {CLIENT3}")
    CLIENT4 = input(f"\n{ask}Enter session or bot token of CLIENT4 or press enter: ")
    if CLIENT4:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set CLIENT4 {CLIENT4}")
    CLIENT5 = input(f"\n{ask}Enter session or bot token of CLIENT5 or press enter: ")
    if CLIENT5:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set CLIENT5 {CLIENT5}")
    CLIENT6 = input(f"\n{ask}Enter session or bot token of CLIENT6 or press enter: ")
    if CLIENT6:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set CLIENT6 {CLIENT6}")
    CLIENT7 = input(f"\n{ask}Enter session or bot token of CLIENT7 or press enter: ")
    if CLIENT7:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set CLIENT7 {CLIENT7}")
    CLIENT8 = input(f"\n{ask}Enter session or bot token of CLIENT8 or press enter: ")
    if CLIENT8:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set CLIENT8 {CLIENT8}")
    CLIENT9 = input(f"\n{ask}Enter session or bot token of CLIENT9 or press enter: ")
    if CLIENT9:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set CLIENT9 {CLIENT9}")
    CLIENT10 = input(f"\n{ask}Enter session or bot token of CLIENT10 or press enter: ")
    if CLIENT10:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set CLIENT10 {CLIENT10}")
    CLIENT11 = input(f"\n{ask}Enter session or bot token of CLIENT11 or press enter: ")
    if CLIENT11:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set CLIENT11 {CLIENT11}")
    CLIENT12 = input(f"\n{ask}Enter session or bot token of CLIENT12 or press enter: ")
    if CLIENT12:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set CLIENT12 {CLIENT12}")
    CLIENT13 = input(f"\n{ask}Enter session or bot token of CLIENT13 or press enter: ")
    if CLIENT13:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set CLIENT13 {CLIENT13}")
    CLIENT14 = input(f"\n{ask}Enter session or bot token of CLIENT14 or press enter: ")
    if CLIENT14:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set CLIENT14 {CLIENT14}")
    CLIENT15 = input(f"\n{ask}Enter session or bot token of CLIENT15 or press enter: ")
    if CLIENT15:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set CLIENT15 {CLIENT15}")
    CLIENT16 = input(f"\n{ask}Enter session or bot token of CLIENT16 or press enter: ")
    if CLIENT16:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set CLIENT16 {CLIENT16}")
    CLIENT17 = input(f"\n{ask}Enter session or bot token of CLIENT17 or press enter: ")
    if CLIENT17:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set CLIENT17 {CLIENT17}")
    CLIENT18 = input(f"\n{ask}Enter session or bot token of CLIENT18 or press enter: ")
    if CLIENT18:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set CLIENT18 {CLIENT18}")
    CLIENT19 = input(f"\n{ask}Enter session or bot token of CLIENT19 or press enter: ")
    if CLIENT19:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set CLIENT19 {CLIENT19}")
    CLIENT20 = input(f"\n{ask}Enter session or bot token of CLIENT20 or press enter: ")
    if CLIENT20:
        print(f"{bcyan}Got it! Fill next value")
        os.system(f"dotenv set CLIENT20 {CLIENT20}")
    database_url = input(f"\n{ask}Enter Postgres database url or press enter: ")
    if database_url:
        if 'postgresql' in database_url or 'postgres' in database_url:
           print(f"{bcyan}Got it!")
           os.system(f"dotenv set DATABASE_URL {database_url}")
        else:
           print(f"{error}Need Postgres database url, fill DATABASE_URL manually")
    recheck()

def recheck():
    Recheck = input(f"\n{ask}Filled ALL Vars Correctly?: y/n: ")
    if Recheck.lower() == "n":
        os.system("clear")
        print(f"{info}Okay! Fill Your Vars Again")
        SpamX_Setup()
    elif Recheck.lower() == "y":
        
        get_start()
    else:
        print(f"\n{ask}Input Must Be Y or N")
        recheck()

def get_start():
    clear(fast=True)
    question = input(f"{ask}Wanna start SpamX Now?: y/n: ")
    if question.lower() == "y":
        os.system("pip3 install python-dotenv")
        os.system("python3 -m SpamX")
    elif question.lower() == "n":
        print(f"\n{info}Nevermind !! You Can Start It Later With by using; python3-m SpamX\n")
        exit(2)
    else:
        os.system("clear")
        print(f"{error}\nInput Must Be y or n")
        get_start()
