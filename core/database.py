from settings import DATABASE_URL;
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession;
from sqlalchemy.orm import declarative_base;

engine = create_async_engine(DATABASE_URL, echo=True)

SessionLocal = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

Base = declarative_base()

async def get_db_session():
    async with SessionLocal() as session:
        yield session