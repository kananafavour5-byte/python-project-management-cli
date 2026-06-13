# Python Project Management CLI Tool

## Overview

This project is a Command-Line Interface (CLI) Project Management Tool built in Python. It allows administrators to manage users, projects, and tasks through terminal commands.

The application demonstrates:

* Object-Oriented Programming (OOP)
* Command-Line Interface development using argparse
* JSON file persistence
* Unit testing with pytest
* External package usage with Rich
* Git and GitHub workflow

---

## Features

### User Management

* Add users
* List users

### Project Management

* Add projects
* List projects

### Task Management

* Add tasks
* List tasks
* Mark tasks as completed

### Data Persistence

* Stores data in JSON format
* Loads data automatically between program runs

---

## Project Structure

project-management-cli/

├── main.py

├── models/

│ ├── person.py

│ ├── user.py

│ ├── project.py

│ └── task.py

├── utils/

│ └── storage.py

├── data/

│ └── database.json

├── tests/

│ ├── test_user.py

│ ├── test_project.py

│ └── test_task.py

├── requirements.txt

└── README.md

---

## Installation

Clone the repository:

git clone YOUR_GITHUB_REPOSITORY_URL

cd python-project-management-cli

Install dependencies:

pip3 install -r requirements.txt

---

## Usage

### Add User

python3 main.py add-user --name Alex --email [alex@gmail.com](mailto:alex@gmail.com)

### List Users

python3 main.py list-users

### Add Project

python3 main.py add-project --user-id 1 --title "CLI Tool" --description "Python CLI Project" --due-date "2026-08-01"

### List Projects

python3 main.py list-projects

### Add Task

python3 main.py add-task --project-id 1 --title "Create User Class" --assigned-to Alex

### List Tasks

python3 main.py list-tasks

### Complete Task

python3 main.py complete-task --task-id 1

---

## Running Tests

pytest

or

python3 -m pytest

---

## Technologies Used

* Python 3.12
* argparse
* JSON
* pytest
* Rich
* Git
* GitHub

---

## Author

Favour Kirema
