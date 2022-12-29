"""Postgres Database"""
from SpamX import DATABASE_URL
if DATABASE_URL:
  import sqlalchemy
  from sqlalchemy.ext.declarative import declarative_base
  from sqlalchemy.orm import scoped_session
  from sqlalchemy.orm import sessionmaker

  def start() -> scoped_session:
     engine = sqlalchemy.create_engine(DATABASE_URL, client_encoding="utf8")
     BASE.metadata.bind = engine
     BASE.metadata.create_all(engine)
     return scoped_session(sessionmaker(bind=engine, autoflush=False))

  BASE = declarative_base()
  SESSION = start()
