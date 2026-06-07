from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from config.config import settings

engine = create_engine(
    settings.database_url,
    echo=True,
    connect_args={"check_same_thread":False}
)


Base = declarative_base()

def init_db():
    Base.metadata.create_all(bind=engine)  # Create all tables
    print("All Tables are created")