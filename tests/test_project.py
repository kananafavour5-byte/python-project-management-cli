from models.project import Project


def test_create_project():

    project = Project(
        "CLI Tool",
        "Python CLI Application",
        "2026-08-01"
    )

    assert project.title == "CLI Tool"


def test_empty_project_title():

    try:
        Project(
            "",
            "Description",
            "2026-08-01"
        )

        assert False

    except ValueError:
        assert True