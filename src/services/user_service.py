from src.models.user import User
from src.utils.string_utils import capitalize

class UserService:
    def get_user(self, name: str) -> User:
        # Simulate a database query
        email = f"{name.lower()}@example.com"
        return User(capitalize(name), email)