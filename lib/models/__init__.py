from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Import models
from .event import Event
from .attendee import Attendee
from .registration import Registration