from sqlalchemy import Column, Integer, ForeignKey, String

from database.models.BaseModel import Base, BaseModel


class Channel(BaseModel):
    __tablename__ = 'channels'
    id = Column(Integer, primary_key=True, autoincrement=True)
    channel_id = Column(Integer, nullable=False)
    channel_name = Column(String, nullable=False)
