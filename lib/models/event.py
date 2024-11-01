from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from . import Base
from lib.database import engine, session  # Import session and engine from the new database module

class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    date = Column(String)  # Use Date type if you prefer
    location = Column(String)

    registrations = relationship('Registration', back_populates='event', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Event(name={self.name}, date={self.date}, location={self.location})>"

Base.metadata.create_all(engine)
