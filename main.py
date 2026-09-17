import firebase_admin
from firebase_admin import credentials, firestore

# Connect to Firebase using the Service Account key
cred = credentials.Certificate("clouddatabasetracker-firebase-adminsdk-fbsvc-6a0cee1181.json")
firebase_admin.initialize_app(cred)

# Get a client to interact with Firestore
db = firestore.client()


def add_client_project():
    """Adds a new client/project to the 'clients' collection in Firestore."""
    client_name = input("Enter client name: ")
    project_name = input("Enter project name: ")
    status = input("Enter project status (e.g. Not Started, In Progress, Complete): ")

    # add() lets Firestore auto-generate a unique document ID for us
    doc_ref = db.collection("clients").add({
        "client_name": client_name,
        "project_name": project_name,
        "status": status
    })

    print(f"\nAdded {client_name} - {project_name} to the database.\n")


def view_clients_projects():
    """Displays all clients/projects currently stored in Firestore."""
    print("\n(View feature coming soon)\n")


def update_project_status():
    """Updates the status field of an existing client/project."""
    print("\n(Update feature coming soon)\n")


def delete_client_project():
    """Removes a client/project from the 'clients' collection."""
    print("\n(Delete feature coming soon)\n")


def main():
    """Runs the console menu loop for the Client & Project Tracker."""
    while True:
        print("=== Client & Project Tracker ===")
        print("1. Add a client/project")
        print("2. View all clients/projects")
        print("3. Update a project's status")
        print("4. Delete a client/project")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_client_project()
        elif choice == "2":
            view_clients_projects()
        elif choice == "3":
            update_project_status()
        elif choice == "4":
            delete_client_project()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("\nInvalid choice, try again.\n")


if __name__ == "__main__":
    main()