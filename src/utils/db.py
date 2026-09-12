from .settings import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker


engine=create_engine(url=settings.DB_CONNECTION)

Base=declarative_base()

LocalSession=sessionmaker(bind=engine)

def get_db():
    session=LocalSession()

    try:
        yield session

    finally:
        session.close()

