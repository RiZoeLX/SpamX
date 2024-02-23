"""
    SpamX by RiZoeLX
    Database - Used MonGo DB
"""
import os

from SpamX.config import DATABASE_URL

from pymongo import MongoClient

db_name = os.getenv("DB_NAME", "SpamX")

class MongoDB:
    def __init__(self, DB_URL) -> None:
        self.client = MongoClient(DB_URL)
        self.db = self.client[db_name]

    # --- sudo --- #
    def addSudo(self, user_id: int, rank: int = 3, promoted_by: int = None) -> None:
        self.db.sudo.insert_one(
            {
                "user_id": user_id,
                "rank": rank,
                "promoted_by": promoted_by,
            }
        )
    
    def updateSudo(self, user_id: int, rank: int) -> None:
        self.db.sudo.update_one(
            {"user_id": user_id}, {"$set": {"rank": rank}}
        )

    def getSudo(self, user_id: int) -> int:
        return self.db.sudo.find_one({"user_id": user_id})["rank"]

    def isSudo(self, user_id: int) -> bool:
        return bool(self.db.sudo.find_one({"user_id": user_id}))

    def removeSudo(self, user_id: int) -> None:
        self.db.sudo.delete_one({"user_id": user_id})

    def getAllSudos(self) -> list[dict]:
        return [sudo for sudo in self.db.sudo.find()]

    # --- Clients --- #
    def addSession(self, phone_number: int, session: str = None, password: str = None) -> None:
        self.db.sessions.insert_one(
            {
                "phone_number": phone_number,
                "session": session,
                "password": password,
            }
        )

    def getSession(self, phone_number: int) -> dict:
        return self.db.sessions.find_one({"phone_number": phone_number})

    def getAllSessions(self) -> list[dict]:
        return [data for data in self.db.sessions.find()]

    def removeSession(self, phone_number: int) -> None:
        self.db.sessions.delete_one({"phone_number": phone_number})

    def addRestrictGroup(self, chat_id: str) -> None:
        self.db.restrict.insert_one({"chat_id": chat_id})

    def removeRestrictGroup(self, chat_id: str) -> None:
        self.db.restrict.delete_one({"chat_id": chat_id})

    def getAllRestrictGroup(self):
        return [chat['chat_id'] for chat in self.db.restrict.find()]

    def isRestricted(self, chat_id: str) -> bool:
        return bool(self.db.restrict.find_one({"chat_id": chat_id}))

dataBase = MongoDB(DATABASE_URL)
