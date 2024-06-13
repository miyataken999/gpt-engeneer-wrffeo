from dataclasses import dataclass

@dataclass
class User:
    name: str
    email: str

    def __str__(self):
        return f"User {self.name} - {self.email}"