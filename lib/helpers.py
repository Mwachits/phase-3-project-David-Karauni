from .models import Event, Attendee, Registration
from lib.database import session  # Import session from the new database module

def create_event():
    name = input("Enter event name: ")
    description = input("Enter event description: ")
    date = input("Enter event date (YYYY-MM-DD): ")
    location = input("Enter event location: ")

    new_event = Event(name=name, description=description, date=date, location=location)
    session.add(new_event)
    session.commit()
    print(f"Event '{name}' created successfully.")

def create_attendee():
    name = input("Enter attendee name: ")
    email = input("Enter attendee email: ")

    new_attendee = Attendee(name=name, email=email)
    session.add(new_attendee)
    session.commit()
    print(f"Attendee '{name}' created successfully.")

def register_attendee():
    event_id = int(input("Enter event ID to register for: "))
    attendee_id = int(input("Enter attendee ID: "))

    registration = Registration(event_id=event_id, attendee_id=attendee_id)
    session.add(registration)
    session.commit()
    print(f"Attendee {attendee_id} registered for event {event_id} successfully.")

def list_events():
    events = session.query(Event).all()
    print("\nList of Events:")
    for event in events:
        print(event)

def list_attendees():
    attendees = session.query(Attendee).all()
    print("\nList of Attendees:")
    for attendee in attendees:
        print(attendee)
