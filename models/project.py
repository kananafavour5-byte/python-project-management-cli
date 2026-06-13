"""
Project model.
"""


class Project:
    """
    Represents a project belonging to a user.
    """

    next_id = 1

    def __init__(self, title, description, due_date):
        self.id = Project.next_id
        Project.next_id += 1

        self.title = title
        self.description = description
        self.due_date = due_date

        self.tasks = []

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not value.strip():
            raise ValueError("Project title cannot be empty.")

        self._title = value

    def add_task(self, task):
        self.tasks.append(task)

    def __str__(self):
        return (
            f"Project {self.id}: "
            f"{self.title} "
            f"(Due: {self.due_date})"
        )