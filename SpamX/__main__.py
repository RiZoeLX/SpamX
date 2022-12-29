
from . import *

if DATABASE_URL:
   from .database import users_db
   print("SpamX - [INFO]: Adding all sudos in DB!")
   for x in sudoser:
      users_db.addsudo(x)
     
if __name__ == "__main__":
    Run_SpamX()
