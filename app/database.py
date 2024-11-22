from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# PostgreSQL database URL
DATABASE_URL = "postgresql+psycopg2://postgres:password@localhost:5432/postgres"

# SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Base class for models
Base = declarative_base()

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)