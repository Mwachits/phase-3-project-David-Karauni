from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from . import Base
from .event import Event
from .attendee import Attendee
from lib.database import engine, session  # Import session and engine from the new database module

class Registration(Base):
    __tablename__ = 'registrations'

    id = Column(Integer, primary_key=True)
    attendee_id = Column(Integer, ForeignKey('attendees.id'))
    event_id = Column(Integer, ForeignKey('events.id'))

    attendee = relationship('Attendee', back_populates='registrations')
    event = relationship('Event', back_populates='registrations')

    def __repr__(self):
        return f"<Registration(attendee_id={self.attendee_id}, event_id={self.event_id})>"

Base.metadata.create_all(engine)
