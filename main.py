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


def main():

    parser = argparse.ArgumentParser(
        description="Project Management CLI"
    )

    subparsers = parser.add_subparsers(
        dest="command"
    )

    # add-user command
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

    # list-users command
    subparsers.add_parser(
        "list-users",
        help="List all users"
    )

    args = parser.parse_args()

    if args.command == "add-user":
        add_user(
            args.name,
            args.email
        )

    elif args.command == "list-users":
        list_users()


if __name__ == "__main__":
    main()