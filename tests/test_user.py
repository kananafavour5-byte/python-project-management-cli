from models.user import User


def test_create_user():
    user = User(
        "Alex",
        "alex@gmail.com"
    )

    assert user.name == "Alex"
    assert user.email == "alex@gmail.com"


def test_invalid_email():

    try:
        User(
            "Alex",
            "invalid-email"
        )

        assert False

    except ValueError:
        assert True