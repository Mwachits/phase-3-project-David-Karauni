# phase-3-project-David-Karauni

Event Planning and Registration System
A Command-Line Interface (CLI) application designed to assist event organizers in managing event details, registering participants, and viewing event data efficiently. Built using Python and SQLAlchemy ORM, this project aims to provide a straightforward and effective solution for managing event-related data.

## Table of Contents
1. Project Overview
2. Features
3. Getting Started
4. Usage
5. Directory Structure
6. Database Models
7. Helper Functions
8. Future Improvements
9. License
Project Overview

Event planning and participant management can be cumbersome tasks without the right tools, especially for organizers managing large-scale events. This CLI application streamlines the process by allowing users to create events, register participants, and manage data from a single, user-friendly interface. With SQLAlchemy handling data persistence, the app is robust and maintains the integrity of relationships between events and participants.

Features
Create Events: Add new events with name, date, and location details.
Register Participants: Sign up participants for specific events with their name and contact details.
View Event and Participant Data: Retrieve event details and participant lists for easy access.
Update and Delete Data: Modify or remove events and participants as necessary.
Data Persistence: Uses SQLAlchemy ORM to handle database operations and manage relationships between events and participants.
Getting Started
Prerequisites
Python 3.6+
Pipenv (for dependency management)
Installation
Clone the Repository

bash
Copy code
git clone https://github.com/yourusername/event-planning-cli.git
cd event-planning-cli
Install Dependencies Ensure you have Pipenv installed. Then, install project dependencies:

bash
Copy code
pipenv install
Activate the Virtual Environment

bash
Copy code
pipenv shell
Set Up the Database If necessary, run any migrations or database initialization commands:

bash
Copy code
python lib/models/__init__.py
Usage
Run the CLI with the following command:

bash
Copy code
python lib/cli.py
Follow the prompts to interact with the system. The main menu offers options for creating events, registering participants, viewing data, and managing records.

Example Commands
Create an Event: Follow prompts to add event name, date, and location.
Register Participant: Enter participant name, contact info, and event selection.
View Events: View a list of events or see participants for a specific event.
Update/Delete Records: Modify event or participant data as needed.
Directory Structure
bash
Copy code
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── models
    │   ├── __init__.py         # Database initialization and constants
    │   ├── event.py            # Event model
    │   ├── participant.py      # Participant model
    │   └── registration.py     # Registration model (event-participant linking)
    ├── cli.py                  # Main CLI script
    ├── debug.py                # Debugging script (if needed)
    └── helpers.py              # Helper functions for CLI operations
Database Models
Event
Represents an event with fields for:

Name: Name of the event
Date: Date of the event
Location: Location of the event
Participant
Represents a participant with fields for:

Name: Name of the participant
Contact: Contact information of the participant
Registration
Intermediate table linking events to participants:

Event ID: Links a participant to an event
Participant ID: Links a participant to the event
Helper Functions
Located in lib/helpers.py, these functions handle the core logic for managing user interactions. Here are some key functions:

create_event(): Creates a new event.
register_participant(): Registers a participant for an event.
view_events(): Displays all events.
view_participants(event_id): Shows all participants for a specific event.
update_event(event_id): Updates event details.
delete_event(event_id): Deletes an event and its registrations.
Future Improvements
Search Feature: Allow searching for events or participants by keyword.
Export to CSV: Enable exporting event and participant lists for easier sharing.
Admin Authentication: Add authentication for better security.
Multi-day Events: Support events that span multiple days.
License
This project is licensed under the MIT License.