import os
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Get the database URL from environment variable
DATABASE_URL = os.getenv('DATABASE_URL').replace("postgres://", "postgresql://")

# Create the engine
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a Session
session = Session()

# Create a base class for our classes definitions
Base = declarative_base()

# Define the Tasks model
class Tasks(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    goal = Column(String(100))
    done = Column(Boolean, default=False)

# Create the database tables
Base.metadata.create_all(engine)

# Close the session
session.close()