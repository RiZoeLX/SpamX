import os, sys
from resources import *
 
os.system("clear")

# ------ main ------ #
start = input(f"{ask}Want to fill vars ? if yes type Y/yes else press enter: ")
if start in ['Y', 'y', 'Yes', 'YES', 'yes']:
  if os.path.exists(".env"):
    x = open(".env", "r")
    check = x.read()
    lines = check.splitlines()
    x.close()
    if not len(lines) == 30:
        os.system("rm -rf .env")
        y = open(".env", "w")
        y.write(evn_vars)
        y.close()
        os.system("clear")
        SpamX_Setup()
    else:
        os.system("clear")
        SpamX_Setup()
  elif not os.path.exists(".env"):
    y = open(".env", "w")
    y.write(evn_vars)
    y.close()
    os.system("clear")
    SpamX_Setup()
else:
  clear()
  os.system("python3 -m SpamX")
