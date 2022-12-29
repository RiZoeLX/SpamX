
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

  class Sudos(BASE):
    __tablename__ = "SpamXSudos"
    user_id = Column(BigInteger, primary_key=True)

    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return "<Sudo {}>".format(self.user_id)


  Sudos.__table__.create(checkfirst=True)

  ILOCK = threading.RLock()

  def addsudo(user_id):
    fuk = SESSION.query(Sudos).get(user_id)
    if not fuk:
        user = Sudos(user_id)
        SESSION.add(user)
        SESSION.commit()

  def get_all_sudos():
    try:
        return SESSION.query(Sudos).all()
    finally:
        SESSION.close()

  def rmsudo(user_id):
    with ILOCK:
        user = SESSION.query(Sudos).get(user_id)
        if user:
            SESSION.delete(user)
            SESSION.commit()
        else:
            SESSION.close()

  def check_sudo(user_id):
    try:
        return SESSION.query(Sudos).filter(Sudos.user_id == str(user_id)).one()
    except BaseException:
        return None
    finally:
        SESSION.close()

  def sudo_count():
    try:
        return SESSION.query(Sudos).count()
    finally:
        SESSION.close()
