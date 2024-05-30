import os
from ssl import create_default_context

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from sqlalchemy.orm import sessionmaker

from database.models.BaseModel import Base
from database.models.User import User


class AlchemyCore:
    def __init__(self):
        ctx = create_default_context(cafile="root.crt")
        self.engine = create_async_engine(
            os.getenv("PG_CONNECT"),
            future=True,
            echo=False,
            pool_size=20,
            connect_args={"ssl": ctx},
            max_overflow=90,
            pool_pre_ping=True,
        )
        self.AsyncSessionLocal = sessionmaker(
            bind=self.engine,
            class_=AsyncSession,
            expire_on_commit=False
        )

    async def create_user(self,user: User) -> User:
        async with self.AsyncSessionLocal() as session:
            session.add(user)
            print("user created")
            await session.commit()
            return user

    async def create_metadata(self):
        async with self.engine.begin() as conn:
            # Create all tables
            await conn.run_sync(Base.metadata.create_all)