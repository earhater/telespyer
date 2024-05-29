from sqlalchemy import Column

from database.models.BaseModel import Base


class Appearances(Base):
    __tablename__ = 'Appearances'
    id = Column(Integer, primary_key=True, autoincrement=True)
    channel_id = Column(BigInteger, ForeignKey('Channels.id'))