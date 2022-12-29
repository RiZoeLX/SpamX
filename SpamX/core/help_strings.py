import os, re


hndlr = os.getenv("HNDLR")
if not hndlr:
  hndlr = "."

help_text = f"""
**Help menu of SpamX!**

Functions/Modules available ⬇️

=> `spam` , `raid` , `owner` , `direct_message` , `admin` , `core` , `sudos` , `global` , `profile` , `joinleave` , `info`

Type `{hndlr}help` (Module name) | Bot'll give info/usage of
that module.

Example: `{hndlr}help core`
"""

spam_text = f"""
**Module name: Spam**

Available commands and there Usage ⬇️

•) {hndlr}spam [counts] [message] 
•) {hndlr}delayspam [delay in secs.] [Counts] [message]
•) {hndlr}pornspam [counts]
•) {hndlr}hange [counts]
•) {hndlr}uspam [message]
•) {hndlr}abuse [counts or leave]
"""

raid_text = f"""
**Module name: Raid**

Available commands and there Usage ⬇️

•) {hndlr}raid [counts] [username or reply to user]
•) {hndlr}uraid [Username or reply to user]
•) {hndlr}replyraid [username or reply to user]
•) {hndlr}dreplyraid [username or reply to user]
"""

dm_text = f"""
**Module name: Direct Message**

Available commands and there Usage ⬇️

•) {hndlr}dm [username or reply to user] [message]
•) {hndlr}dmspam [user] [counts] [message]
•) {hndlr}dmraid [counts] [username or reply to user]
"""

admin_text = f"""
**Module name: Admin**

Available commands and there Usage ⬇️

•) {hndlr}ban [user]
•) {hndlr}unban [user]
•) {hndlr}promote [user]
•) {hndlr}demote [user]
•) {hndlr}pin [reply to message]
•) {hndlr}unpin [reply to message]
•) {hndlr}purge [reply to message]
"""

core_text = f"""
**Module name: Core**

Available commands and there Usage ⬇️

•) {hndlr}report [user] [R7 ban code] [telegraph link as proof]
•) {hndlr}stats
•) {hndlr}setvar [var name] [key value] (It may be useful)
•) {hndlr}getvar (to get all Vars name)
•) {hndlr}limit (to check @Spambot limit)
•) {hndlr}telegraph [reply to Media]
"""

sudos_text = f"""
**Module name: Sudos**

Available commands and there Usage ⬇️

•) {hndlr}addsudo [user] (Fill DATABASE_URL for smooth use)
•) {hndlr}rmsudo [user] (Fill DATABASE_URL for smooth use)
•) {hndlr}sudolist
"""

global_text = f"""
**Module name: Global**

Available commands and there Usage ⬇️

•) {hndlr}gban [user] (DATABASE_URL required in this CMD)
•) {hndlr}ungban [user] (DATABASE_URL required in this CMD)
•) {hndlr}gbanlist
•) {hndlr}gpromote [user]
•) {hndlr}Gdemote [user]
"""

profile_text = f"""
**Module name: Profile**

Available commands and there Usage ⬇️

•) {hndlr}setpic [reply to Media]
•) {hndlr}setname [First name] [last name (optionsi) ]
•) {hndlr}setbio [New bio]
•) {hndlr}clone [user] (to clone someone's profile]
•) {hndlr}revert (To remove clone)
"""

owner_text = f"""
**Module name: Owner stuff**

Available commands and there Usage ⬇️

•) {hndlr}eval [code]
•) {hndlr}broadcast [message]
•) {hndlr}msgall [message] (in groups only)
•) {hndlr}scrape [From group] 
•) {hndlr}banall
"""

joinleave_text = f"""
**Module name: Join leave**

Available commands and there Usage ⬇️

•) {hndlr}join [group username]
•) {hndlr}leave [group username or ID]
"""

info_text = f"""
**Module name: Info**

Available commands and there Usage ⬇️

•) {hndlr}SpamX
•) {hndlr}info [User]
•) {hndlr}id [user]
"""

def check_string(text):
   if re.search("spam".lower(), text.lower()):
      return "spam"
   if re.search("raid".lower(), text.lower()):
      return "raid"
   if re.search("owner".lower(), text.lower()):
      return "owner"
   if re.search("direct|dm|direct_message".lower(), text.lower()):
      return "dm"
   if re.search("admin".lower(), text.lower()):
      return "admin"
   if re.search("core".lower(), text.lower()):
      return "core"
   if re.search("sudos|sudo".lower(), text.lower()):
      return "sudos"
   if re.search("global".lower(), text.lower()):
      return "global"
   if re.search("profile".lower(), text.lower()):
      return "profile"
   if re.search("join|leave|joinleave".lower(), text.lower()):
      return "joinleave"
   if re.search("info".lower(), text.lower()):
      return "info"

async def help_return(text):
   if check_string(text) == "spam":
      return spam_text
   elif check_string(text) == "raid":
      return raid_text
   elif check_string(text) == "dm":
      return dm_text
   elif check_string(text) == "admin":
      return admin_text
   elif check_string(text) == "core":
      return core_text
   elif check_string(text) == "sudos":
      return sudos_text
   elif check_string(text) == "global":
      return global_text
   elif check_string(text) == "profile":
      return profile_text
   elif check_string(text) == "owner":
      return owner_text
   elif check_string(text) == "joinleave":
      return joinleave_text
   elif check_string(text) == "info":
      return info_text
   else:
      return help_text
