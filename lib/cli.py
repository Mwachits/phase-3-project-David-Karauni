from lib.helpers import create_event, create_attendee, register_attendee, list_events, list_attendees
from lib.database import init_db  # This should work if the function is defined

def main():
    while True:
        print("\nEvent Registration System")
        print("1. Create Event")
        print("2. Create Attendee")
        print("3. Register Attendee")
        print("4. List Events")
        print("5. List Attendees")
        print("6. Exit")
        print("7. Initialize Database")
        choice = input("Choose an option: ")

        if choice == '1':
            create_event()
        elif choice == '2':
            create_attendee()
        elif choice == '3':
            register_attendee()
        elif choice == '4':
            list_events()
        elif choice == '5':
            list_attendees()
        elif choice == '6':
            break
        elif choice == '7':
            init_db()  # Call the init_db function to create tables
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
