from models.user import User
from models.project import Project
from models.task import Task


user = User(
    "Alex",
    "alex@gmail.com"
)

project = Project(
    "CLI Tool",
    "Python Project Management Application",
    "2026-08-01"
)

task1 = Task(
    "Create User Class",
    "Alex"
)

task2 = Task(
    "Build CLI Commands",
    "Alex"
)

project.add_task(task1)
project.add_task(task2)

user.add_project(project)

print(user)

print("\nProjects:")

for project in user.projects:
    print(project)

    print("Tasks:")

    for task in project.tasks:
        print(task)