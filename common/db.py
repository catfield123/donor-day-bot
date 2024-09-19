from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from common.config import database_settings


engine = create_engine(database_settings.database_url,
                        pool_size=5,
                        max_overflow=20)

SessionLocal = sessionmaker(engine, expire_on_commit=False, autocommit=False, autoflush=False)