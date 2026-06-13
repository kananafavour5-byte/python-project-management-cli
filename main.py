import argparse

from utils.storage import load_data
from utils.storage import save_data


def add_user(name, email):
    """
    Add a user to the database.
    """

    data = load_data()

    user = {
        "id": len(data["users"]) + 1,
        "name": name,
        "email": email
    }

    data["users"].append(user)

    save_data(data)

    print(
        f"User added: {name} ({email})"
    )


def list_users():
    """
    Display all users.
    """

    data = load_data()

    if not data["users"]:
        print("No users found.")
        return

    for user in data["users"]:
        print(
            f"ID: {user['id']} | "
            f"{user['name']} | "
            f"{user['email']}"
        )


def add_project(user_id, title, description, due_date):
    """
    Add a project to the database.
    """

    data = load_data()

    project = {
        "id": len(data["projects"]) + 1,
        "user_id": user_id,
        "title": title,
        "description": description,
        "due_date": due_date
    }

    data["projects"].append(project)

    save_data(data)

    print(
        f"Project added: {title}"
    )


def main():

    parser = argparse.ArgumentParser(
        description="Project Management CLI"
    )

    subparsers = parser.add_subparsers(
        dest="command"
    )

    # add-user
    add_user_parser = subparsers.add_parser(
        "add-user",
        help="Add a new user"
    )

    add_user_parser.add_argument(
        "--name",
        required=True
    )

    add_user_parser.add_argument(
        "--email",
        required=True
    )

    # list-users
    subparsers.add_parser(
        "list-users",
        help="List all users"
    )

    # add-project
    add_project_parser = subparsers.add_parser(
        "add-project",
        help="Add a project"
    )

    add_project_parser.add_argument(
        "--user-id",
        required=True,
        type=int
    )

    add_project_parser.add_argument(
        "--title",
        required=True
    )

    add_project_parser.add_argument(
        "--description",
        required=True
    )

    add_project_parser.add_argument(
        "--due-date",
        required=True
    )

    args = parser.parse_args()

    if args.command == "add-user":
        add_user(
            args.name,
            args.email
        )

    elif args.command == "list-users":
        list_users()

    elif args.command == "add-project":
        add_project(
            args.user_id,
            args.title,
            args.description,
            args.due_date
        )


if __name__ == "__main__":
    main()