## Event Registration System
This project is a Command-Line Interface (CLI) application created to manage events and attendee registrations. Built with Python, the system leverages SQLAlchemy ORM to handle database interactions, ensuring efficient data management and relationship handling between events and attendees.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Project Structure](#project-structure)
6. [Technologies Used](#technologies-used)
7. [Contributing](#contributing)
8. [License](#license)

# Project Overview
The Event Registration System offers a streamlined solution for managing events and registering attendees. Users can create events, add attendee profiles, register attendees to events, and view lists of all events and attendees. The project follows best practices for CLI applications and utilizes SQLAlchemy ORM for database management.

# Features
Event Management: Create and list events with specific details.
Attendee Management: Create and list attendee profiles.
Registration: Register attendees for events, establishing a one-to-many relationship.
Data Persistence: Use SQLAlchemy ORM for creating and managing tables with related data.
Interactive CLI: Menu-driven interface for ease of use.

# Installation
Clone the Repository
  git clone https://github.com/your-username/phase-3-project-David-Karauni.git
  
Set Up Virtual Environment
Make sure Pipenv is installed: pip install pipenv

Create a virtual environment and install dependencies: pipenv install

Activate Virtual Environment: pipenv shell

Initialize Database
Run the command to set up the database tables:
python -m lib.cli

# Usage
Launch the Application : python -m lib.cli
Menu Options
1. Create Event:	    Create a new event with name, description, date, and location.
2. Create Attendee:	    Add a new attendee profile with name and email.
3. Register Attendee:	Register an attendee for an event.
4. List Events:	        Display all created events.
5. List Attendees:	    Display all attendees in the system.
6. Exit:	            Exit the application.
7. Initialize Database:	Set up the database tables for the first time.

# Project Structure
phase-3-project-David-Karauni/
├── lib/
│   ├── __init__.py
│   ├── cli.py               # CLI logic for user interaction
│   ├── helpers.py           # Functions to handle CRUD operations
│   ├── models.py            # SQLAlchemy models for Event, Attendee, Registration
├── .venv/                   # Virtual environment folder (auto-created)
├── Pipfile                  # Pipenv dependency management
├── README.md                # Project documentation
└── LICENSE                  # License information

# Technologies Used
    Python: Core programming language.
    SQLAlchemy: ORM for database management.
    Pipenv: Virtual environment and dependency management.
    SQLite: Lightweight database for data persistence.

# Contributing
Contributions are welcome! Please follow the standard fork-and-pull workflow:
    Fork the repository.
    Create a new feature branch (git checkout -b feature/new-feature).
    Commit your changes 
    Push to the branch 
    Create a new Pull Request.

# License
This project is licensed under the MIT License. 