from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base

class Attendee(Base):
    __tablename__ = 'attendees'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

    # Ensure this backref name is unique
    registrations = relationship('Registration', back_populates='attendee', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Attendee(name={self.name}, email={self.email})>"
