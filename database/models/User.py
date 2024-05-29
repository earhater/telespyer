from sqlalchemy import Column, String, BigInteger, UniqueConstraint

from database.models.BaseModel import BaseModel


class User(BaseModel):
    __tablename__ = 'users'
    bio = Column(String)
    userid = Column(BigInteger, unique=True, nullable=False)
    firstname = Column(String)
    __table_args__ = (
        UniqueConstraint('userid', name='unique_userid'),
    )