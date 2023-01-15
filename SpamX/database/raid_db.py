
from SpamX import DATABASE_URL
if DATABASE_URL:
  import threading
  from . import SESSION, BASE
  from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    UnicodeText,
    UniqueConstraint,
    func,
    )
  from sqlalchemy.sql.sqltypes import BigInteger

  class raiders(BASE):
     __tablename__ = "raid_users"
     user_id = Column(BigInteger, primary_key=True)

     def __init__(self, user_id):
        self.user_id = user_id

     def __repr__(self):
        return "<Sudo {}>".format(self.user_id)


  raiders.__table__.create(checkfirst=True)

  ILOCK = threading.RLock()

  def add_user(user_id):
     fuk = SESSION.query(raiders).get(user_id)
     if not fuk:
        user = raiders(user_id)
        SESSION.add(user)
        SESSION.commit()

  def get_all_raiders():
    try:
        return SESSION.query(raiders).all()
    finally:
        SESSION.close()

  def rm_user(user_id):
    with ILOCK:
        user = SESSION.query(raiders).get(user_id)
        if user:
            SESSION.delete(user)
            SESSION.commit()
        else:
            SESSION.close()

  def check(user_id):
    try:
        return SESSION.query(raiders).filter(raiders.user_id == str(user_id)).one()
    except BaseException:
        return None
    finally:
        SESSION.close()

  def raid_count():
    try:
        return SESSION.query(raiders).count()
    finally:
        SESSION.close()
