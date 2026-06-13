from models.task import Task


def test_create_task():

    task = Task(
        "Create User Class",
        "Alex"
    )

    assert task.title == "Create User Class"
    assert task.status == "Pending"


def test_complete_task():

    task = Task(
        "Create User Class",
        "Alex"
    )

    task.complete_task()

    assert task.status == "Completed"