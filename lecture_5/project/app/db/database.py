from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Define URL of the database
DATABASE_URL = "sqlite:///./db/books.db"


# Create the SQLAlchemy engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)


# Create database sessions for each request
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


# Create Base class for all ORM models
Base = declarative_base()


# Create the table
def init_db():
    Base.metadata.create_all(bind=engine)
