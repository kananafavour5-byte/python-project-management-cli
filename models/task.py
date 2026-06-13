"""
Task model.
"""


class Task:
    """
    Represents a task belonging to a project.
    """

    next_id = 1

    def __init__(self, title, assigned_to):
        self.id = Task.next_id
        Task.next_id += 1

        self.title = title
        self.assigned_to = assigned_to
        self.status = "Pending"

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not value.strip():
            raise ValueError("Task title cannot be empty.")

        self._title = value

    def complete_task(self):
        """Mark task as completed."""
        self.status = "Completed"

    def __str__(self):
        return (
            f"Task {self.id}: "
            f"{self.title} "
            f"| Status: {self.status} "
            f"| Assigned To: {self.assigned_to}"
        )