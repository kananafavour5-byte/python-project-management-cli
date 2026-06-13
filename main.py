from models.user import User
from models.project import Project


user = User(
    "Alex",
    "alex@gmail.com"
)

project = Project(
    "CLI Tool",
    "Python Project Management Application",
    "2026-08-01"
)

user.add_project(project)

print(user)

print("\nProjects:")

for project in user.projects:
    print(project)