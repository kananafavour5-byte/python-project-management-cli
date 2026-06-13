import argparse

from utils.storage import load_data
from utils.storage import save_data


def add_user(name, email):
    data = load_data()

    user = {
        "id": len(data["users"]) + 1,
        "name": name,
        "email": email
    }

    data["users"].append(user)

    save_data(data)

    print(f"User added: {name} ({email})")


def list_users():
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

    print(f"Project added: {title}")


def list_projects():
    data = load_data()

    if not data["projects"]:
        print("No projects found.")
        return

    for project in data["projects"]:
        print(
            f"ID: {project['id']} | "
            f"User ID: {project['user_id']} | "
            f"{project['title']} | "
            f"Due: {project['due_date']}"
        )


def add_task(project_id, title, assigned_to):
    data = load_data()

    task = {
        "id": len(data["tasks"]) + 1,
        "project_id": project_id,
        "title": title,
        "status": "Pending",
        "assigned_to": assigned_to
    }

    data["tasks"].append(task)

    save_data(data)

    print(f"Task added: {title}")


def list_tasks():
    data = load_data()

    if not data["tasks"]:
        print("No tasks found.")
        return

    for task in data["tasks"]:
        print(
            f"ID: {task['id']} | "
            f"Project ID: {task['project_id']} | "
            f"{task['title']} | "
            f"Status: {task['status']} | "
            f"Assigned To: {task['assigned_to']}"
        )


def complete_task(task_id):
    data = load_data()

    for task in data["tasks"]:

        if task["id"] == task_id:

            task["status"] = "Completed"

            save_data(data)

            print(
                f"Task {task_id} marked as completed."
            )

            return

    print("Task not found.")


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

    # list-projects
    subparsers.add_parser(
        "list-projects",
        help="List all projects"
    )

    # add-task
    add_task_parser = subparsers.add_parser(
        "add-task",
        help="Add a task"
    )

    add_task_parser.add_argument(
        "--project-id",
        required=True,
        type=int
    )

    add_task_parser.add_argument(
        "--title",
        required=True
    )

    add_task_parser.add_argument(
        "--assigned-to",
        required=True
    )

    # list-tasks
    subparsers.add_parser(
        "list-tasks",
        help="List all tasks"
    )

    # complete-task
    complete_task_parser = subparsers.add_parser(
        "complete-task",
        help="Mark a task as completed"
    )

    complete_task_parser.add_argument(
        "--task-id",
        required=True,
        type=int
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

    elif args.command == "list-projects":
        list_projects()

    elif args.command == "add-task":
        add_task(
            args.project_id,
            args.title,
            args.assigned_to
        )

    elif args.command == "list-tasks":
        list_tasks()

    elif args.command == "complete-task":
        complete_task(
            args.task_id
        )


if __name__ == "__main__":
    main()