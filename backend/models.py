### models.py
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class LoginAttempt(Base):
    __tablename__ = "login_attempts"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False)
