from datetime import datetime

from sqlalchemy import Column, Integer, TIMESTAMP
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.utcnow)
    updated_at = Column(TIMESTAMP, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return "<{0.__class__.__name__}(id={0.id!r})>".format(self)