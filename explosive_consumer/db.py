
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils import database_exists, create_database

Base = declarative_base()



DATABASE_URL = "postgresql://postgres:1234@localhost:5432/messages_monitoring"

# יצירת מנוע
engine = create_engine(DATABASE_URL)

if not database_exists(engine.url):
    create_database(engine.url)

# יצירת בסיס למודלים
Base = declarative_base()

Base.metadata.create_all(bind=engine)

# יצירת מפעל סשנים
SessionLocal = sessionmaker(bind=engine)


# פונקציה ליצירת סשן חדש
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


