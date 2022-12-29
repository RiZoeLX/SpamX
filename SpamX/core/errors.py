""" RiZoeLX 2022-2023 © SpamX """

import re


def user_errors(error):
    if '[400 USERNAME_NOT_OCCUPIED]' in str(error):
       return "You didn't provide username"
    elif '[400 USERNAME_INVALID]' in str(error):
       return "Username is invalid"
    elif '[400 PEER_ID_INVALID]' in str(error):
       return "Invalid User ID!"
    else:
       return f"**Unknown Error:** \n\n {error}"

def join_errors(error):
    if '[400 USERNAME_NOT_OCCUPIED]' in str(error):
       return "You didn't Provide Username to join!"
    elif '[400 USERNAME_INVALID]' in str(error):
       return "Ahh.. Username is invalid"
    elif '[400 INVITE_REQUEST_SENT]' in str(error):
       return "Join request sent!"
    elif 'Username not found' in str(error):
       return "I'm banned in that group 🫠"
    else:
       return f"**Unknown Error:** \n\n {error}" 

def leave_errors(error):
    if '[400 PEER_ID_INVALID]' in str(error):
       return "Wrong Chat ID!"
    elif '[400 USER_NOT_PARTICIPANT]' in str(error):
       return "I'm not in that group 🫠"
    elif '[400 USERNAME_INVALID]' in str(error):
       return "Ahh.. Username is invalid"
    else:
       return f"**Unknown Error:** \n\n {error}" 
