from sqlalchemy import Column, BigInteger, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from database.models.BaseModel import BaseModel


class Appearances(BaseModel):
    __tablename__ = 'Appearances'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    channel_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    user_id:Mapped[int] = mapped_column(BigInteger, ForeignKey('users.userid'), nullable=False)