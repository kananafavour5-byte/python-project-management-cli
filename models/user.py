"""
User model.
"""

from models.person import Person


class User(Person):
    """
    Represents a user in the project management system.
    """

    next_id = 1

    def __init__(self, name, email):
        super().__init__(name)

        self.id = User.next_id
        User.next_id += 1

        self.email = email
        self.projects = []

    @property
    def email(self):
        """Get email."""
        return self._email

    @email.setter
    def email(self, value):
        """Validate email."""
        if "@" not in value:
            raise ValueError("Invalid email address.")

        self._email = value

    def add_project(self, project):
        """Add a project to user."""
        self.projects.append(project)

    def __str__(self):
        return f"User {self.id}: {self.name} ({self.email})"