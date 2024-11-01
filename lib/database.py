from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base  # Import Base to use it for creating tables

# Create a database engine
engine = create_engine('sqlite:///events.db')  # Ensure your DB path is correct
Session = sessionmaker(bind=engine)
session = Session()

def init_db():
    """Initialize the database and create tables."""
    Base.metadata.create_all(engine)
    print("Database initialized and tables created.")
