"""
Person model.
Base class for all people in the system.
"""


class Person:
    """Base class representing a person."""

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        """Get person's name."""
        return self._name

    @name.setter
    def name(self, value):
        """Validate and set person's name."""
        if not value.strip():
            raise ValueError("Name cannot be empty.")

        self._name = value

    def __str__(self):
        return self.name