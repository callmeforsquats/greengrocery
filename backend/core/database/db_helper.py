from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker
from ..config import settings
class DbHerlper:
    def __init__(
            self,
            url:str,
            max_overflow:int=10,
            pool_size:int=5,
            echo:bool=False
    ):
        self.engine=create_async_engine(
            url=url,
            pool_size=pool_size,
            max_overflow=max_overflow,
            echo=echo
        )
        self.session_maker=async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False
        )
    async def close(self):
        await self.engine.dispose()

    async def get_session(self):
        async with self.session_maker() as session:
            yield session

db_helper=DbHerlper(
    url=settings.db.url,
    max_overflow=settings.db.max_overflow,
    pool_size=settings.db.pool_size,
    echo=settings.db.echo
)