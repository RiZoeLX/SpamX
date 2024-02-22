import os
from resources import setupSpamX, evn_vars, clear, ask

os.system("clear")

# ------ main ------ #
start = str(input(f"{ask}Want to fill vars ? if yes type Y/yes else press enter: "))
if start.lower() in ['y', 'yes']:
  if os.path.exists(".env"):
    x = open(".env", "r")
    check = x.read()
    lines = check.splitlines()
    x.close()
    if not len(lines) == 11:
        os.system("rm -rf .env")
        y = open(".env", "w")
        y.write(evn_vars)
        y.close()
        os.system("clear")
        setupSpamX()
    else:
        os.system("clear")
        setupSpamX()
  elif not os.path.exists(".env"):
    y = open(".env", "w")
    y.write(evn_vars)
    y.close()
    os.system("clear")
    setupSpamX()
else:
  clear()
  os.system("python3 -m SpamX")
