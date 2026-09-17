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
    docs = db.collection("clients").stream()

    print("\n=== All Clients & Projects ===")
    found_any = False

    for doc in docs:
        found_any = True
        data = doc.to_dict()
        print(f"ID: {doc.id}")
        print(f"  Client: {data.get('client_name')}")
        print(f"  Project: {data.get('project_name')}")
        print(f"  Status: {data.get('status')}")
        print()

    if not found_any:
        print("No clients or projects found.\n")


def update_project_status():
    """Updates the status field of an existing client/project."""
    # Show everything first so the user can find the right document ID
    view_clients_projects()

    doc_id = input("Enter the ID of the client/project to update: ")
    new_status = input("Enter the new status: ")

    doc_ref = db.collection("clients").document(doc_id)

    # Check the document actually exists before trying to update it
    if doc_ref.get().exists:
        doc_ref.update({"status": new_status})
        print(f"\nStatus updated to '{new_status}'.\n")
    else:
        print("\nNo client/project found with that ID.\n")

def delete_client_project():
    """Removes a client/project from the 'clients' collection."""
    # Show everything first so the user can find the right document ID
    view_clients_projects()

    doc_id = input("Enter the ID of the client/project to delete: ")

    doc_ref = db.collection("clients").document(doc_id)

    # Check the document actually exists before trying to delete it
    if doc_ref.get().exists:
        doc_ref.delete()
        print(f"\nDeleted document {doc_id}.\n")
    else:
        print("\nNo client/project found with that ID.\n")

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