import pytest
from src.services.user_service import UserService

def test_get_user():
    user_service = UserService()
    user = user_service.get_user("John Doe")
    assert user.name == "John Doe"
    assert user.email == "johndoe@example.com"